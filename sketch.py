import drawing
import leds
import buttons


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
