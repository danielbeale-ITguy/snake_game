
class boarder:
    def __init__(self,screen,screen_height,square_size,color):
        self.screen = screen
        self.screen_height = screen_height
        self.square_size = square_size
        self.color = color
        self.second_color = WHITE
        self.line_color = RED
        self.grid_list = []
        self.border_data = boarder_data

#defines the grid out Rects using double for loop
    def grid(self):
        for row in range(0,self.screen_height,self.square_size):
            for column in range(0,self.screen_height,self.square_size):
                rect = pygame.Rect(row,column,self.square_size,self.square_size)
                self.grid_list.append(rect)
# draws the Rect list to screen
    def draw_grid(self):
        for square_to_draw in self.grid_list:
                pygame.draw.rect(self.screen, self.second_color, (square_to_draw))

# This is just to act a guide, no other funciton
    def line_guide(self):
        for line in range(0,self.screen_height,self.square_size):
            pygame.draw.line(self.screen,self.line_color,(line,0),(line,self.screen_height))
            pygame.draw.line(self.screen,self.line_color, (0,line),(self.screen_height,line))

