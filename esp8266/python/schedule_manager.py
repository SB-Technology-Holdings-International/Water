schedule_list = []

class ScheduleItem:
    def __init__(self, valve_number, start_time, length):
        self.start_time = start_time
        self.length = length
        self.valve_number = valve_number
        self.done = False
        valve_number_table = [14, 12, 13, 4]
        self.valve_gpio = valve_number_table[valve_number]

        self.pin = machine.Pin(self.valve_gpio, machine.Pin.OUT)
        self.pin.high()

    def check_timing(self):
        now = time.time()
        now_tuple = time.localtime()
        today = time.mktime((now_tuple[0], now_tuple[1], now_tuple[2], 0, 0, 0, now_tuple[6], now_tuple[7]))
        start = today + self.start_time
        end = today + self.start_time + self.length

        if (now > start and now < end):
            # Turn on valve
            print('on')

        if now > end:
            # Turn off valve
            print('off')
            self.done = True

def get_schedule():
    global schedule_list
    temp_schedule_list = []
    url = 'https://watering-web-client.appspot.com/_ah/api/water/v1/getschedule?alt=json'
    response = http_client.post(url, json={'device_id': '000'})
    schedule = response.json()
    for s in schedule['schedule']:
        start = int(s['start_time'])
        duration = int(s['duration_seconds'])
        valve = int(s['valve'])
        temp_schedule_list.append(ScheduleItem(start_time=start, valve_number=valve, length=duration))
    if temp_schedule_list:
        schedule_list = temp_schedule_list

def add_item(item):
    global schedule_list
    schedule_list.append(item)
