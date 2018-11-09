from PIL import Image



# take hight map and build color map
with open("elevation_small.txt") as file:
    for word in file:
        # this nested list comprehention 
        # makes a float and removes white space... 
        # for each item in the list... 
        # in the array
        elevation_map = [[float(
            smaller_thing) for smaller_thing in thing.split()] for thing in file.readlines()] 

        # find the highest elevation
        # take the max of the max of the elevation_map
        max_elevation = max(max(elevation_map))
       
        # for each elevation, 
        # make each an int (this removes decimal)
        # divide by the maximum elevation...
        # then multiply by 255... 
        # for each item in the list...
        # in the array
        color_code_map = [[int(
            ((each/max_elevation)*255)) for each in num_list] for num_list in elevation_map]
        # print(color_code_map)

        # testing  initial concept 
        # color_code_map = [[int(
        #     (each/40)) for each in num_list] for num_list in elevation_map]


# get height and width
# height is the number of lists
height = len(elevation_map[0])
# print(height)
# width is the length of each list (number of rows)
width = len(elevation_map)
# print(width)

# y value is the first index of every row
# x value is the next index sequentially

def make_map(color_code_map):
    '''
    takes a color_code_map and outputs a png file
    '''
    test = Image.new('RGB', (height, width), (238, 255, 200))
    for y, row in enumerate(color_code_map):
        for x, num in enumerate(row):
            test.putpixel((x,y), (num, num, num))
    return test.save("test9.png")       
    
make_map(color_code_map)

# # make an image
# # set height
# # set width 
# test = Image.new('RGB', (height, width), color=(255, 255, 255))
# # save image
# test.save("test.png")


# clinton magical biz =>
# enumerate
    # for y, row in enumerate(data):
    #     for x, num in enumerate(row):
    #         img.putpixel((x, y), (num, num, num))
    # img.save('test1.png')

# abs method meaning absolute value 