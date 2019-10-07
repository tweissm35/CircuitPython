import time
import board#pylint: disable-msg=import-error
import digitalio#pylint: disable-msg=import-error


btn = digitalio.DigitalInOut(board.D1)#
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP

count = 0

seconds = time.time()#seconds since 1970
oldSeconds = time.time()

state = False

oldState = False

while True:
    seconds = time.time()#updated seconds
    state = btn.value#check if the photo interrupter is blocked
    if (seconds-oldSeconds) == 4:#if seconds and oldseconds are different by 4 seconds it must mean 4 seconds have passed
        print("The total number of interruptions is "+str(count))
        oldSeconds = time.time()#set oldseconds equal to seconds, effectively reseting this if statement
    if state and (state == (not oldState)):#works as a toggle "if photointerrupter blocked and it didn't used to be"
        count+=1#increase count by 1
    oldState = state#update what oldstate is so it knows what used to be going on