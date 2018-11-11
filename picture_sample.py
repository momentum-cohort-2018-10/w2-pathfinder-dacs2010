from PIL import Image

test = Image.new('RGB', (50,50), color=(255, 255, 255))

test.save("test.png")