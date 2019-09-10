import time
import board
import neopixel
import adafruit_hcsr04
import adafruit_fancyled.adafruit_fancyled as fancy
from myfunction import mape
from constrain import clamp

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D4, echo_pin=board.D3)

while True:
    try:
        color = fancy.CHSV(int(round(mapp(clamp(sonar.distance,5,35), 5, 35, 255, 85))), 255, 50)
        packed = color.pack()
        dot.fill(packed)#turns the board's led on
    except RuntimeError:
        print("Retrying!")
        pass
    time.sleep(0.1)
    #map
    '''def mape(x,in_min,in_max,out_min,out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min'''
    #constrain
    '''def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)'''