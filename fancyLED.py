import digitalio #pylint: disable-msg=import-error
import random
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
        self.btwo.value = False
        self.bthree.value = True
        self.bone.value = True
        time.sleep(1)
        self.btwo.value = True
        self.bthree.value = False
        self.bone.value = False
    def off(self):
        self.bthree.value = False
        self.bone.value = False
        self.btwo.value = False
    def blink(self):
        self.bthree.value = True
        self.bone.value = True
        self.btwo.value = True
        time.sleep(1)
        self.bthree.value = False
        self.bone.value = False
        self.btwo.value = False
    def chase(self):
        self.bthree.value = False
        self.btwo.value = False
        self.bone.value = True
        time.sleep(0.5)
        self.bthree.value = False
        self.btwo.value = True
        self.bone.value = False
        time.sleep(0.5)
        self.bthree.value = True
        self.btwo.value = False
        self.bone.value = False
        time.sleep(0.5)
        self.bthree.value = False
        self.btwo.value = False
        self.bone.value = False
    def sparkle(self):
        ran = random.randint(0,2)
        if(ran == 0):
            self.bthree.value = True
            time.sleep(random.random())
            self.bthree.value = True
        elif(ran == 1):
            self.btwo.value = True
            time.sleep(random.random())
            self.btwo.value = False
        elif(ran == 2):
            self.bone.value = True
            time.sleep(random.random())
            self.bone.value = False

