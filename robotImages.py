import os
import glob
from PIL import Image
import time

directory = "/media"
jpeg_files = glob.glob(os.path.join(directory, "*.jpg"))

max_size = (1000, 1000)
quality = 50

timestamp_file = "processed_images.txt"

if os.path.isfile(os.path.join(directory, timestamp_file)):
    with open(os.path.join(directory, timestamp_file), "r") as f:
        processed_images = f.read().splitlines()
else:
    processed_images = []

for jpeg_file in jpeg_files:
    filename = os.path.basename(jpeg_file)
    if filename in processed_images:
         print(f"skipping {filename}, already processed")
         continue
    print(f"processing {filename}")
    with Image.open(jpeg_file) as image:
        image.thumbnail(max_size)
        save = f"{directory}/robotThumbnails/{filename}"
        image.save(save, quality=quality)
        processed_images.append(filename)

with open(os.path.join(directory, timestamp_file), "w") as f:
    f.write("\n".join(processed_images))
