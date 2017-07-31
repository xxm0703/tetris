import pygame
import random
import obj


pygame.init()
box_size = 10
wide = 10
high = 20
screen = pygame.display.set_mode((wide*box_size, high*box_size))
clock = pygame.time.Clock()
line = []
figs = [obj.O, obj.I, obj.S, obj.Z, obj.L, obj.J, obj.T]
fig_index = random.randint(0, 1)
obj_y = 0
obj_x = 5
ch_x = 0
speed = 2
IN = True
cent = figs[fig_index](obj_x, obj_y)
pos = []
OK = 1
while IN:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                speed = 10
            elif event.key == pygame.K_RIGHT:
                check_list = [[x + 1, y] for x, y in cent.Ret_list()]
                if len([x for x in check_list if x in pos[:-4]]) == 0:
                    ch_x = 1
                    var = "R"
            elif event.key == pygame.K_LEFT:
                check_list = [[x-1, y] for x, y in cent.Ret_list()]
                if len([x for x in check_list if x in pos[:-4]]) == 0:
                    ch_x = -1
                    var = "L"
        elif event.type == pygame.KEYUP:
            ch_x = 0
            speed = 2
        elif event.type == pygame.QUIT:
            IN = False
        cent.x += ch_x

    # Stop
    for x in cent.Ret_list():
        print(x)
        x[1] += 1
        for y in pos[:-1]:
            if x in y.Ret_list():
                OK = 0
        if not OK or high - 1 in cent.Ret_y():
            pos.append(cent)
            cent = figs[random.randint(0, 1)](int(wide / 2), 0)
            OK = 0
            break
    if OK:
        cent.Drop()
    else:
        OK = 1
    print()
    # Draw
    for y in pos:
        for x in y.Ret_list():
            obj.Box(screen, x[0], x[1], box_size).Draw()

    for x in cent.Ret_list():
        obj.Box(screen, x[0], x[1], box_size).Draw()

    pygame.display.update()
    clock.tick(speed)
    screen.fill((250, 250, 250))
pygame.quit()
