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
