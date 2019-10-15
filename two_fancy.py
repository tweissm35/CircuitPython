from fancyLED import fancyLED#from file fancyLED import class fancyLED
import board #pylint: disable-msg=import-error
import time#↑↑↑this changes and import error into a warning

f1 = board.D13
f2 = board.D12
f3 = board.D11

b1 = board.D10
b2 = board.D9
b3 = board.D8

fancy1 = fancyLED(f1,f2,f3)#creating an object with the above pins
fancy2 = fancyLED(b1,b2,b3)

while True:#loop forever
    fancy1.alternate()#call function "alternate"
    fancy2.blink()
    fancy1.chase()
    fancy2.sparkle()