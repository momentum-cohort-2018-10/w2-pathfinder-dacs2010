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