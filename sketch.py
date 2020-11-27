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
loop_index = 0

def setup():
    print("SetUp")
    #Noting to see here yet

def display_loop():
    global square_location, last_square_location, loop index

    square_location = ((loop_index % 8) * 12) + 10


    if (square_location != last_square_location):
        #Refresh Screen
        bitmap.fill(backgroundFill)

        print(square_location)
        setFill(0)
        rect(150, 170, square_location, square_location+square_size)

        setFill(1)
        rect(110, 130, square_location, square_location+square_size)

        setFill(2)
        rect(70, 90, square_location, square_location+square_size)

        setFill(0)
        v_line(32, 0, canvas_height)
        h_line(32, 0, canvas_width)

        last_square_location = square_location
        loop_index = loop_index + 1

def hardware_loop():
    if (buttons[0].value == 0):
        print("Pressed")
        all_on(CYAN)
    else:
        all_off()
