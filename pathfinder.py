from PIL import Image



# take hight map and build color map
with open("elevation_small.txt") as file:
    for word in file:
        # this nested list comprehention makes a float... for each item in the list... in the array
        elevation_list = [[float(smaller_thing) for smaller_thing in thing.split()] for thing in file.readlines()] 

        # find the highest elevation
        # build list of highest elevations
        max_list = max(elevation_list)
        #find highest elevation  of that list
        max_elevation = max(max_list)

        # take (each elevation and divide them by the maximum elevation) then multiply each by 255
        color_code_list = [[int(((each/max_elevation)*255)) for each in num_list] for num_list in elevation_list]
        # print(color_code_list)


# get height and width
# height is the number of lists
print(len(elevation_list[0]))
# width is the length of each list (number of rows)
print(len(elevation_list))



# clinton magical biz =>
# enumerate
    # for y, row in enumerate(data):
    #     for x, num in enumerate(row):
    #         img.putpixel((x, y), (num, num, num))
    # img.save('test.png')

# abs method meaning absolute value 