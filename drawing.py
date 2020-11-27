import epd

## --- DRAWING
# Better choice: https://github.com/ladyada/Adafruit_CircuitPython_Display_Shapes
# Calls require a RGB Color, wasn't clear on how that'd work for this
# v. 2.0 thing to check
backgroundFill = 3
currentFill = 0
canvas_height = 128#display.height
canvas_width = 296#display.width

def refresh():
    epd.bitmap.fill(backgroundFill)

def setFill(paletteIndex):
    global currentFill
    currentFill = paletteIndex

def rect(x1, x2, y1, y2):
    global bitmap
    for x in range(x1, x2):
        for y in range(y1, y2):
            epd.bitmap[x, y] = currentFill

def v_line(x, y1, y2):
    global bitmap
    for y in range(y1, y2):
        epd.bitmap[x, y] = currentFill

def h_line(y, x1, x2):
    global bitmap
    for x in range(x1, x2):
            epd.bitmap[x, y] = currentFill
