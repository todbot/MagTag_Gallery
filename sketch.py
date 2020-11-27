import drawing
import leds
import buttons


######################## --- SKETCH SPECIFIC CODE
## Nothing in here should update variables outside of
## here directly.

## Squares move accross the screen. When they reach the
## edge program throws an out of bounds error and stops

square_location = 10
last_square_location = 0
square_size = 20

def setup():
    print("SetUp")
    #Noting to see here yet

def display_loop(loop_index):
    global square_location, last_square_location
    square_location = ((loop_index % 8) * 12) + 10


    if (square_location != last_square_location):
        #Refresh Screen
        drawing.refresh()

        print(square_location)
        drawing.setFill(0)
        drawing.rect(150, 170, square_location, square_location+square_size)

        drawing.setFill(1)
        drawing.rect(110, 130, square_location, square_location+square_size)

        drawing.setFill(2)
        drawing.rect(70, 90, square_location, square_location+square_size)

        drawing.setFill(0)
        drawing.v_line(32, 0, drawing.canvas_height)
        drawing.h_line(32, 0, drawing.canvas_width)

        last_square_location = square_location

def hardware_loop():
    if (buttons.buttons[0].value == 0):
        print("Pressed")
        leds.all_on(leds.CYAN)
    else:
        leds.all_off()
