import gpio
import datetime
import time
import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler
import threading

class Server(threading.Thread):
    def __init__(self):
        super(Server, self).__init__()
        self._stop = threading.Event()
    def run(self):

        class RequestHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path == '/local-control':
                    # Insert code here
                    pass

                self.send_response(200)

        httpd = SocketServer.TCPServer(("", 8080), RequestHandler)
        httpd.serve_forever()
    def stop(self):
        self._stop.set()
    def stopped(self):
        return self._stop.isSet()

class Controller(threading.Thread):
    def __init__(self):
        super(Controller, self).__init__()
        self._stop = threading.Event()
    def run(self):
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

        while True:
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

            if self._stop.isSet():
                print "Controller off"
                break
            # Reduce cpu usage
            time.sleep(0.1)
    def stop(self):
        self._stop.set()
    def stopped(self):
        return self._stop.isSet()


def main():
    t1_stop= threading.Event()
    t1 = threading.Thread(target=thread1, args=(1, t1_stop))

    t2_stop = threading.Event()
    t2 = threading.Thread(target=thread2,  args=(2, t2_stop))

    raw_input("Press enter to stop")
    print "Stopping"
    #stop the thread2
    t1_stop.set()
    t2_stop.set()

Server().start()
a = Controller().start()
print a
raw_input("Press enter to stop ")
print "Stopping"
a.stop()
Server().stop()
