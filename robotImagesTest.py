from PIL import Image
team = 176
img = Image.open(f"media/frc{team}.jpg")

height = img.width
width = img.height

maxSize = 1000
quality = 75

print("original width: " + str(width))
print("original height: " + str(height))

img = img.rotate(-90, expand= True)

newWidth = maxSize
newHeight = int((height / width) * maxSize)

print("new width: " + str(newWidth))
print("new height: " + str(newHeight))
resized_img = img.resize((newWidth, newHeight))
resized_img.save(f"frc{team}Resized.jpg", quality=quality)