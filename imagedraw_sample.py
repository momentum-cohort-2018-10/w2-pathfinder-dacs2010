
# draws an 'x' over the image
# sample taken from PIL docs
from PIL import Image, ImageDraw

im = Image.open("maps/test_images/test2.png")

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
draw.point
del draw


im.save("maps/test_images/imagedraw_test1.png")