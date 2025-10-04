from numpy.array_api import square

boarder_data = [[1,1,1,1,1,1,1,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0,0,0,0,0,0]]

square_size = 50

for row in boarder_data:
    for column in row:
        rect_x = row * square_size
        rect_y = column * square_size
        pygame.draw.rect(screen,RED,(rect_x,rect_y,square_size,square_size))