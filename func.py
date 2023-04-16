import barricade

def func():

    import scan
    import checkspace

    scan.scan()
    
    empty_image = 'images/test.jpg'
    current_image = 'images/target.jpg'

    coordinates = [[231, 437, 36, 453, 60, 363, 235, 346],
[238, 302, 66, 320, 84, 248, 239, 232],
[243, 203, 93, 216, 107, 145, 244, 125],
[625, 389, 423, 411, 412, 324, 585, 303],
[576, 266, 409, 287, 398, 216, 555, 199],
[547, 172, 392, 186, 388, 114, 523, 102]]

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
