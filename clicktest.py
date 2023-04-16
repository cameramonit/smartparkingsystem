import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imwrite('images/test.jpg', frame)
cap.release()


from PIL import Image, ImageFilter

# Load the image
image_path = 'images/test.jpg'
image = Image.open(image_path)

# Convert the image to grayscale
grayscale_image = image.convert('L')

# Add Gaussian blur to the grayscale image
blurred_image = grayscale_image.filter(ImageFilter.GaussianBlur(radius=2))

# Save the blurred image
blurred_image.save('images/test.jpg')
