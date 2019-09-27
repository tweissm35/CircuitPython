import digitalio #pylint: disable-msg=import-error
import time

class fancyLED:
    def __init__(self,one,two,three):
        self.bone = digitalio.DigitalInOut(one)
        self.btwo = digitalio.DigitalInOut(two)
        self.bthree = digitalio.DigitalInOut(three)

        self.bone.direction = digitalio.Direction.OUTPUT
        self.btwo.direction = digitalio.Direction.OUTPUT
        self.bthree.direction = digitalio.Direction.OUTPUT
    def alternate(self):
        self.bthree = True
        self.bone = True
        time.sleep(1)
        self.bthree = False
        self.bone = False
        self.btwo = True
    def off(self):
        self.bthree = False
        self.bone = False
        self.btwo = False
    def blink(self):
        self.bthree = True
        self.bone = True
        self.btwo = True
        time.sleep(1)
        self.bthree = False
        self.bone = False
        self.btwo = False
    def chase(self):
        #stuff goes here
        self.bthree = False

