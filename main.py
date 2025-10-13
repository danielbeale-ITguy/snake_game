import pygame
from Variables import *



def main():












    pygame.init()
    screen_height = 700
    screen_width = 700
    screen = pygame.display.set_mode((screen_height,screen_width))
    clock = pygame.time.Clock()

    direction = 0


    square_size = 30
    running = True

    snake_x = 60
    snake_y = 60
    




    game_run = boarder(screen,screen_height,square_size,WHITE,boarder_data)
    snake_ = snake(snake_x,snake_y,square_size,screen)
    fruit = Fruit(screen,square_size)
    



    

    move = False
    game_run.grid()
    while running:
        

        key = pygame.key.get_pressed()
            

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False



            

            if key[pygame.K_d] and direction != 3:
                direction = 1
                right = True
                snake_.move_right()
            if key[pygame.K_a] and direction != 1:
                direction = 3
                snake_.move_left()
            if key[pygame.K_s] and direction != 4:
                direction = 2
                snake_.move_down()
            if key[pygame.K_w] and direction != 2:
                direction = 4
                snake_.move_up()
  


        if direction == 1:
            snake_.move_right()
        if direction == 3:
            snake_.move_left()
        if direction == 2:
            snake_.move_down()
        if direction == 4:
            snake_.move_up()





        


        screen.fill(LILY)
        fruit.draw_fruit()  

        
        snake_.draw_head()
        snake_.update_snake_body()
        
        
        if pygame.Rect.colliderect(snake_.snake_head,fruit.current_pos):
            fruit.fruit_collison()
            snake_.collison()

#        if snake_.snake_head.collidepoint(fruit.center):
#            fruit.fruit_collison()
#            snake_.collison()
        
            






        
        
        
        pygame.display.update()
        dt = clock.tick(60)
        
    #QUITS the game
    pygame.quit()



main()

