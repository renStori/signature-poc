from PIL import Image, ImageDraw

from base62 import base62_to_int
from config import canvas_size
from helpers import from_int_to_coords


def load_file(filename):
    content = []
    with open(filename, "r") as f:
        for line in f:
            content.append(line)
    if len(content) == 1:
        return content[0]
    return content


base62_string = load_file("output/painted_pixels_encoded")

# Define the size of the image
width, height = canvas_size

# Create a new white image
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Decode the base62 string back to coordinates
painted_pixels = from_int_to_coords(base62_to_int(base62_string))

# Draw the signature from the coords
for i in range(1, len(painted_pixels)):
    x1, y1 = painted_pixels[i - 1]
    x2, y2 = painted_pixels[i]
    draw.line((x1, y1, x2, y2), fill="black", width=2)

# Save and show the image
image.save("output/recovered_signature.png")
image.show()
