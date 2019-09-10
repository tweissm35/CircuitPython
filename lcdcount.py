# Write your code here :-)
import board
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

btnstate = False
oldbtnstate = False
count = 0

lcd = LCD(I2CPCF8574Interface(0x3F), num_rows=2, num_cols=16)

switch = digitalio.DigitalInOut(board.D12)
switch.direction = digitalio.Direction.INPUT


btn = digitalio.DigitalInOut(board.D13)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP

print("Make it press!")
lcd.set_cursor_pos(0, 0)
lcd.print("Button presses:")
while True:
    lcd.set_cursor_pos(1, 0)
    lcd.print(str(count))
    btnstate = btn.value
    if not btn.value and (btnstate == (not oldbtnstate)):
        if switch.value:
            count += 1
        else:
            count -= 1
    oldbtnstate = btnstate
    lcd.print("          ")