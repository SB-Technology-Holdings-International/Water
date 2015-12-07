import gpio
import datetime
import time
import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler
import threading


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/local-control':
            # Insert code here
            pass

        self.send_response(200)

httpd = SocketServer.TCPServer(("", 8080), RequestHandler)

def server(a):
    print a
    httpd.serve_forever()


def controller(a, stop_event):
    # Valve GPIO pin mapping
    valves = [135, 136, 137, 138] # Not actual values
    # Setup GPIO
    #gpio.pin_mode(valves[0], 'out')
    #gpio.pin_mode(valves[1], 'out')
    #gpio.pin_mode(valves[2], 'out')
    #gpio.pin_mode(valves[3], 'out')
    # Define variables
    last_update = ''
    schedule = [(0, 1000), (0, 1009)] # (valve number, seconds past midnight)
    print "ok"
    while(not stop_event.isSet()):
        # Update once a day
        if last_update != datetime.date.today():
            print "Updating from server..."
            # Fetch latest data
            # If things work out:
            last_update = datetime.date.today()

        if schedule != []:
            if datetime.datetime.now() > (datetime.datetime.combine(datetime.date.today(),
                                          datetime.datetime.min.time()) +
                                          datetime.timedelta(seconds=schedule[0][1])):
                print "Turning on"
                #gpio.digital_write(valves[schedule[0][0]], 1)
                schedule.pop(0)

        # Reduce cpu usage
        time.sleep(0.5)
        print "Test"

t1_stop= threading.Event()
t1 = threading.Thread(target=server, args=(1, t1_stop))
t1.start()

t2_stop = threading.Event()
t2 = threading.Thread(target=controller, args=(1, t2_stop))
t2.start()
raw_input("Press enter to stop")
t2_stop.set()
t1_stop.set()
httpd.server_close()
