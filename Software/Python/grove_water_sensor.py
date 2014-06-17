# GrovePi + Grove Water Sensor
# http://www.seeedstudio.com/wiki/Grove_-_Water_Sensor

import time
import grovepi

# Connect the Water Sensor to digital port D2
water_sensor = 2

grovepi.pinMode(water_sensor,"INPUT")

while True:
    try:
        print grovepi.digitalRead(water_sensor)
        time.sleep(.5)

    except IOError:
        print "Error"
