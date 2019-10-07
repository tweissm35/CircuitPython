import time
import board#pylint: disable-msg=import-error
import neopixel#pylint: disable-msg=import-error
import adafruit_hcsr04#pylint: disable-msg=import-error
import adafruit_fancyled.adafruit_fancyled as fancy#pylint: disable-msg=import-error
from myfunction import mapp
from constrain import clamp

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)#create a neopixel object at pin neopixel that is only one led long
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D4, echo_pin=board.D3)#create a distance sensor object with a trigger pin(the one making the sound) at 4 and an echo pin (the one receiving) at 3

while True:
    try:#do this unless there is an error
        color = fancy.CHSV(int(round(mapp(clamp(sonar.distance,5,35), 5, 35, 255, 85))), 255, 50)#take the distance value and make the minimum 5cm and the max 35cm, then map the distance value in its range to a range from 255 to 85, then set the hue component of "color" equal to it. Saturation is permenantly 255 and value is always 50
        packed = color.pack()#turn hue, saturation, and value into one number called "packed"
        dot.fill(packed)#make the led turn whatever color packed is
    except RuntimeError:#if there is an error do this (with the ultrasonic sensor this usually means something is too far away)
        print("Retrying!")
    time.sleep(0.1)
    #mapp is defined like this
    '''def mapp(x,in_min,in_max,out_min,out_max): 
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min'''
    #constrain is defined like this
    '''def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)'''