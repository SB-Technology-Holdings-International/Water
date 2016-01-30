import gpio
import datetime
import time
from twisted.web import server, resource
from twisted.internet import reactor
from apiclient.discovery import build

class Schedule:
    def __init__(self, valve_number, start_time, length, valve_gpio):
        self.start_time = start_time
        self.length = length
        self.valve_number = valve_number
        self.valve_gpio = valve_gpio
        gpio.pin_mode(self.valve_gpio, 'out')
    def check_timing(self):
        now = datetime.datetime.now()
        start = datetime.datetime.combine(datetime.date.today(),
                datetime.datetime.min.time()) +
                datetime.timedelta(seconds=self.start_time)
        end = datetime.datetime.combine(datetime.date.today(),
              datetime.datetime.min.time()) +
              datetime.timedelta(seconds=self.start_time + self.length)

        if (now > start and now < end):
            # Turn on valve
            print "Turn on"
        if now > end:
            # Turn off valve
            print "off"

class Simple(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return "<html>%s Iterations!</html>"%n

def main():
    # Valve GPIO pin mapping
    valves = [135, 136, 137, 138] # Not actual values
    # Define variables
    last_update = ''
    schedule_list = [()]
    schedule_list = [Schedule(start_time=6700), Schedule(), Schedule(), Schedule()] # (valve number, seconds past midnight, length)
    site = server.Site(Simple())
    reactor.listenTCP(9000, site)
    reactor.startRunning(False)
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


        time.sleep(0.001)
        reactor.iterate()

if __name__=="__main__":
    main()
