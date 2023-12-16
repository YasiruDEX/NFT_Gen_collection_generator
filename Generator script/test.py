# import PIL module
from PIL import Image

# Front Image
filename = '002.png'

# Back Image
filename1 = '001.png'

# Open Front Image
frontImage = Image.open(filename)

# Open Background Image
background = Image.open(filename1)

# Convert image to RGBA
frontImage = frontImage.convert("RGBA")

# Convert image to RGBA
background = background.convert("RGBA")

# Calculate width to be at the center
width = (background.width - frontImage.width) // 2

# Calculate height to be at the center
height = (background.height - frontImage.height) // 2

# Paste the frontImage at (width, height)
background.paste(frontImage, (width, height), frontImage)

# Save this image
background.save("new.png", format="png")
