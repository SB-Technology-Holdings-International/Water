import gpio
import datetime
import time
from twisted.web import server, resource
from twisted.internet import reactor

class Simple(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return "<html>%s Iterations!</html>"%n

def main():
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
