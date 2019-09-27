# Write your code here :-)
import board #pylint: disable-msg=import-error
import neopixel #pylint: disable-msg=import-error
import time
import pulseio #pylint: disable-msg=import-error
import touchio #pylint: disable-msg=import-error
from adafruit_motor import servo #pylint: disable-msg=import-error

angle = 90

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
#led = pulseio.PWMOut(board.D12, frequency=5000, duty_cycle=65535)#PWM output
pwm = pulseio.PWMOut(board.D13, frequency=50, duty_cycle=0)

servo = servo.Servo(pwm, min_pulse=500, max_pulse=2400)

touch_a = touchio.TouchIn(board.A0)
touch_b = touchio.TouchIn(board.A5)

print("Make it blue!")

while True:
    dot.fill((0,0,255))#turns the board's led on
    '''for i in range(100):#i increments from 0 to 100
        led.duty_cycle = int(i / 100 * 65535)#sets duty cycle to a percentage of range
        time.sleep(0.01)#pauses for a little bit
    for i in range(100, -1, -1):#i increments from 100 by -1 until it reaches -1
        led.duty_cycle = int(i / 100 * 65535)
        time.sleep(0.01)'''
    '''for i in range(180):
        servo.angle = i
        time.sleep(0.02)
    for i in range(180):
        servo.angle = 180 - i
        time.sleep(0.02)'''
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