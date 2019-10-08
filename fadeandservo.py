# Write your code here :-)
import board #pylint: disable-msg=import-error
import time
import touchio #pylint: disable-msg=import-error
from adafruit_motor import servo #pylint: disable-msg=import-error
import pulseio #pylint: disable-msg=import-error

angle = 90

pwm = pulseio.PWMOut(board.D13, frequency=50, duty_cycle=0)
servo = servo.Servo(pwm, min_pulse=500, max_pulse=2400)

touch_a = touchio.TouchIn(board.A0)
touch_b = touchio.TouchIn(board.A5)

while True:
    if touch_a.value:#tests for A0 being touched
        if(angle<177):#the number is this because bad things happen when angle goes above 180 or below 0
            print("a touched")
            angle+=3#increments angle by 3
    if touch_b.value:#tests for A5 being touched
        if(angle>2):
            print("b touched")
            angle-=3#increments angle by -3
    servo.angle = angle#sets the servo to angle
    time.sleep(0.01)#waits a little bit for the servo to catch up