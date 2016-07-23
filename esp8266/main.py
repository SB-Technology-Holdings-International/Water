import time
import http_client
import network
from machine import Timer
tim = Timer(-1)

tim.init(period=3600000, mode=Timer.PERIODIC, callback=lambda t:time.time())



def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('not connected to network...')
        # Allow user to set network config

    print('network config:', wlan.ifconfig())

do_connect()
time.time()
