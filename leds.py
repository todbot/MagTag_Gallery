#NEOPIXELS
neopixels = neopixel.NeoPixel(board.NEOPIXEL, 4, brightness=0.3)
_neopixel_disable = DigitalInOut(board.NEOPIXEL_POWER)
_neopixel_disable.direction = Direction.OUTPUT
_neopixel_disable.value = False #keep them off by default

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
