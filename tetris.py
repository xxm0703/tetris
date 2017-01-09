import pygame

import obj

pygame.init()
box_size = 10
wide = 10
high = 20
screen = pygame.display.set_mode((wide*box_size, high*box_size))
clock = pygame.time.Clock()
pos = []
line = []
obj_y = 0
obj_x = 5
ch_x = 0
speed = 2
IN = True
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
    obj_x += ch_x
    obj_y += 1
    screen.fill((255,255,255))
    cent = obj.O(screen,obj_x,obj_y, box_size)
    #for cords in obj.O(screen,obj_x,obj_y,box_size).Ret_list()
    pos.extend(cent.Ret_list())
    for fig in pos:
        obj.Box(screen,fig[0],fig[1],box_size).Draw()
    print(pos)
    if 19 in cent.Ret_y() or [x for x in cent.Ret_list() if x in pos[:-5]]:
        obj_y = 0
        for cords in cent.Ret_list():
            line.append(cords[1])
        print("hi")
    else:
        del pos[-4:]
    print(pos)
    print(line)
    for j in range(high):
        if line.count(j) == wide:
            i = 0
            while i < wide:
                g = line.index(j)
                print(g)
                del line[g]
                del pos[g]
                i += 1
            pos = [[x,y+1] if y < j else [x,y] for x,y in pos]
    pygame.display.update()
    clock.tick(speed)
pygame.quit()
