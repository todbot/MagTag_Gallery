import board
import time
import displayio
from digitalio import DigitalInOut, Direction, Pull
import neopixel
import adafruit_il0373
import sketch

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

# Buttons and LEDs are now in their own files

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



######################## --- MORE TEMPLATE CODE
######## -- DO NOT LOOK AT THE CODE BEHIND THE CURTAIN

def update_io():
    sketch.hardware_loop()

def update_display():
    global display_loop_index, bitmap_has_update, last_refresh_time
    #print("update")
    sketch.display_loop()

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
