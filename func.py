import print
import barricade

def func():

    import scan
    import checkspace

    scan.scan()
    
    empty_image = 'images/test.jpg'
    current_image = 'images/target.jpg'

    coordinates = [[119, 101, 270, 90, 261, 172, 100, 179],
[417, 85, 423, 168, 587, 167, 568, 82],
[89, 214, 257, 208, 250, 286, 66, 290],
[427, 202, 592, 195, 612, 276, 435, 282],
[56, 335, 249, 330, 238, 437, 28, 438],
[437, 322, 621, 310, 635, 405, 444, 422]]

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
        print.print(random.choice(available))
        barricade.barricade()
    else:
        print.print(0)
        print("No space.")
