import bitmap_tools as bt

def draw(bitmap):
    baseline = 32
    bird_height = 20
    bird_offset = 10
    bird_width = 10
    #Refresh Screen
    bitmap.fill(bt.backgroundFill)

    bt.setFill(1)
    bt.rect(bitmap, 150, baseline+bird_offset, bird_width, bird_height)

    #setFill(1)
    bt.rect(bitmap,110, baseline+bird_offset, bird_width, bird_height)

    #setFill(2)
    bt.rect(bitmap,70, baseline+bird_offset, bird_width, bird_height)

    bt.setFill(0)
    bt.v_line(bitmap,32, 0, canvas_height)
    bt.v_line(bitmap,32+4, 0, canvas_height)
    bt.v_line(bitmap,32-4, 0, canvas_height)
    bt.h_line(bitmap,baseline+4, 0, canvas_width)

