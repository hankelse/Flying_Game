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

enemy_num = 1

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
speed = init_speed
scroll_speed = init_speed

enemies= []
for i in range(enemy_num): enemies.append(characters.new_enemy())


#--RUNNING--#
x=0
lose = False
while lose == False:
    x+=1
    now = time.time()
    screen.fill((160, 160, 160))
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    if keys[bindings["boost"]] and speed < 10:
        speed += 0.5
        sky.change_speed(round(speed))
    
    elif keys[bindings["slow"]] and speed >= 5:
        speed -= 0.5
        sky.change_speed(round(speed))

    if keys[bindings["boost"]] or keys[bindings["slow"]]: pass
    elif speed > 4:
        speed -= deceleration
        sky.change_speed(round(speed))
        # if x % int(1/deceleration) == 0:
        #     scroll_speed -= 1
        #     sky.change_speed(scroll_speed)
    sky.move()
    sky.draw()

    player.move(keys, bindings, speed)
    player.draw()
    
    for enemy in enemies:
        enemy.move(speed)
        characters.test_collision(player, enemy)
        enemy.draw()
        if enemy.y - enemy.size/2 > height: 
            enemies.remove(enemy)
            enemies.append(characters.new_enemy())
    


    
    pygame.display.flip()
    elapsed = time.time()-now
    if elapsed < cycle_time:
        time.sleep(cycle_time-elapsed)