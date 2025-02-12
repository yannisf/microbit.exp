# Imports go at the top
from microbit import *
import math

left = Image('00500:'
             '07000:'
             '98765:'
             '07000:'
             '00500')

bottom_left = Image('00005:'
                    '30060:'
                    '50700:'
                    '78000:'
                    '97530')

right = Image('00500:'
              '00070:'
              '56789:'
              '00070:'
              '00500')

top_right = Image('03579:'
                  '30087:'
                  '00705:'
                  '06003:'
                  '50000')

top_left = Image('97530:'
                 '78000:'
                 '50700:'
                 '30060:'
                 '00005')

bottom_right = Image('50000:'
                     '06003:'
                     '00705:'
                     '00087:'
                     '03579')


top = Image('00900:'
            '07870:'
            '50705:'
            '00600:'
            '00500')

bottom = Image('00500:'
               '00600:'
               '50705:'
               '07870:'
               '00900')

def direction(components):
    x = components['x']
    y = components['y']
    theta = math.degrees(math.atan2(y, x))  # Convert atan2 result to degrees
    if theta < 0:
        theta += 360  # Ensure θ is in [0, 360]
    return theta
    

while True:
    xyz = {
        'x': accelerometer.get_x(),
        'y': accelerometer.get_y(),
        'z': accelerometer.get_z(),
    }
    d = direction(xyz)
    if d >= 325 or d < 35: display.show(right)
    if d >= 35 and d < 55: display.show(bottom_right)
    if d >= 55 and d < 125: display.show(bottom)
    if d >= 125 and d < 145: display.show(bottom_left)
    if d >= 145 and d < 215: display.show(left)
    if d >= 215 and d < 235: display.show(top_left)
    if d >= 235 and d < 305: display.show(top)
    if d >= 305 and d < 325: display.show(top_right)
    print(d)
    sleep(50)

