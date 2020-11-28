import board
import time
import displayio
import random
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
neopixels = neopixel.NeoPixel(board.NEOPIXEL, 4, brightness=0.1)
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
display_updates_enabled = True

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

def pauseDisplay():
    global display_updates_enabled
    display_updates_enabled = False

def resumeDisplay():
    global display_updates_enabled
    display_updates_enabled = True

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

def rect_old(x1, x2, y1, y2):
    global bitmap
    for x in range(x1, x2):
        for y in range(y1, y2):
            bitmap[x, y] = currentFill

def rect(x, y, width, height):
    global bitmap
    i_max = int(x+width)
    j_min = int(y-height)
    for i in range(x, i_max):
        for j in range(j_min, y):
            bitmap[i, j] = currentFill

def square(x, y, size):
    rect(x, y, size, size)

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

CHARTREUSE = 0x448811

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
## edge program throws an out of bounds error and stop
current_mode = 0
lockout_flag = False
release_time = 0
lockout_duration = min_refresh_rate

def setup():
    print("SetUp")
    #Noting to see here yet

def display_loop():
    if current_mode == 1:
        image1()
        pauseDisplay()
    elif current_mode == 2:
        image2()
        pauseDisplay()
    elif current_mode == 3:
        image3()
        pauseDisplay()
    elif current_mode == 4:
        image4()
        pauseDisplay()
    elif current_mode == 0:
        default_image()
        pauseDisplay()
        print("nothing to see?")




def hardware_loop():
    global current_mode, lockout_flag, release_time

    if (lockout_flag == True):
        if time.monotonic() > release_time:
            lockout_flag = False

    if (lockout_flag == False):
        if (buttons[0].value == 0):
            buttonPress(0)

        if (buttons[1].value == 0):
            buttonPress(1)

        if (buttons[2].value == 0):
            buttonPress(2)

        if (buttons[3].value == 0):
            buttonPress(3)


    if current_mode == 1:
        lockoutLEDIndicator(CYAN)
    elif current_mode == 2:
        lockoutLEDIndicator(MAGENTA)
    elif current_mode == 3:
        lockoutLEDIndicator(YELLOW)
    elif current_mode == 4:
        lockoutLEDIndicator(CHARTREUSE)
    elif current_mode == 0:
        #print("Off")
        all_off()

def buttonPress(button_index):
    global current_mode, lockout_flag, release_time
    current_mode = button_index + 1
    lockout_flag = True
    release_time = time.monotonic() + lockout_duration
    resumeDisplay()
    print("Mode ", current_mode)

def lockoutLEDIndicator(color):
    if (lockout_flag == True):
        all_on(color)
    else:
        all_off()

def image1():
    square_location = 10
    square_size = 5
    limit_min_width = square_size
    limit_min_height = square_size
    limit_max_width = (canvas_width - square_size)
    limit_max_height = (canvas_height - square_size)

    bitmap.fill(0)

    for s in range(1, 100):
        setFill(3)
        size = random.randrange(1,square_size)
        x = random.randrange(limit_min_width, limit_max_width)
        y = random.randrange(limit_min_height, limit_max_height)
        square(x, y, size)

def image2():
    h_spacing = 8
    h_line_count = int(canvas_height / h_spacing)
    v_spacing = 8
    v_line_count = int(canvas_width / v_spacing)

    #Refresh Screen
    bitmap.fill(3)

    setFill(1)
    for r in range(0, h_line_count):
        h_line(r*h_spacing, 0, canvas_width)

    for c in range(0, v_line_count):
        v_line(c*v_spacing, 0, canvas_height)


    for r in range(0, h_line_count):
        for c in range(0, v_line_count):
            if (r % 2):
                if (c % 2):
                    setFill(0)
                    h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing-1, canvas_width))
                    h_line(r*h_spacing, max(c*v_spacing+1, 0), min(c*v_spacing+2, canvas_width))
                    setFill(2)
                    v_line(c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing+2, canvas_height))

                else:
                    setFill(0)
                    v_line(c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing-1, canvas_height))
                    v_line(c*v_spacing, max(r*h_spacing+1, 0), min(r*h_spacing+2, canvas_height))
                    setFill(2)
                    h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing+2, canvas_width))
            else:
                if (c % 2):
                    setFill(0)
                    v_line(c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing-1, canvas_height))
                    v_line(c*v_spacing, max(r*h_spacing+1, 0), min(r*h_spacing+2, canvas_height))
                    setFill(2)
                    h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing+2, canvas_width))
                else:
                    setFill(0)
                    h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing-1, canvas_width))
                    h_line(r*h_spacing, max(c*v_spacing+1, 0), min(c*v_spacing+2, canvas_width))
                    setFill(2)
                    v_line(c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing+2, canvas_height))


def image3():
    baseline = 125

    rect1_width = 95
    rect1_height = 95
    rect1_y = baseline

    rect0_width = 110
    rect0_height = 110
    rect0_y = baseline

    rect2_width = 30
    rect2_height = 30
    rect2_y = baseline - int(rect1_height * 0.6) + int(rect2_height * 0.7)

    overlap1 = 10
    overlap2 = int(rect2_width/2)
    rect1_x = int((canvas_width - (rect1_width + rect0_width))/2) + int(overlap1/2)
    rect2_x = rect1_width + rect1_x - overlap2
    rect0_x = rect1_width + rect1_x - overlap1

    #Refresh Screen
    bitmap.fill(0)

    setFill(3)
    rect(rect0_x, rect0_y, rect0_width, rect0_height)

    setFill(2)
    rect(rect1_x, rect1_y, rect1_width, rect1_height)

    setFill(1)
    rect(rect2_x, rect2_y, rect2_width, rect2_height)


def image4():
    baseline = 32
    bird_height = 20
    bird_offset = 10
    bird_width = 10
    #Refresh Screen
    bitmap.fill(backgroundFill)

    setFill(1)
    rect(150, baseline+bird_offset, bird_width, bird_height)

    #setFill(1)
    rect(110, baseline+bird_offset, bird_width, bird_height)

    #setFill(2)
    rect(70, baseline+bird_offset, bird_width, bird_height)

    setFill(0)
    v_line(32, 0, canvas_height)
    v_line(32+4, 0, canvas_height)
    v_line(32-4, 0, canvas_height)
    h_line(baseline+4, 0, canvas_width)

def default_image():
    ## testing sketch for primatives
    square_location = 10
    square_size = 20

    #Refresh Screen
    bitmap.fill(backgroundFill)

    print(square_location)
    setFill(0)
    rect_old(150, 170, square_location, square_location+square_size)

    setFill(1)
    rect_old(110, 130, square_location, square_location+square_size)

    setFill(2)
    rect_old(70, 90, square_location, square_location+square_size)

    setFill(0)
    v_line(32, 0, canvas_height)
    h_line(32, 0, canvas_width)



######################## --- MORE TEMPLATE CODE
######## -- DO NOT LOOK AT THE CODE BEHIND THE CURTAIN

def update_io():
    hardware_loop()

def update_display():
    global display_loop_index, bitmap_has_update, last_refresh_time, display_updates_enabled
    #print("update")

    #print("updates enabled?: ", display_updates_enabled)
    if (display_updates_enabled == True):
        current_time = time.monotonic()
        if (current_time - last_refresh_time) > min_refresh_rate:
            display_loop()
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
