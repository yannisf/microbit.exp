# Imports go at the top
from microbit import *

i1 = Image('00500:'
           '07000:'
           '98765:'
           '07000:'
           '00500')

i2 = Image('00500:'
           '00070:'
           '56789:'
           '00070:'
           '00500')

i3 = Image('00900:'
           '07870:'
           '50705:'
           '00600:'
           '00500')

i4 = Image('00500:'
           '00600:'
           '50705:'
           '07870:'
           '00900')

def direction(sorted_keys):
    if sorted_keys[0] == 'z':
        key = sorted_keys[1]
    else:
        key = sorted_keys[0]
    if xyz[key] > 0:
        d = "{}+".format(key)
    else:
        d = "{}-".format(key)
    return d

while True:
    xyz = {
        'x': accelerometer.get_x(),
        'y': accelerometer.get_y(),
        'z': accelerometer.get_z(),
    }
    sorted_keys = sorted(xyz, key=lambda k: abs(xyz[k]), reverse=True)
    d = direction(sorted_keys)
    print(d)
    if d == 'x+': display.show(i2)
    if d == 'x-': display.show(i1)
    if d == 'y+': display.show(i4)
    if d == 'y-': display.show(i3)
    sleep(50)
