from PIL import Image

with open("elevation_small.txt") as file:
    for word in file:
        elevation_list = file.readlines()
        elevation_list = [each_thing.split() for each_thing in elevation_list] 
        # elevation_list = [y/22 for y in file]
print(elevation_list[0])


