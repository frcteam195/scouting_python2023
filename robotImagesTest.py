from PIL import Image

img = Image.open("frc176.jpg")

width = img.width
height = img.height

maxSize = 1000
quality = 75

print("original width: " + str(width))
print("original height: " + str(height))

newWidth = maxSize
newHeight = int((height / width) * maxSize)

print("new width: " + str(newWidth))
print("new height: " + str(newHeight))

resized_img = img.resize((newWidth, newHeight))
resized_img.save("frc176Resized.jpg", quality=quality)