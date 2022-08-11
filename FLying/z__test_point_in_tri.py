

from Sky import Sky
import Characters as characters

import pygame, sys, time, math, random
from pygame.constants import K_SPACE, K_ESCAPE,K_w, K_a, K_s, K_d
pygame.init()

size = width, height =  800, 800
cycle_time = 0.025

screen = pygame.display.set_mode(size)




#--SETTINGS--#
init_speed = 4
deceleration = 0.1
startingx, startingy = 400, 600

enemy_num = 10

    #KEYS
bindings = {
    "boost" : K_w,
    "slow": K_s,
    "left" : K_a,
    "right" : K_d
}

#--SETUP--#
sky = Sky(5, init_speed)
player = characters.Player(startingx, startingy)
player2 = characters.Player(startingx, startingy)
player2.radius= player.radius*2.5

speed = init_speed
scroll_speed = init_speed

enemies= []
for i in range(enemy_num): enemies.append(characters.new_enemy())


#--RUNNING--#
x=0
lose = False
color = (255, 255, 255)
screen.fill((255, 255, 255))
while lose == False:
    x+=1
    now = time.time()
    #screen.fill(color)
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    player.draw()
    player2.draw()
    x, y = pygame.mouse.get_pos()
    if player.point_in_tri(x,y, 0.5)==True: 
        pygame.draw.ellipse(screen, (0, 0, 0), pygame.Rect(x-2, y-2, 4, 4))
    else: pygame.draw.ellipse(screen, (255, 0, 0), pygame.Rect(x-2, y-2, 4, 4))

    

    
    pygame.display.flip()
    elapsed = time.time()-now
    if elapsed < cycle_time:
        time.sleep(cycle_time-elapsed)