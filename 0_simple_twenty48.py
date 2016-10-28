"""
Clone of 2048 game.
"""

import poc_2048_gui
import random
import numeric
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    origin_len = len(line)
    new_line = list(line)
    empty_space = 0
    # remove zero
    while empty_space in new_line:
        new_line.remove(0)
    # merge
    tile_cursor = 0
    for dummy_count in range(len(new_line) - 1):
        if tile_cursor >= (len(new_line) - 1):
            break
        elif new_line[tile_cursor] == new_line[tile_cursor + 1]:
            new_line[tile_cursor] = 2 * new_line[tile_cursor]
            new_line[tile_cursor + 1] = 0
            tile_cursor = tile_cursor + 2
        else:
            tile_cursor += 1
    
    #remove zero
    while empty_space in new_line:
        new_line.remove(0)
    list_zero = [0] * (origin_len - len(new_line))
    new_line.extend(list_zero)
    
    return new_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.grid = [[]]
        self.reset()
        self.__direct_top = {
            UP: [(0,i) for i in range(self.grid_width)],
            DOWN:[(self.grid_height - 1,i) for i in range(self.grid_width)],
            RIGHT:[(i,self.grid_width - 1) for i in range(self.grid_height)],
            LEFT:[(i,0) for i in range(self.grid_height)] 
        }
        self.__direct_range = {
            UP: self.grid_height,
            DOWN: self.grid_height,
            RIGHT: self.grid_width,
            LEFT: self.grid_width
        }
        self.update_dict = {
            UP:0,
            DOWN:1,
            RIGHT:2,
            LEFT:3
        }
                
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for dummy_col in range(self.grid_width)] for dummy_row in range(self.grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        for row in self.grid:
            print row
            print '\n'
        return str(self.grid)
        
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width
    
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        initial_tile = self.__direct_top[direction]
        offset = OFFSETS[direction]
        direct_range = self.__direct_range[direction]        
        backup_list = [[0 for dummy_col in range(self.grid_width)] for dummy_row in range(self.grid_height)]
        
        for initial_count, tile_cursor in enumerate(initial_tile):
            tem_list = []
            grid_cursor = tile_cursor
            for dummy_cursor in range(direct_range):
                
                tem_list.append(self.grid[grid_cursor[0]][grid_cursor[1]])
                grid_cursor = tuple(x + y for x,y in zip(grid_cursor,offset))
                
            new_list = merge(tem_list)
            if self.update_dict[direction] == 0:
                for col_cursor in range(direct_range):
                    backup_list[col_cursor][initial_count] = new_list[col_cursor]
            elif self.update_dict[direction] == 1: 
                for col_cursor in range(direct_range):
                    backup_list[self.grid_height -1 - col_cursor][initial_count] = new_list[col_cursor]
            elif self.update_dict[direction] ==3:
                backup_list[initial_count] = new_list
            else:
                for col_cursor in range(direct_range):
                    backup_list[initial_count][self.grid_width -1 - col_cursor] = new_list[col_cursor]
        
        flag = (self.grid == backup_list)
        self.grid = backup_list
        if not flag:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # check if is zero or not
        new_tile_added = False
        # a list to 2 90% of the time and 4 10% of the time
        new_tile_list = [2,2,2,2,2,2,2,2,2,4]
        counter = 0
        while not new_tile_added:
            row_position = random.randrange(0,self.grid_height)
            col_position = random.randrange(0,self.grid_width)
            if self.grid[row_position][col_position] == 0:
                self.grid[row_position][col_position] = random.choice(new_tile_list)
                new_tile_added = True
            if counter > self.grid_width * self.grid_height:
                print 'you failed'
                break

            counter +=1
                
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.grid[row][col]


#poc_2048_gui.run_gui(TwentyFortyEight(3, 5))
