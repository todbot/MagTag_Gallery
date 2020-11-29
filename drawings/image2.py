import bitmap_tools as bt

def draw(bitmap):
    canvas_height = bt.canvas_height
    canvas_width = bt.canvas_width
    h_spacing = 8
    h_line_count = int(bt.canvas_height / h_spacing)
    v_spacing = 8
    v_line_count = int(bt.canvas_width / v_spacing)

    #Refresh Screen
    bitmap.fill(3)

    bt.setFill(1)
    for r in range(0, h_line_count):
        bt.h_line(bitmap, r*h_spacing, 0, canvas_width)

    for c in range(0, v_line_count):
        bt.v_line(bitmap, c*v_spacing, 0, canvas_height)


    for r in range(0, h_line_count):
        for c in range(0, v_line_count):
            if (r % 2):
                if (c % 2):
                    bt.setFill(0)
                    bt.h_line(bitmap,r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing-1, canvas_width))
                    bt.h_line(bitmap,r*h_spacing, max(c*v_spacing+1, 0), min(c*v_spacing+2, canvas_width))
                    bt.setFill(2)
                    bt.v_line(bitmap,c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing+2, canvas_height))

                else:
                    bt.setFill(0)
                    bt.v_line(bitmap,c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing-1, canvas_height))
                    bt.v_line(bitmap,c*v_spacing, max(r*h_spacing+1, 0), min(r*h_spacing+2, canvas_height))
                    bt.setFill(2)
                    bt.h_line(bitmap,r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing+2, canvas_width))
            else:
                if (c % 2):
                    bt.setFill(0)
                    bt.v_line(bitmap,c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing-1, canvas_height))
                    bt.v_line(bitmap,c*v_spacing, max(r*h_spacing+1, 0), min(r*h_spacing+2, canvas_height))
                    bt.setFill(2)
                    bt.h_line(bitmap,r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing+2, canvas_width))
                else:
                    bt.setFill(0)
                    bt.h_line(bitmap,r*h_spacing, max(c*v_spacing-2, 0), min(c*v_spacing-1, canvas_width))
                    bt.h_line(bitmap,r*h_spacing, max(c*v_spacing+1, 0), min(c*v_spacing+2, canvas_width))
                    bt.setFill(2)
                    bt.v_line(bitmap,c*v_spacing, max(r*h_spacing-2, 0), min(r*h_spacing+2, canvas_height))

