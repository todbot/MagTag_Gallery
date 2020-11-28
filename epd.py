import board
import displayio
import adafruit_il0373

min_refresh_rate = 10

displayio.release_displays()
display_bus = displayio.FourWire(
    board.SPI(),
    command=board.EPD_DC,
    chip_select=board.EPD_CS,
    reset=board.EPD_RESET,
    baudrate=1000000,
)

display = adafruit_il0373.IL0373(display_bus,width=296,height=128,rotation=270,black_bits_inverted=False,color_bits_inverted=False,grayscale=True,refresh_time=1,seconds_per_frame=5,)


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


def updateDisplay():
    print("update called")
    # Create a TileGrid using the Bitmap and Palette
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
    # Create a Group
    group = displayio.Group()
    # Add the TileGrid to the Group
    group.append(tile_grid)
    display.show(group)
    display.refresh()

def updateBitmap(x,y,color):
    bitmap[x, y] = color

def wipeBitmap(color):
    bitmap.fill(color)

