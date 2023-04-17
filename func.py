import barricade

def func():

    import scan
    import checkspace

    scan.scan()
    
    empty_image = 'images/test.jpg'
    current_image = 'images/target.jpg'

    coordinates = [[89, 319, 91, 102, 206, 88, 227, 297],
[230, 297, 213, 86, 360, 67, 414, 272],
[418, 271, 365, 66, 493, 52, 570, 249]]

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
        print("Park at slot: ", random.choice(available))
        barricade.barricade()
    else:
        print("No space.")
