import obj,pygame
pygame.init()
box_size = 10
wide = box_size*10
high = box_size*20
screen = pygame.display.set_mode((wide, high))
board = [[0]*10]*20
clock = pygame.time.Clock()
objects = []
obj_y = 0
obj_x = 5
ch_x = 0
speed = 2
IN = True
cent = obj.Box(screen, obj_x, obj_y, box_size)
objects.append(cent)
while IN:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                speed = 10
            elif event.key == pygame.K_RIGHT:
                ch_x = 1
            elif event.key == pygame.K_LEFT:
                ch_x = -1
        if event.type == pygame.KEYUP:
            ch_x = 0
            speed = 2
        elif event.type == pygame.QUIT:
            IN = False
    obj_y += 1
    obj_x += ch_x
    screen.fill((255,255,255))
    cent = obj.Box(screen, obj_x, obj_y, box_size)
    for fig in objects:
        fig.Draw()
    objects.append(cent)
    if obj_y > 19:

        obj_y = 0
    else:
        del objects[-2]
    pygame.display.update()
    clock.tick(speed)
    print(board)
pygame.quit()