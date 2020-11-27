import board
from digitalio import DigitalInOut, Direction, Pull
#BUTTONS
#The buttons are on D11, D12, D14 and D15
buttons = []
for pin in (board.BUTTON_A, board.BUTTON_B, board.BUTTON_C, board.BUTTON_D):
    switch = DigitalInOut(pin)
    switch.direction = Direction.INPUT
    switch.pull = Pull.UP
    buttons.append(switch)
