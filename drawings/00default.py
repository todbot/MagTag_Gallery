import bitmap_tools as bt

def draw(bitmap):
    ## testing sketch for primatives
    square_location = 10
    square_size = 20

    # Refresh Screen
    bitmap.fill(bt.backgroundFill)

    # print(square_location)
    bt.setFill(0)
    bt.rect_old(bitmap, 150, 170, square_location, square_location+square_size)

    bt.setFill(1)
    bt.rect_old(bitmap, 110, 130, square_location, square_location+square_size)

    bt.setFill(2)
    bt.rect_old(bitmap, 70, 90, square_location, square_location+square_size)

    bt.setFill(0)
    bt.v_line(bitmap, 32, 0, bt.canvas_height)
    bt.h_line(bitmap, 32, 0, bt.canvas_width)

