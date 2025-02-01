import PIL
from PIL import Image
import PIL.Image

img = PIL.Image.open("C:/Users/Surjith S Hanji/OneDrive/Pictures/Saved Pictures/Camera Roll/WIN_20250109_14_17_34_Pro.jpg/")
width,height=img.size

print(width,"x",height)