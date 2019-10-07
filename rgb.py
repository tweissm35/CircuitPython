

import time
class RGB:

    import digitalio #pylint: disable-msg=import-error
    import pulseio #pylint: disable-msg=import-error

    def __init__(self, red, green, blue):
        self.mred = self.pulseio.PWMOut(red, frequency=5000, duty_cycle=65535)#create a pulseio object called "mred" using pin "red" with a frequency of 5,000 Hz and a 16-bit integer which is a fraction that represents how much of one cycle is high or low
        self.mgreen = self.pulseio.PWMOut(green, frequency=5000, duty_cycle=65535)
        self.mblue = self.pulseio.PWMOut(blue, frequency=5000, duty_cycle=65535)

    def red(self):
        self.mgreen.duty_cycle = 65535#turn the green on for 0% of the time
        self.mblue.duty_cycle = 65535#turn the blue on for 0% of the time
        self.mred.duty_cycle = 0#turn the red on for 100% of the time

    def green(self):
        self.mred.duty_cycle = 65535#This is a common anode led, so normally this would be high
        self.mblue.duty_cycle = 65535
        self.mgreen.duty_cycle = 0

    def blue(self):
        self.mgreen.duty_cycle = 65535
        self.mred.duty_cycle = 65535
        self.mblue.duty_cycle = 0

    def cyan(self):
        self.mred.duty_cycle = 65535#turn the red on for 0% of the time
        self.mblue.duty_cycle = int(65535*0.5)#turn the blue on for 50% of the time
        self.mgreen.duty_cycle = int(65535*0.5)#turn the green on for 50% of the time

    def magenta(self):
        self.mgreen.duty_cycle = 65535
        self.mred.duty_cycle = int(65535*0.5)
        self.mblue.duty_cycle = int(65535*0.5)

    def yellow(self):
        self.mblue.duty_cycle = 65535
        self.mred.duty_cycle = int(65535*0.5)
        self.mgreen.duty_cycle = int(65535*0.5)

    def rainbow(self, rate):

        for i in range(1, 1001, int(rate)):#loop that goes from 1 to 1000 incrementing by the inputed rate
            self.mred.duty_cycle = int(i/1000*65535)#fade red from being on 100% of the time to 0%
            self.mgreen.duty_cycle = int(65535 - i/1000*65535)#fade green from being on 0% of the time to 100%
            time.sleep(0.01)#small delay so you can see each change


        for i in range(0,1001, rate):
            self.mgreen.duty_cycle = int(i/1000*65535)#fade green from being on 100% of the time to 0%
            self.mblue.duty_cycle = int(65535 - i/1000*65535)#fade blue from being on 0% of the time to 100%
            time.sleep(0.01)