import printi2c
import barricade

def func():

    import scan
    import checkspace

    scan.scan()
    
    empty_image = 'images/test.jpg'
    current_image = 'images/target.jpg'

    coordinates = [[264, 40, 116, 42, 92, 121, 253, 123],
[557, 48, 416, 45, 418, 124, 574, 130],
[252, 157, 80, 154, 58, 233, 240, 232],
[584, 161, 420, 158, 424, 233, 599, 235],
[239, 273, 47, 274, 18, 370, 222, 375],
[435, 361, 615, 355, 600, 281, 438, 286]]

    coordinates_flag = [0,0,0,0,0,0]
    available = []

    for index, item in enumerate(coordinates):

        empty = checkspace.avg_dark_pixels(empty_image, item)
        current = checkspace.avg_dark_pixels(current_image, item)

        if abs(current - empty) < 10:
            coordinates_flag[index] = 0     # if empty
            available.append(index+1)
        else:
            coordinates_flag[index] = 1     # if occupied

    import random

    if(len(available)>0):
        # print("Park at slot: ", random.choice(available))
        printi2c.printi2c(random.choice(available))
        barricade.barricade()
    else:
        printi2c.printi2c(0)
        # print("No space.")
