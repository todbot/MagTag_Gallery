import board
import time
import displayio
from digitalio import DigitalInOut, Direction, Pull
import neopixel
import adafruit_il0373

######################## --- TEMPLATE CODE

#----------------------------- MagTag Hardware Set Up
# Reccomendation to use the MagTag Library, not this
# I just wanted to learn
# https://github.com/adafruit/Adafruit_CircuitPython_MagTag/blob/main/adafruit_magtag/

#DISPLAY

displayio.release_displays()
display_bus = displayio.FourWire(
    board.SPI(),
    command=board.EPD_DC,
    chip_select=board.EPD_CS,
    reset=board.EPD_RESET,
    baudrate=1000000,
)

display = adafruit_il0373.IL0373(display_bus,width=296,height=128,rotation=270,black_bits_inverted=False,color_bits_inverted=False,grayscale=True,refresh_time=1,seconds_per_frame=5,)

#BUTTONS
#The buttons are on D11, D12, D14 and D15
buttons = []
for pin in (board.BUTTON_A, board.BUTTON_B, board.BUTTON_C, board.BUTTON_D):
    switch = DigitalInOut(pin)
    switch.direction = Direction.INPUT
    switch.pull = Pull.UP
    buttons.append(switch)

#NEOPIXELS
neopixels = neopixel.NeoPixel(board.NEOPIXEL, 4, brightness=0.3)
_neopixel_disable = DigitalInOut(board.NEOPIXEL_POWER)
_neopixel_disable.direction = Direction.OUTPUT
_neopixel_disable.value = False #keep them off by default

#----------------------------- End MagTag Setup

#----------------------------- Environment Variables
#-- EPaper Handling
last_refresh_time = 0
min_refresh_rate = 10
display_loop_index = 1 #How often has been the display been updated
bitmap_has_update = True #Should the display be updating

# Create a bitmap with two colors
# 4 colors are (0,0,0), (82,82,82), (163,163,163), (255,255,255)
#number_of_colors = 2

bitmap = displayio.Bitmap(display.width, display.height, 4)

# Create a two color palette
palette = displayio.Palette(4)
# palette[0] = 0x000000
# palette[1] = 0x666666
# palette[2] = 0x999999
# palette[3] = 0xFFFFFF

palette[0] = 0x000000
palette[1] = 0x525252
palette[2] = 0xA3A3A3
palette[3] = 0xFFFFFF


# Create a TileGrid using the Bitmap and Palette
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
# Create a Group
group = displayio.Group()
# Add the TileGrid to the Group
group.append(tile_grid)

## -- End Epaper Handing

## --- DRAWING
# Better choice: https://github.com/ladyada/Adafruit_CircuitPython_Display_Shapes
# Calls require a RGB Color, wasn't clear on how that'd work for this
# v. 2.0 thing to check
backgroundFill = 3
currentFill = 0
canvas_height = display.height
canvas_width = display.width

def setFill(paletteIndex):
    global currentFill
    currentFill = paletteIndex

def rect(x1, x2, y1, y2):
    global bitmap
    for x in range(x1, x2):
        for y in range(y1, y2):
            bitmap[x, y] = currentFill

def v_line(x, y1, y2):
    global bitmap
    for y in range(y1, y2):
        bitmap[x, y] = currentFill

def h_line(y, x1, x2):
    global bitmap
    for x in range(x1, x2):
            bitmap[x, y] = currentFill


## --- NEOPIXEL HANDLING
# Thank you for the colors JP!
RED = 0x880000
GREEN = 0x008800
BLUE = 0x000088
YELLOW = 0x884400
CYAN = 0x0088BB
MAGENTA = 0x9900BB
WHITE = 0x888888

def all_on(color):
    global _neopixel_disable
    if _neopixel_disable:
        _neopixel_disable = False
    neopixels.fill(color)

def all_off():
    global _neopixel_disable
    neopixels.fill(0)
    _neopixel_disable = True
##

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

def display_loop():
    global square_location, last_square_location

    square_location = ((display_loop_index % 8) * 12) + 10


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




def hardware_loop():
    if (buttons[0].value == 0):
        print("Pressed")
        all_on(CYAN)
    else:
        all_off()

######################## --- MORE TEMPLATE CODE
######## -- DO NOT LOOK AT THE CODE BEHIND THE CURTAIN

def update_io():
    hardware_loop()

def update_display():
    global display_loop_index, bitmap_has_update, last_refresh_time
    #print("update")
    display_loop()

    current_time = time.monotonic()
    if (current_time - last_refresh_time) > min_refresh_rate:
        print(current_time,"---- epaper refresh loop! ---- ", display_loop_index)
        display.show(group)
        # Refresh the screen
        last_refresh_time = current_time
        display_loop_index = display_loop_index + 1

        display.refresh()



setup()
while True:
    update_io()
    update_display()
