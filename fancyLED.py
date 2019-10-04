import digitalio #pylint: disable-msg=import-error
import random #import library "random" ↑↑↑this is changes an import error to a warning
import time

class fancyLED:
    def __init__(self,one,two,three):
        self.bone = digitalio.DigitalInOut(one)#creates a digitalio object called "bone" with pin "one"
        self.btwo = digitalio.DigitalInOut(two)
        self.bthree = digitalio.DigitalInOut(three)

        self.bone.direction = digitalio.Direction.OUTPUT#sets the direction to output
        self.btwo.direction = digitalio.Direction.OUTPUT
        self.bthree.direction = digitalio.Direction.OUTPUT
    def alternate(self):#assuming you have the leds in order makes the middle one light up and the outer ones
        self.btwo.value = False#turn led #2 off
        self.bthree.value = True#turns led #3 on
        self.bone.value = True
        time.sleep(1)#one second delay
        self.btwo.value = True
        self.bthree.value = False
        self.bone.value = False
    def off(self):#turns everything off
        self.bthree.value = False
        self.bone.value = False
        self.btwo.value = False
    def blink(self):#turns every led on and then off
        self.bthree.value = True
        self.bone.value = True
        self.btwo.value = True
        time.sleep(1)
        self.bthree.value = False
        self.bone.value = False
        self.btwo.value = False
    def chase(self):#turns one led on at a time and moves down the line
        self.bthree.value = False
        self.btwo.value = False
        self.bone.value = True
        time.sleep(0.4)
        self.bthree.value = False
        self.btwo.value = True
        self.bone.value = False
        time.sleep(0.4)
        self.bthree.value = True
        self.btwo.value = False
        self.bone.value = False
        time.sleep(0.4)
        self.bthree.value = False
        self.btwo.value = False
        self.bone.value = False
    def sparkle(self):#picks a random led to light up for a random amount of time, repeats
        for x in range(25):#repeats 25 times
            ran = random.randint(0,2)#pick a random integer starting at 0 and ending at 2
            if(ran == 0):#testing to see which led was chosen
                self.bthree.value = True
                time.sleep(random.random()/2)#delay is half a float between 0 and 1(dividing by two to make it faster)
                self.bthree.value = False
            elif(ran == 1):
                self.btwo.value = True
                time.sleep(random.random()/2)
                self.btwo.value = False
            elif(ran == 2):
                self.bone.value = True
                time.sleep(random.random()/2)
                self.bone.value = False

