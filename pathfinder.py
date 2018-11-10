from PIL import Image

class Map:
    def __init__(self, name):
        self.name = name

    def make_color_code_map(self, file):
        '''
        take the height map data and turn it into color map data
        '''
        with open(file) as file:
                # this nested list comprehention 
                # makes a float and removes white space... 
                # for each item in the list... 
                # in the array
            elevation_map = [[float(
                smaller_thing) for smaller_thing in thing.split()] for thing in file.readlines()] 

            # find the minimum 
            min_list = [min(row) for row in elevation_map]
            min_elevation = min(min_list)
            
            # find the highest elevation
            max_list = [max(row) for row in elevation_map]
            max_elevation = max(max_list)

            # for each elevation, 
            # make each an int (this removes decimal)
            # divide by the maximum elevation...
            # then multiply by 255... 
            # for each item in the list...
            # in the array
            color_code_map = [[int(
                (((each - min_elevation)/(max_elevation - min_elevation))*255)) for each in num_list] for num_list in elevation_map]
        return color_code_map

    def make_height_map_png(self, file):
        '''
        takes a color_code_map and outputs a png file
        '''
        color_code_map = self.make_color_code_map(file)
        # height is the number of lists
        height = len(color_code_map)
        # width is the length of each list (number of rows)
        width = len(color_code_map[0])
        test = Image.new('RGB', (height, width))
        # y value is the first index of every row
        for y, row in enumerate(color_code_map):
            # x values are list items sequentially
            for x, num in enumerate(row):
                test.putpixel((x,y), (num, num, num))
        return test.save(self.name)       
    
map = Map("maps/test_tiny2.png") 
map.make_height_map_png('elevation_tiny.txt')

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