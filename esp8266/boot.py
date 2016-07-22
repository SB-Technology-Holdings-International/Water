# This file is executed on every boot (including wake-boot from deepsleep)

import gc
#import webrepl
#webrepl.start()
import machine
pin = machine.Pin(2, machine.Pin.OUT)
pin.high()
gc.collect()
