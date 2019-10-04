import board#pylint: disable-msg=import-error
import digitalio#pylint: disable-msg=import-error
from lcd.lcd import LCD#pylint: disable-msg=import-error
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface#pylint: disable-msg=import-error

btnstate = False#used to see if button is pressed
oldbtnstate = False#used to see if button used to pressed(so it only increments once per press)
count = 0

lcd = LCD(I2CPCF8574Interface(0x3F), num_rows=2, num_cols=16)#creates an LCD object called "lcd" at adress 0x3F with 2 rows and 16 collumns

switch = digitalio.DigitalInOut(board.D12)#create a digitalio object called switch
switch.direction = digitalio.Direction.INPUT#set it to input


btn = digitalio.DigitalInOut(board.D13)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP#lets the button use a pull up resistor which means it will read HIGH when not being pressed

lcd.set_cursor_pos(0, 0)#moves the cursor to row 0 collumn 0
lcd.print("Button presses:")
while True:
    lcd.set_cursor_pos(1, 0)
    lcd.print(str(count))#turn integer count into a string, so it can be printed
    btnstate = btn.value
    if not btn.value and (btnstate == (not oldbtnstate)):#if button is pressed and it didn't used to be
        if switch.value:#determines if it counts up or down
            count += 1#set count equal to count + 1
        else:
            count -= 1
    oldbtnstate = btnstate
    lcd.print("          ")#clears screen