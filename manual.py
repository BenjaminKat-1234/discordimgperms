from PIL import Image

# SETTINGS
image_path = "yourimage.png"
output_path = "output.gif"

# LOAD AND SAVE AS GIF
image = Image.open(image_path).convert("RGBA")
image.save(output_path, format="GIF")
