# from rembg import remove
# from PIL import Image
# inputPath = 'some.jpg'
# outputPath = 'some.png'
# inp = Image.open(inputPath)
# output = remove(inp)
# output.save(outputPath)

from rembg import remove
from PIL import Image

# Define input and output paths
inputPath = 'some.jpeg'
outputPath = 'some.png'

# Open the input image
inp = Image.open(inputPath)

# Remove the background
output = remove(inp)

# Save the output image
output.save(outputPath)
