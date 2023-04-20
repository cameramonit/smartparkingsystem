import printi2c
import barricade

def func():

    import scan
    import checkspace

    scan.scan()
    
    empty_image = 'images/test.jpg'
    current_image = 'images/target.jpg'

    coordinates = [[505, 166, 315, 78, 271, 133, 473, 231],
[473, 232, 274, 136, 198, 232, 421, 343],
[421, 343, 199, 234, 127, 331, 368, 459],]

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
