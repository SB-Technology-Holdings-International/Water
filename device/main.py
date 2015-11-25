import gpio
import datetime
import time
import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler
from threading import Thread

last_update = ''
schedule = [100] # In seconds past midnight

class server(Thread):
    def run(self):
        def some_function():
            print "some_function got called"

        class RequestHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path == '/local-control':
                    # Insert code here
                    some_function()

                self.send_response(200)

        httpd = SocketServer.TCPServer(("", 8080), RequestHandler)
        httpd.serve_forever()

class controller(Thread):
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
                                          datetime.timedelta(seconds=schedule[0])):
                print "Turning on"
                schedule.pop(0)

        # Reduce cpu usage
        time.sleep(0.1)
