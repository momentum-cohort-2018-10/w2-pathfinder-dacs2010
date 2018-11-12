from PIL import Image, ImageDraw

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
            elevation_map = [[float(smaller_thing) 
                for smaller_thing in thing.split()] 
                for thing in file.readlines()] 

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
                (((each - min_elevation)/(max_elevation - min_elevation))*255)
                ) 
                for each in num_list] 
                for num_list in elevation_map]
        return color_code_map    
    
    def make_new_image(self, color_code_map):
        '''
        makes new image, and finds height and width
        '''
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
        # return new_image.save(self.name)
        return new_image           

    def node_finder(self, current_node, num):
        x = current_node[0]
        # remove x...
        current_node.pop(0)
        # insert new x at the 0 index
        current_node.insert(0, x)
        # now i have to try to find the new y values
        y = current_node[1]
        # and then get the num for each of those values

        # print the number associated with the y value

    def single_path(self, file):
        '''
        draw a greedy line across the map
        '''
        # get data for coordinates
        color_file = self.make_color_code_map(file)
        # find the half way point for y value
        y_half_height = len(color_file) / 2
        y = int(y_half_height)

        x = 0
        current_node = [x, y]
        print(current_node)
        # grab the image to draw on
        image_to_draw_on = self.make_height_map_png(file)
        for _, row in enumerate(color_file):
            for x, num in enumerate(row):
                # remove x...
                current_node.pop(0)
                # insert new x at the 0 index
                current_node.insert(0,x)
                # now i have to try to find the new y values
                # and then get the num for each of those values
                # for coordinate in 
                # for y in current_node[1]:
                # print the number associated with the y value
                
                # draw line
                image_to_draw_on.putpixel((current_node), (255, 0, 0))
        return image_to_draw_on

    def save_png(self, file):
        '''
        saves files after they pass throuhg make_height_map
        '''
        file.save(self.name)

map = Map("maps/small_map7.png")
# height_map_png =  map.make_height_map_png('elevation_small.txt')
single_path = map.single_path("elevation_small.txt")
# => pathfinder gets called here
map.save_png(single_path)



