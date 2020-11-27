import board
import time
import displayio
import adafruit_il0373
import sketch
import epd

last_refresh_time = 0
display_loop_index = 1 #How often has been the display been updated


def update_io():
    sketch.hardware_loop()

def update_display():
    global last_refresh_time, display_loop_index
    sketch.display_loop(display_loop_index)

    current_time = time.monotonic()
    delta = current_time - last_refresh_time
    if epd.refreshCheck(delta):
        print(current_time,"---- epaper refresh loop! ---- ", display_loop_index)
        #epd.updateDisplay()

        epd.display.show(epd.group)

        # Refresh the screen
        last_refresh_time = current_time
        display_loop_index = display_loop_index + 1

        epd.display.refresh()



sketch.setup()
while True:
    update_io()
    update_display()
