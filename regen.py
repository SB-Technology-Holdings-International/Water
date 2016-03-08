#!/usr/bin/python -u
# coding=utf-8
"""
Generate certificates via Let's Encrypt
"""
import re
from subprocess import check_output, check_call
from os import path

import click
from colorama import Fore
import pexpect

# Extract the file/challenge from the LetsEncrypt output e.g.
CREX = re.compile(
    ".well-known\/acme-challenge\/(\S+) before continuing:\s+(\S+)",
    re.MULTILINE
)

MODULE_CONFIG = 'module.yaml'  # The file in our project root
APPENGINE_URL = ("https://console.cloud.google.com/" +
                 "appengine/settings/certificates")


def get_default_email():
    """Get a default user email from the git config."""
    return check_output(['git', 'config', 'user.email']).strip()


@click.command()
@click.option('--appid', '-A', prompt=True)
@click.option('--test/--no-test', default=True)
@click.option('--domains', '-d', multiple=True)
@click.option('--app-path', default=path.abspath(path.dirname(__file__)))
@click.option('--acme-path', required=True)
@click.option('--email', default=get_default_email)
def gen(test, appid, domains, acme_path, app_path, email):
    """Regenerate the keys.

    Run all the steps, being:
        1. Call Let's Encrypt
        2. Capture the challenges from the LE output
        3. Deploy the AppEngine module
        4. Print Cert. to terminal
    """
    common_name = domains[0]  # noqa

    sans = " ".join(domains)  # noqa
    click.echo("""
        APPID: {appid}
        Test: {test}
        Common Name: {common_name}
        Domain(s): {sans}
        App Path: {app_path}
        ACME path: {acme_path}
        User Email: {email}
    """.format(**{
        k: Fore.YELLOW + str(v) + Fore.RESET
        for k, v in locals().items()
    }))

    CERT_PATH = acme_path
    KEY_PATH = acme_path
    CHAIN_PATH = acme_path
    FULLCHAIN_PATH = acme_path
    CONFIG_DIR = acme_path
    WORK_DIR = path.join(acme_path, 'tmp')
    LOG_DIR = path.join(acme_path, 'logs')

    cmd = [
        'letsencrypt',
        'certonly',
        '--rsa-key-size',
        '2048',
        '--manual',
        '--agree-tos',
        '--manual-public-ip-logging-ok',
        '--text',
        '--cert-path', CERT_PATH,
        '--key-path', KEY_PATH,
        '--chain-path', CHAIN_PATH,
        '--fullchain-path', FULLCHAIN_PATH,
        '--config-dir', CONFIG_DIR,
        '--work-dir', WORK_DIR,
        '--logs-dir', LOG_DIR,
        '--email', email,
        '--domain', ",".join(domains),
    ]
    if test:
        cmd.append('--staging')

    print("$ " + Fore.MAGENTA + " ".join(cmd) + Fore.RESET)

    le = pexpect.spawn(" ".join(cmd))

    out = ''
    idx = le.expect(["Press ENTER", "Select the appropriate number"])
    if idx == 1:
        # 1: Keep the existing certificate for now
        # 2: Renew & replace the cert (limit ~5 per 7 days)
        print le.before + le.after
        le.interact("\r")
        print "..."
        le.sendline("")
        if le.expect(["Press ENTER", pexpect.EOF]) == 1:
            # EOF - User chose to not update certs.
            return
    out += le.before
    # Hit "Enter" for each domain; we extract all challenges at the end;
    # We stop just at the last "Enter to continue" so we can publish
    # our challenges on AppEngine.
    for i in xrange(len(domains) - 1):
        le.sendline("")
        le.expect("Press ENTER")
        out += le.before

    # The challenges will be in `out` in the form of CREX
    challenges = CREX.findall(out)
    if not challenges:
        raise Exception("Expected challenges from the output")

    for filename, challenge in challenges:
        filepath = path.join(app_path, "challenges", filename)
        print "[%s]\n\t%s\n\t=> %s" % (
            Fore.BLUE + filepath + Fore.RESET,
            Fore.GREEN + filename + Fore.RESET,
            Fore.YELLOW + challenge + Fore.RESET
        )
        with open(filepath, 'w') as f:
            f.write(challenge)

    # Deploy to AppEngine
    cmd = [
        'appcfg.py',
        'update',
        '-A', appid,
        path.join(app_path, MODULE_CONFIG)
    ]
    print("$ " + Fore.MAGENTA + " ".join(cmd) + Fore.RESET)
    check_call(cmd)

    # After deployment, continue the Let's Encrypt (which has been waiting
    # on the last domain)
    le.sendline("")
    le.expect(pexpect.EOF)
    le.close()
    if le.exitstatus:
        print Fore.RED + "\nletsencrypt failure: " + Fore.RESET + le.before
        return
    print "\nletsencrypt complete.", le.before

    # Convert the key to a format AppEngine can use
    # LE seems to choose the domain at random, so we have to pluck it.

    CPATH_REX = (
        "Your certificate and chain have been saved at (.+)fullchain\.pem\."
    )
    outstr = le.before.replace("\n", "").replace('\r', '')
    results = re.search(CPATH_REX, outstr, re.MULTILINE)

    LIVE_PATH = "".join(results.group(1).split())
    CHAIN_PATH = path.join(LIVE_PATH, "fullchain.pem")
    PRIVKEY_PATH = path.join(LIVE_PATH, "privkey.pem")
    cmd = [
        'openssl', 'rsa',
        '-in', PRIVKEY_PATH,
        '-outform', 'pem',
        '-inform', 'pem'
    ]
    print "$ " + Fore.MAGENTA + " ".join(cmd) + Fore.RESET
    priv_text = check_output(cmd)
    with open(CHAIN_PATH, 'r') as cp:
        pub_text = cp.read()

    print """
    --- Private Key ---
    at {PRIVKEY_PATH}
    (the above file must be converted with {cmd} to a format usable by
     AppEngine, the result of which will be as follows)

{priv_text}

    --- Public Key Chain ---
    at {CHAIN_PATH}

{pub_text}

    ✄ Copy the above into the respective fields of AppEngine at

      https://console.cloud.google.com/appengine/settings/certificates

    """.format(
        PRIVKEY_PATH=PRIVKEY_PATH,
        priv_text=Fore.RED + priv_text + Fore.RESET,
        CHAIN_PATH=CHAIN_PATH,
        pub_text=Fore.BLUE + pub_text + Fore.RESET,
        cmd=Fore.MAGENTA + " ".join(cmd) + Fore.RESET,
    )


if __name__ == '__main__':
    gen()
