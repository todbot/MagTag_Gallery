import board
import time
from adafruit_magtag.magtag import MagTag

import bitmap_tools

from drawings import drawings

magtag = MagTag()  #(debug=True)

display = magtag.display

bitmap = bitmap_tools.setupBitmap(display)

drawings[0].draw(bitmap)

display.refresh()

i=1
while True:
    print('hi',i)
    time.sleep(10)
    drawings[i].draw(bitmap)
    display.refresh()
    i = (i+1) % len(drawings)

    
