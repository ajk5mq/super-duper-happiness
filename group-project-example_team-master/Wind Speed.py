# Wind Speed Calculation
# Andy Kehr, Sept 2018
# Simple script that counts each time the anemometer spins, keeping track of the distance and therefore velocity

import math
import time
from gpiozero import Button


wind_count = 0

radius = 9.0 # measure for individual anemometer
interval = 5 # number of seconds to wait between wind speed measurements
circ_cm = 2 * (math.pi) * radius
circ_in = circ_cm * 0.393701
distance = circ_cm * rotations

def spin():
    rotations = wind_count / 2

def wind_speed(seconds):
    global wind_count



windsensor = Button(5)
windsensor.when_pressed = spin

while True:
    '''calculates wind speed on a 5 second interval and prints to the terminal'''
    speed_met = wind_speed_met(interval)
#   speed_imp = wind_speed_imp(interval)
    time.sleep(interval)
    print(speed_met + "kph")
#   print(speed_imp + "mph")
