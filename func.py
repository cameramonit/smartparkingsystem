import print
import barricade

def func():

    import scan
    import checkspace

    scan.scan()
    
    empty_image = 'images/test.jpg'
    current_image = 'images/target.jpg'

    coordinates = [[512, 405, 271, 419, 277, 311, 503, 293],
[503, 293, 278, 311, 280, 203, 486, 191],
[486, 191, 281, 202, 286, 136, 475, 121]]

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
