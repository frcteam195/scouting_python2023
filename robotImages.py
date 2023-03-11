# from PIL import Image

# # open the image
# img = Image.open("robot.jpg")

# # crop the image to zoom in on the robot
# # left = 100
# # top = 100
# # right = 400
# # bottom = 400
# # img = img.crop((left, top, right, bottom))

# # resize the image to 1000 x 1000 pixels
# img = img.resize((900, 1200))


# img.save("robot_cropped.jpg", optimize=True, quality=50)


import os
import glob
from PIL import Image
import time

# define the directory where the images are located
directory = "/media"

# get a list of all the jpeg files in the directory
jpeg_files = glob.glob(os.path.join(directory, "*.jpg"))
print(jpeg_files)


# define the maximum size for the images
max_size = (1000, 1000)

# define the quality factor for the images
quality = 50

# define the file name for the timestamp file
timestamp_file = "processed_images.txt"

# check if the timestamp file exists
if os.path.isfile(os.path.join(directory, timestamp_file)):
    # read the contents of the timestamp file
    with open(os.path.join(directory, timestamp_file), "r") as f:
        processed_images = f.read().splitlines()
else:
    # create an empty list if the timestamp file doesn't exist
    processed_images = []

# # loop through all the jpeg files in the directory
for jpeg_file in jpeg_files:
    # get the file name and check if it has already been processed
    filename = os.path.basename(jpeg_file)
    if filename in processed_images:
         continue
    print(filename)
    # open the image file
    with Image.open(jpeg_file) as im:
        # resize the image
        im.thumbnail(max_size)
        tmp = f"/tmp/{filename}"
        tmp2 = f"/tmp/images/{filename}"
        print(tmp)
        # save the resized image with the same file name
        im.save(tmp, quality=quality)
        im.save(tmp2, quality=quality)

        # add the file name to the list of processed images
        processed_images.append(filename)

# write the list of processed images to the timestamp file
with open(os.path.join(directory, timestamp_file), "w") as f:
    f.write("\n".join(processed_images))
