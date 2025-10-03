import pygame
from cloudinit.sources.DataSourceConfigDrive import LABEL_TYPES
from numpy.array_api import square
from pexpect.screen import screen

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
LAVENDAR = (230,230,250)




class boarder:
    def __init__(self,screen,screen_height,square_size,color):
        self.screen = screen
        self.screen_height = screen_height
        self.square_size = square_size
        self.color = color
        self.second_color = WHITE
        self.grid_list = []


#currently this grid method only ranges the left column
    def grid(self):
        for row in range(0,self.screen_height,self.square_size):
            rect = pygame.Rect(0,row,self.square_size,self.square_size)
            self.grid_list.append(rect)




# just checking this works dont user this draw method
    def draw_grid(self):
        counter = 0
        for square_to_draw in self.grid_list:
            if counter > 14:
                return
            elif counter % 2 == 0:
                pygame.draw.rect(self.screen,self.color,(square_to_draw))
                counter += 1
            else:
                pygame.draw.rect(self.screen, self.second_color, (square_to_draw))
                counter += 1



pygame.init()
screen_height = 700
screen_width = 700
screen = pygame.display.set_mode((screen_height,screen_width))









square_size = 50


test = boarder(screen,screen_height,square_size,RED)
running = True
try:






    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False





        screen.fill(LAVENDAR)



        test.grid()
        test.draw_grid()


        pygame.display.update()
    #QUITS the game
    pygame.quit()



except TypeError:
    print('got Type Error')
