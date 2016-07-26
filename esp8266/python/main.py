import time
import http_client
import network
from machine import Timer
import websocket_server

DEVICE_ID = '000' # Must be user set

tim = Timer(-1)

tim.init(period=3600000, mode=Timer.PERIODIC, callback=lambda t:time.time())

schedule_list = []

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('not connected to network...')
        # Allow user to set network config

    print('network config:', wlan.ifconfig())

class Schedule:
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
    schedule_list = []
    url = 'https://watering-web-client.appspot.com/_ah/api/water/v1/getschedule?alt=json'
    response = http_client.post(url, json={'device_id': '000'})
    schedule = response.json()
    for s in schedule['schedule']:
        start = int(s['start_time'])
        duration = int(s['duration_seconds'])
        valve = int(s['valve'])
        schedule_list.append(Schedule(start_time=start, valve_number=valve, length=duration))
    return schedule_list



do_connect()
schedule_list = get_schedule()
time.time()
websocket_server.start()
