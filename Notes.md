- Compaired ImageDraw.point to Image.putpixle and found run times of 0m4.616s and 0m4.000s respectfully
- decide to stick with putpixle

```py
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
        draw = ImageDraw.Draw(test)
        # y value is the first index of every row
        for y, row in enumerate(color_code_map):
            # x values are list items sequentially
            for x, num in enumerate(row):
                draw.point((x,y), (num, num, num))
        # might have to make save a function
        return test.save(self.name)  
```

- changed make_heigth_map_png by taking out the height, width and Image.new and put them in their own function
```py
def make_height_map_png(self, file):
        '''
        takes a color_code_map and outputs a png file
        '''
        color_code_map = self.make_color_code_map(file)
        # # height is the number of lists
        # height = len(color_code_map)
        # # width is the length of each list (number of rows)
        # width = len(color_code_map[0])
        # test = Image.new('RGB', (height, width))
        # y value is the first index of every row
        test = self.make_new_image(color_code_map)
        for y, row in enumerate(color_code_map):
            # x values are list items sequentially
            for x, num in enumerate(row):
                test.putpixel((x,y), (num, num, num))   
        return test.save(self.name)
```

completely failed attempt

```py
class Pathfinder:
    def __init__(self):
        pass

    
    def y_half_way(self, map):
        '''
        takes map data and finds the half way down 'y' value
        '''
        # look at the amount of rows and divide by half
        y = len(map)/2
        return y

    def top_choice(self, x, y):
        y += 1 
        x_y = []
        x_y.append(x, y)
        return x_y
    
    def mid_choice(self, x, y):
        x += 1 
        return x

    def bot_choice(self, x, y): 
        y -= 1 
        return y

    def simple_pathfinder(self, map, x, y):
        '''
        looks at the next 3 coordinates and chooses one
        '''
        
        t_y = self.top_choice(x, y)
        m_y =self.mid_choice(x, y)
        b_y =self.bot_choice(x, y)
        # take these and put them in a list
        choice_list = [t_y, m_y, b_y]

        
        # find minium after checking the absolute value of each item in list
        # min(new_list, key = abs)
        # if top and bottom are the same pick random
        # resets the current coordinates to the choice
        # repeates until out of choices
        # deals with 'edge' conditions
```