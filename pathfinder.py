from PIL import Image, ImageDraw

class Map:
    def __init__(self, name):
        '''
        
        '''
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

    def find_single_path(self, file):
        '''
        finds a 'greedy' path across the map horozontally
        '''
        # use min() and abs()
        # set current coordinates
        # look at the next 3 choices and choose one
        # reset the current coordinates to the choice
        # repeate until out of choices
        # deal with 'edge' conditions
    


    def make_new_image(self, color_code_map):
        # get the height
        # get the width
        # make new image
        # height is the number of lists
        height = len(color_code_map)
        # width is the length of each list (number of rows)
        width = len(color_code_map[0])
        new_image = Image.new('RGB', (height, width))
        return new_image

    def make_height_map_png(self, file):
        '''
        takes a color_code_map and outputs a png file
        '''
        # call color_code_map and set it to new variable
        color_code_map = self.make_color_code_map(file)
        # call make_new_image and set it to new variable
        new_image = self.make_new_image(color_code_map)
        # y values are each row
        for y, row in enumerate(color_code_map):
            # x values are list items sequentially
            for x, num in enumerate(row):
                new_image.putpixel((x,y), (num, num, num))   
        # might have to make save a function
        return new_image.save(self.name)            
    
    # take 'save' out of make_height_map_png
    # def save_png(self, file):
    #     file.save(self.name)

class Pathfinder:
    # use min() and abs()
    
    # looks at the next 3 choices and chooses one
    # resets the current coordinates to the choice
    # repeates until out of choices
    # deals with 'edge' conditions
    def __init__(self):
        pass

    # sets current coordinates
    def half_way_down(self, map):
        '''
        takes map data and finds the half way down y value
        '''
        # look at the amount of rows and divide by half
        half_way_down = len(map)/2
        return half_way_down
    
    




map = Map("maps/test_small_test_altered_new_image.png") 
color_map = map.make_color_code_map("elevation_small.txt")
finder = Pathfinder()
print(finder.half_way_down(color_map))
# map.make_height_map_png('elevation_small.txt')



