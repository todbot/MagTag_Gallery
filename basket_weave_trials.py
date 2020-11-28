## This code not used in program, but a record of test "weave" patterns

# Started here. Had to be grey on grey otherwise too prison-like
def grid():
    h_spacing = 8
    h_line_count = int(canvas_height / h_spacing)
    v_spacing = 8
    v_line_count = int(canvas_width / v_spacing)

    #Refresh Screen
    bitmap.fill(2)

    setFill(1)
    for r in range(0, h_line_count):
        h_line(r*h_spacing, 0, canvas_width)

    for c in range(0, v_line_count):
        v_line(c*v_spacing, 0, canvas_height)

#Add horizontal low-lights go over thread, but hightlights too
def basket_weave_1():
    h_spacing = 8
    h_line_count = int(canvas_height / h_spacing)
    v_spacing = 8
    v_line_count = int(canvas_width / v_spacing)

    #Refresh Screen
    bitmap.fill(2)

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
                    h_line(r*h_spacing, max(c*v_spacing-1, 0), min(c*v_spacing+1, canvas_width))
                else:
                    setFill(3)
                    h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing+2, canvas_width))
            else:
                if (c % 2):
                    setFill(3)
                    h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing+2, canvas_width))
                else:
                    setFill(0)
                    h_line(r*h_spacing, max(c*v_spacing-1, 0), min(c*v_spacing+1, canvas_width))

# Horizontal low lights with gap and horizontal highlights
def basket_weave_2():
    h_spacing = 8
    h_line_count = int(canvas_height / h_spacing)
    v_spacing = 8
    v_line_count = int(canvas_width / v_spacing)

    #Refresh Screen
    bitmap.fill(2)

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
                else:
                    setFill(3)
                    h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing+2, canvas_width))
            else:
                if (c % 2):
                    setFill(3)
                    h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing+2, canvas_width))
                else:
                    setFill(0)
                    h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing-1, canvas_width))
                    h_line(r*h_spacing, max(c*v_spacing+1, 0), min(c*v_spacing+2, canvas_width))

#Just gappy horizontal low-lights
def basket_weave_3():
    h_spacing = 8
    h_line_count = int(canvas_height / h_spacing)
    v_spacing = 8
    v_line_count = int(canvas_width / v_spacing)

    #Refresh Screen
    bitmap.fill(2)

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
            else:
                if (c % 2) == False:
                    setFill(0)
                    h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing-1, canvas_width))
                    h_line(r*h_spacing, max(c*v_spacing+1, 0), min(c*v_spacing+2, canvas_width))

#Nice, subtle runner up, hase both H and V lowlights
def basket_weave_4():
    h_spacing = 8
    h_line_count = int(canvas_height / h_spacing)
    v_spacing = 8
    v_line_count = int(canvas_width / v_spacing)

    #Refresh Screen
    bitmap.fill(2)

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

                else:
                    setFill(0)
                    v_line(c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing-1, canvas_height))
                    v_line(c*v_spacing, max(r*h_spacing+1, 0), min(r*h_spacing+2, canvas_height))
            else:
                if (c % 2):
                    setFill(0)
                    v_line(c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing-1, canvas_height))
                    v_line(c*v_spacing, max(r*h_spacing+1, 0), min(r*h_spacing+2, canvas_height))
                else:
                    setFill(0)
                    h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing-1, canvas_width))
                    h_line(r*h_spacing, max(c*v_spacing+1, 0), min(c*v_spacing+2, canvas_width))

## Too Fussy, H and V highlights and lowlights
## on grey background, white is highlight color
def basket_weave_5():
    h_spacing = 8
    h_line_count = int(canvas_height / h_spacing)
    v_spacing = 8
    v_line_count = int(canvas_width / v_spacing)

    #Refresh Screen
    bitmap.fill(2)

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
                    setFill(3)
                    v_line(c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing+2, canvas_height))

                else:
                    setFill(0)
                    v_line(c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing-1, canvas_height))
                    v_line(c*v_spacing, max(r*h_spacing+1, 0), min(r*h_spacing+2, canvas_height))
                    setFill(3)
                    h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing+2, canvas_width))
            else:
                if (c % 2):
                    setFill(0)
                    v_line(c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing-1, canvas_height))
                    v_line(c*v_spacing, max(r*h_spacing+1, 0), min(r*h_spacing+2, canvas_height))
                    setFill(3)
                    h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing+2, canvas_width))
                else:
                    setFill(0)
                    h_line(r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing-1, canvas_width))
                    h_line(r*h_spacing, max(c*v_spacing+1, 0), min(c*v_spacing+2, canvas_width))
                    setFill(3)
                    v_line(c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing+2, canvas_height))

#Winner Winner Tofurkey Dinner - H and V highlights and lowlights
## on white background, lighter grey is highlight color
def basket_weave_5():
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
