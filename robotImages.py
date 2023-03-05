from PIL import Image

# open the image
img = Image.open("robot.jpg")

# crop the image to zoom in on the robot
# left = 100
# top = 100
# right = 400
# bottom = 400
# img = img.crop((left, top, right, bottom))

# resize the image to 1000 x 1000 pixels
img = img.resize((900, 1200))


img.save("robot_cropped.jpg", optimize=True, quality=50)