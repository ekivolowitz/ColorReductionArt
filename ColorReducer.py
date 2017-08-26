import sys
from Colors import TEN_COLORS as colors
from PIL import Image
from math import sqrt
from matplotlib.colors import to_rgba_array

# Used for debugging.
hex_value = True

try:
    im = Image.open(sys.argv[1])
except:
    raise("Error: cannot open image")
px = im.load()

if hex_value:
    # This section of code iterates over the every pixel in the image,
    # and converts its color to an rgb tuple. It will then calculate the 
    # euclidean distance (https://en.wikipedia.org/wiki/Euclidean_distance)
    # of all of the colors and set the color of the pixel to be the color with the 
    # shortest distance. I'm not knowledgeable on color theory, but this is the best
    # way to reduce colors that I could think of. As I learn more, I will create a less
    # intensive, more efficient algorithm.
    for x in range(im.size[1]):
        for y in range(im.size[0]):
            minColorDistance = -1
            minColor = None
            pixel = px[x,y]
            for color in colors:
                rgb = to_rgba_array(color)[0]
                for i,val in enumerate(rgb):
                    rgb[i] = int(val * 255)
                distance = sqrt((pixel[0] - rgb[0]) ** 2 + (pixel[1] - rgb[1]) ** 2 + (pixel[2] - rgb[2]) ** 2)
                if minColorDistance == -1:
                    minColorDistance = distance
                    minColor = rgb
                else:
                    if minColorDistance > distance:
                        minColorDistance = distance
                        minColor = rgb
                
            px[x,y] = (int(minColor[0]), int(minColor[1]), int(minColor[2]))

else:
    # Same concept as in the if clause, except the color coming in is already in rgb form.
    # I should probably turn this into a function and then just call it from above. 
    for x in range(im.size[1]):
        for y in range(im.size[0]):
            minColorDistance = -1
            minColor = None
            pixel = px[x,y]
            for color in colors:
                distance = sqrt((pixel[0] - color[0]) ** 2 + (pixel[1] - color[1]) ** 2 + (pixel[2] - color[2]) ** 2)
                if minColorDistance == -1:
                    minColorDistance = distance
                    minColor = color
                else:
                    if minColorDistance > distance:
                        minColorDistance = distance
                        minColor = color
            px[x,y] = (color[0], color[1], color[2])
            

im.show()
