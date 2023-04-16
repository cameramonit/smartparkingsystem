def avg_dark_pixels(image_path, coords):
    import numpy as np
    from PIL import Image
    
    # Load image and convert to grayscale
    img = Image.open(image_path).convert('L')
    # Extract pixel values as a numpy array
    pixels = np.asarray(img)
    # Get coordinates of four points
    x1, y1, x2, y2, x3, y3, x4, y4 = coords
    # Define a list of distances between the points
    distances = [np.linalg.norm(np.array([x1, y1])-np.array([x2, y2])),
                 np.linalg.norm(np.array([x2, y2])-np.array([x3, y3])),
                 np.linalg.norm(np.array([x3, y3])-np.array([x4, y4])),
                 np.linalg.norm(np.array([x4, y4])-np.array([x1, y1]))]
    # Calculate the total number of dark pixels between the points
    total_dark_pixels = 0
    for i in range(len(distances)):
        x_start = int(round((coords[i*2]+coords[(i*2+2)%8])/2))
        y_start = int(round((coords[i*2+1]+coords[(i*2+3)%8])/2))
        x_end = int(round((coords[(i*2+2)%8]+coords[(i*2+4)%8])/2))
        y_end = int(round((coords[(i*2+3)%8]+coords[(i*2+5)%8])/2))
        dx = x_end - x_start
        dy = y_end - y_start
        dist = int(round(np.sqrt(dx*dx + dy*dy)))
        pixels_between = pixels[y_start:y_end, x_start:x_end].ravel()
        dark_pixels_between = len(pixels_between[pixels_between < 128])
        total_dark_pixels += dark_pixels_between
    # Calculate the average number of dark pixels between the points
    avg_dark_pixels = total_dark_pixels / len(distances)
    return avg_dark_pixels