import drawing as MyD
import leds as MyL
import buttons as MyB
import random
import time


######################## --- SKETCH SPECIFIC CODE
## Nothing in here should update variables outside of
## here directly.

## Squares move accross the screen. When they reach the
## edge program throws an out of bounds error and stop
current_mode = 0
lockout_flag = False
release_time = 0
lockout_duration = 10## HARD CODED min_refresh_rate
display_updates_enabled = True

def pauseDisplay():
    global display_updates_enabled
    display_updates_enabled = False

def resumeDisplay():
    global display_updates_enabled
    display_updates_enabled = True

def updateReady():
    return display_updates_enabled

def updateDisplay():
    MyD.updateDisplay()


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
        splash_screen()
        pauseDisplay()
        print("nothing to see?")




def hardware_loop():
    global current_mode, lockout_flag, release_time

    if (lockout_flag == True):
        if time.monotonic() > release_time:
            lockout_flag = False

    if (lockout_flag == False):
        if (MyB.buttons[0].value == 0):
            buttonPress(0)

        if (MyB.buttons[1].value == 0):
            buttonPress(1)

        if (MyB.buttons[2].value == 0):
            buttonPress(2)

        if (MyB.buttons[3].value == 0):
            buttonPress(3)


    if current_mode == 1:
        lockoutLEDIndicator(MyL.CYAN)
    elif current_mode == 2:
        lockoutLEDIndicator(MyL.MAGENTA)
    elif current_mode == 3:
        lockoutLEDIndicator(MyL.YELLOW)
    elif current_mode == 4:
        lockoutLEDIndicator(MyL.CHARTREUSE)
    elif current_mode == 0:
        #print("Off")
        MyL.all_off()

def buttonPress(button_index):
    global current_mode, lockout_flag, release_time
    current_mode = button_index + 1
    lockout_flag = True
    release_time = time.monotonic() + lockout_duration
    resumeDisplay()
    print("Mode ", current_mode)

def lockoutLEDIndicator(color):
    if (lockout_flag == True):
        MyL.all_on(color)
    else:
        MyL.all_off()

def image1():
    print("Image 1")
    square_location = 10
    square_size = 5
    limit_min_width = square_size
    limit_min_height = square_size
    limit_max_width = (MyD.canvas_width - square_size)
    limit_max_height = (MyD.canvas_height - square_size)

    MyD.refresh(0)

    for s in range(1, 100):
        MyD.setFill(3)
        size = random.randrange(1,square_size)
        x = random.randrange(limit_min_width, limit_max_width)
        y = random.randrange(limit_min_height, limit_max_height)
        MyD.square(x, y, size)

def image2():
    print("Image 2")
    h_spacing = 8
    h_line_count = int(MyD.canvas_height / h_spacing)
    v_spacing = 8
    v_line_count = int(MyD.canvas_width / v_spacing)

    #Refresh Screen
    MyD.refresh(3)

    MyD.setFill(1)
    for r in range(0, h_line_count):
        MyD.h_line(r*h_spacing, 0, MyD.canvas_width)

    for c in range(0, v_line_count):
        MyD.v_line(c*v_spacing, 0, MyD.canvas_height)


    for r in range(0, h_line_count):
        for c in range(0, v_line_count):
            if (r % 2):
                if (c % 2):
                    MyD.setFill(0)
                    MyD.h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing-1, MyD.canvas_width))
                    MyD.h_line(r*h_spacing, max(c*v_spacing+1, 0), min(c*v_spacing+2, MyD.canvas_width))
                    MyD.setFill(2)
                    MyD.v_line(c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing+2, MyD.canvas_height))

                else:
                    MyD.setFill(0)
                    MyD.v_line(c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing-1, MyD.canvas_height))
                    MyD.v_line(c*v_spacing, max(r*h_spacing+1, 0), min(r*h_spacing+2, MyD.canvas_height))
                    MyD.setFill(2)
                    MyD.h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing+2, MyD.canvas_width))
            else:
                if (c % 2):
                    MyD.setFill(0)
                    MyD.v_line(c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing-1, MyD.canvas_height))
                    MyD.v_line(c*v_spacing, max(r*h_spacing+1, 0), min(r*h_spacing+2, MyD.canvas_height))
                    MyD.setFill(2)
                    MyD.h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing+2, MyD.canvas_width))
                else:
                    MyD.setFill(0)
                    MyD.h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing-1, MyD.canvas_width))
                    MyD.h_line(r*h_spacing, max(c*v_spacing+1, 0), min(c*v_spacing+2, MyD.canvas_width))
                    MyD.setFill(2)
                    MyD.v_line(c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing+2, MyD.canvas_height))


def image3():
    print("Image 3")
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
    rect1_x = int((MyD.canvas_width - (rect1_width + rect0_width))/2) + int(overlap1/2)
    rect2_x = rect1_width + rect1_x - overlap2
    rect0_x = rect1_width + rect1_x - overlap1

    #Refresh Screen
    MyD.refresh(0)

    MyD.setFill(3)
    MyD.rect(rect0_x, rect0_y, rect0_width, rect0_height)

    MyD.setFill(2)
    MyD.rect(rect1_x, rect1_y, rect1_width, rect1_height)

    MyD.setFill(1)
    MyD.rect(rect2_x, rect2_y, rect2_width, rect2_height)


def image4():
    print("Image 4")
    baseline = 32
    bird_height = 20
    bird_offset = 10
    bird_width = 10
    #Refresh Screen
    MyD.refresh(3)

    MyD.setFill(1)
    MyD.rect(150, baseline+bird_offset, bird_width, bird_height)

    #setFill(1)
    MyD.rect(110, baseline+bird_offset, bird_width, bird_height)

    #setFill(2)
    MyD.rect(70, baseline+bird_offset, bird_width, bird_height)

    MyD.setFill(0)
    MyD.v_line(32, 0, MyD.canvas_height)
    MyD.v_line(32+4, 0, MyD.canvas_height)
    MyD.v_line(32-4, 0, MyD.canvas_height)
    MyD.h_line(baseline+4, 0, MyD.canvas_width)

def splash_screen():
    print("Splash Screen")
    ## testing sketch for primatives
    square_location = 10
    square_size = 20

    #Refresh Screen
    MyD.refresh(3)

    print(square_location)
    MyD.setFill(0)
    MyD.rect_old(150, 170, square_location, square_location+square_size)

    MyD.setFill(1)
    MyD.rect_old(110, 130, square_location, square_location+square_size)

    MyD.setFill(2)
    MyD.rect_old(70, 90, square_location, square_location+square_size)

    MyD.setFill(0)
    MyD.v_line(32, 0, MyD.canvas_height)
    MyD.h_line(32, 0, MyD.canvas_width)
