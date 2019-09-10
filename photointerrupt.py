import time
import board
import digitalio


btn = digitalio.DigitalInOut(board.D1)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP

count = 0

seconds = time.time()
oldSeconds = time.time()

state = False

oldState = False

while True:
    seconds = time.time()
    state = btn.value
    if (seconds-oldSeconds) == 4:
        print("The total number of interruptions is "+str(count))
        oldSeconds = time.time()
    if state and (state == (not oldState)):
        count+=1
    oldState = state