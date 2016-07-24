# This file is executed on every boot (including wake-boot from deepsleep)

import gc
#import webrepl
#webrepl.start()
import machine
import ntptime
ntptime.settime()

pin = machine.Pin(2, machine.Pin.OUT)
pin.low()
gc.collect()
