import obj
import pygame

pygame.init()
box_size = 10
wide = box_size*10
high = box_size*20
screen = pygame.display.set_mode((wide, high))
clock = pygame.time.Clock()
pos = []
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
    print([x for x in cent.Ret_list() if x in pos[:-4]])
    if 20 in cent.Ret_y() or [x for x in cent.Ret_list() if x in pos[:-5]]:
        obj_y = 0
        print("hi")
    else:
        print (pos)
        del pos[-4:]
        #del pos[-1]
        #del pos[0])
    line = []
    for cord in pos:
        line.append(cord[1])
    for j in range(21):
        if line.count(j) == 10:
            i = 0
            while i < 10:
                del pos[line.index(j)]
                i += 1
    pygame.display.update()
    clock.tick(speed)
pygame.quit()
