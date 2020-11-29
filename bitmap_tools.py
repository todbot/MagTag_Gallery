
import displayio

## --- DRAWING
# Better choice: https://github.com/ladyada/Adafruit_CircuitPython_Display_Shapes
# Calls require a RGB Color, wasn't clear on how that'd work for this
# v. 2.0 thing to check
backgroundFill = 3
currentFill = 0
canvas_height = 0
canvas_width = 0

def setupBitmap(display):
    global canvas_height, canvas_width, bitmap, palette
    canvas_height = display.height
    canvas_width = display.width
    # Create a bitmap with two colors
    # 4 colors are (0,0,0), (82,82,82), (163,163,163), (255,255,255)

    bitmap = displayio.Bitmap(display.width, display.height, 4)

    # Create a two color palette
    palette = displayio.Palette(4)

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
    # Attach group to display, we're not changing groups so we're done,
    # so just edit bitmap and refresh display
    display.show(group)

    return bitmap
    
def setFill(paletteIndex):
    global currentFill
    currentFill = paletteIndex

def rect_old(bitmap, x1, x2, y1, y2):
    for x in range(x1, x2):
        for y in range(y1, y2):
            bitmap[x, y] = currentFill

def rect(bitmap, x, y, width, height):
    i_max = int(x+width)
    j_min = int(y-height)
    for i in range(x, i_max):
        for j in range(j_min, y):
            bitmap[i, j] = currentFill

def square(bitmap, x, y, size):
    rect(bitmap, x, y, size, size)

def v_line(bitmap, x, y1, y2):
    for y in range(y1, y2):
        bitmap[x, y] = currentFill

def h_line(bitmap, y, x1, x2):
    for x in range(x1, x2):
            bitmap[x, y] = currentFill
