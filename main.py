import pygame
from cloudinit.sources.DataSourceConfigDrive import LABEL_TYPES
from gi.types import snake_case
from numpy.array_api import square
from oauthlib.uri_validate import segment_nz_nc
from pexpect.screen import screen
from pkg_resources import working_set




boarder_data = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]






WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
LILY = (250,225,255)
GREEN = (0,255,0)
LIGHT_RED = (255,189,189)



pygame.init()
screen_height = 700
screen_width = 700
screen = pygame.display.set_mode((screen_height,screen_width))
clock = pygame.time.Clock()

direction = 0

right = False




square_size = 25
running = True

snake_x = 50
snake_y = 50



class boarder:
    def __init__(self,screen,screen_height,square_size,color,world_data):
        self.screen = screen
        self.screen_height = screen_height
        self.square_size = square_size
        self.color = color
        self.second_color = WHITE
        self.line_color = GREEN
        self.grid_list = []
        self.world_data = world_data

#defines the grid out Rects using double for loop

    def grid(self):
        y_count = 0
        for row in self.world_data:
            x_rect = 0
            for column in row:
                if column == 1:
                    self.grid_list.append((x_rect,y_count,self.square_size,self.square_size))
                x_rect += self.square_size
            x_rect = 0
            y_count += self.square_size

    # draws the Rect list to screen
    def draw_grid(self):
        for square_to_draw in self.grid_list:
                pygame.draw.rect(self.screen, self.second_color, (square_to_draw))

# This is just to act a guide, no other funciton
    def line_guide(self):
        for line in range(0,self.screen_height,self.square_size):
            pygame.draw.line(self.screen,self.line_color,(line,0),(line,self.screen_height))
            pygame.draw.line(self.screen,self.line_color, (0,line),(self.screen_height,line))






class snake:
    def __init__(self,snake_x,snake_y,square_size,screen):
        self.snake_x = snake_x
        self.snake_y = snake_y
        self.square_size = square_size
        self.screen = screen
        self.snake_head = pygame.Rect(self.snake_x, self.snake_y,self.square_size, self.square_size)
        self.speed = 3
        self.dx = 1



    def draw_snake_head(self):
        pygame.draw.rect(self.screen,RED,(self.snake_head))


    def move_right(self):
        self.snake_head.x += self.speed * self.dx
    def move_left(self):
        self.snake_head.x -= self.speed
    def move_up(self):
        self.snake_head.y -= self.speed
    def move_down(self):
        self.snake_head.y += self.speed







game_run = boarder(screen,screen_height,square_size,WHITE,boarder_data)
snake_ = snake(snake_x,snake_y,square_size,screen)
move = False
while running:
    dt = clock.tick(60)




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        
        key = pygame.key.get_pressed()

        if key[pygame.K_d] and direction != 3:
            direction = 1
            snake_.move_right()
        if key[pygame.K_a] and direction != 1:
            direction = 3
            snake_.move_left()
        if key[pygame.K_s] and direction != 4:
            direction = 2
            snake_.move_down()
        if key[pygame.K_w] and direction != 4:
            direction = 2
            snake_.move_up()







    screen.fill(LILY)

    # Testing out how to draw and update snake, can use below, or you can define the rect outside of the loop and use the snake_rect.x += 5

    snake_.draw_snake_head()


    pygame.display.update()
#QUITS the game
pygame.quit()



