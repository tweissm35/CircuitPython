import board #pylint: disable-msg=import-error
import time
import pulseio #pylint: disable-msg=import-error

led = pulseio.PWMOut(board.D12, frequency=5000, duty_cycle=65535)#PWM output
while True:
    for i in range(100):#i increments from 0 to 100
        led.duty_cycle = int(i / 100 * 65535)#sets duty cycle to a percentage of range
        time.sleep(0.01)#pauses for a little bit
    for i in range(100, -1, -1):#i increments from 100 by -1 until it reaches -1
        led.duty_cycle = int(i / 100 * 65535)
        time.sleep(0.01)
