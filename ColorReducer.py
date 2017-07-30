# from Colors import PRIMARY_COLORS as colors
# from Colors import FIVE_SHADES_OF_RED as colors
from Colors import TEN_COLORS as colors
from PIL import Image
from math import sqrt
from matplotlib.colors import to_rgba_array
# from PIL import Image
# print(dir(Image))

hex_value = True


im = Image.open('test-image.jpg')
px = im.load()

if hex_value:
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
