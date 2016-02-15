import gpio
import datetime
import time
from twisted.web import server, resource
from twisted.internet import reactor
from apiclient.discovery import build

class Schedule:
    self.done = False
    def __init__(self, valve_number, start_time, length):
        self.start_time = start_time
        self.length = length
        self.valve_number = valve_number
        if valve_number == 0:
            self.valve_gpio = 0000
        elif valve_number == 1:
            self.valve_gpio = 0000
        elif valve_number == 2:
            self.valve_gpio = 0000
        elif valve_number == 3:
            self.valve_gpio = 0000

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
            gpio.digital_write(self.valve_gpio, 1)

        if now > end:
            # Turn off valve
            gpio.digital_write(self.valve_gpio, 0)
            self.done = True

class Simple(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return "<html>%s Iterations!</html>"%n

def main():
    # setup endpoints
    api_root = 'https://watering-web-client.appspot.com/_ah/api'
    api = 'water'
    version = 'v1'
    discovery_url = '%s/discovery/v1/apis/%s/%s/rest' % (api_root, api, version)
    service = build(api, version, discoveryServiceUrl=discovery_url)

    # Define variables
    last_update = None
    reactor.listenTCP(9000, site)
    reactor.startRunning(False)

    while True:
        # Update once a day
        if last_update != datetime.date.today():
            print "Updating from server..."
            schedule_list = []
            schedule = service.get_schedule(body={'device_id': '000'}).execute()
            # Format
            for s in schedule['schedule']:
                start = int(s['start_time'])
                duration = int(s['duration_seconds'])
                valve = int(s['valve'])
                schedule_list.append(Schedule(start_time=start, valve_number=valve, length=duration))
            # If things work out:
            last_update = datetime.date.today()

        if schedule_list != []:
            for i in schedule_list:
                i.check_timing()
                if i.done:
                    a.remove(i)

        time.sleep(0.001)
        reactor.iterate()

if __name__=="__main__":
    main()
