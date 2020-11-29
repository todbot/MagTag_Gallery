import bitmap_tools as bt

def draw(bitmap):
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
    rect1_x = int((bt.canvas_width - (rect1_width + rect0_width))/2) + int(overlap1/2)
    rect2_x = rect1_width + rect1_x - overlap2
    rect0_x = rect1_width + rect1_x - overlap1

    #Refresh Screen
    bitmap.fill(0)

    bt.setFill(3)
    bt.rect(bitmap, rect0_x, rect0_y, rect0_width, rect0_height)

    bt.setFill(2)
    bt.rect(bitmap, rect1_x, rect1_y, rect1_width, rect1_height)

    bt.setFill(1)
    bt.rect(bitmap, rect2_x, rect2_y, rect2_width, rect2_height)

