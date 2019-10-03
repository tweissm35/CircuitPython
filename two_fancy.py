from fancyLED import fancyLED
import board #pylint: disable-msg=import-error
import time
f1 = board.D13
f2 = board.D12
f3 = board.D11

b1 = board.D10
b2 = board.D9
b3 = board.D8

fancy1 = fancyLED(f1,f2,f3)
fancy2 = fancyLED(b1,b2,b3)

#while True:
fancy1.alternate()
fancy2.alternate()
time.sleep(1)
fancy1.off()
fancy2.off()
time.sleep(1)
fancy1.blink()
fancy2.blink()
time.sleep(1)
fancy1.off()
fancy2.off()
time.sleep(1)
fancy1.chase()
fancy2.chase()
#fancy2.sparkle()