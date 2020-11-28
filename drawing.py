import epd

## --- DRAWING
# Better choice: https://github.com/ladyada/Adafruit_CircuitPython_Display_Shapes
# Calls require a RGB Color, wasn't clear on how that'd work for this
# v. 2.0 thing to check
backgroundFill = 3
currentFill = 0
canvas_height = 128#display.height ##HARDCODED!!
canvas_width = 296#display.width ##HARDCODED!!
display_updates_enabled = True

def updateDisplay():
    epd.updateDisplay()

def refresh():
    epd.wipeBitmap(backgroundFill)

def refresh(paletteIndex):
    epd.wipeBitmap(paletteIndex)

def setFill(paletteIndex):
    global currentFill
    currentFill = paletteIndex

def rect_old(x1, x2, y1, y2):
    global bitmap
    for x in range(x1, x2):
        for y in range(y1, y2):
            epd.updateBitmap(x,y,currentFill)

def rect(x, y, width, height):
    global bitmap
    i_max = int(x+width)
    j_min = int(y-height)
    for i in range(x, i_max):
        for j in range(j_min, y):
            epd.updateBitmap(i,j,currentFill)

def square(x, y, size):
    rect(x, y, size, size)

def v_line(x, y1, y2):
    global bitmap
    for y in range(y1, y2):
        epd.updateBitmap(x,y,currentFill)

def h_line(y, x1, x2):
    global bitmap
    for x in range(x1, x2):
        epd.updateBitmap(x,y,currentFill)
