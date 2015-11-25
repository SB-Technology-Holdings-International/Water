import atexit

open_pins = []

def sys_write(path, value):
    f = open('/sys/class/gpio/' + str(path), 'w')
    f.write(str(value))
    f.close()

def sys_read(path):
    f = open('/sys/class/gpio/' + str(path), 'r')
    value = f.read()
    f.close()
    return value

def create(pin):
    pin = str(pin)
    sys_write('export', pin)
    open_pins.append(pin)

def distroy(pin):
    sys_write('unexport', pin)

def pin_mode(pin, direction):
    pin = str(pin)
    sys_write('gpio' + pin + '/direction', direction)

def digital_write(pin, value):
    pin = str(pin)
    sys_write('gpio' + pin + '/value', value)

def clean():
    for p in open_pins:
        if 'out' in sys_read('gpio' + p + '/direction'):
            digital_write(p, 0)
        distroy(p)
        open_pins.remove(p)

atexit.register(clean)
