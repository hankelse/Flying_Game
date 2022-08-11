from Sky import Sky
import Characters as characters

import pygame, sys, time, math, random
from pygame.constants import K_SPACE, K_ESCAPE,K_w, K_a, K_s, K_d
pygame.init()

size = width, height =  800, 800
cycle_time = 0.025

screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont("monospace", 50)




#--SETTINGS--#
init_speed = 8
deceleration = 0.1
startingx, startingy = 400, 600
init_lives = 3

enemy_node_visible = False

enemy_num = 2
new_enemy_interval = 100

boost_score_bonus = 0.1

    #KEYS
bindings = {
    "boost" : K_w,
    "slow": K_s,
    "left" : K_a,
    "right" : K_d
}

#--SETUP--#
def setup():
    sky = Sky(5, init_speed)
    player = characters.Player(startingx, startingy)
    speed = init_speed
    scroll_speed = init_speed
    score = 0
    lives = init_lives

    enemies= []
    for i in range(enemy_num): enemies.append(characters.new_enemy())

    collisions = 0

    text_color = (0, 0, 0)
    base_speed = init_speed

    return(sky, player, enemies, speed, scroll_speed, score, collisions, lives, text_color, base_speed)
sky, player, enemies, speed, scroll_speed, score, collisions, lives, text_color, base_speed = setup()




#--RUNNING--#
x=0
lose = False
game_state = "playing"
#colliding = False
while 1:
    x+=1
    if x % new_enemy_interval==0: enemies.append(characters.new_enemy())
    base_speed+=0.01
    now = time.time()
    screen.fill((160, 160, 160))
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    if game_state == "playing":
        # if x % 10 == 0:
        #     score = round(score+(1*(speed-2)/2))
        if x%round(20/(speed-3)*4) ==0:
            score = score+1

        if keys[bindings["boost"]]:
            score += boost_score_bonus
            if speed < 4+base_speed:
                speed += 0.5
            
            sky.change_speed(round(speed))
        
        elif keys[bindings["slow"]] and speed >= base_speed:
            speed -= 0.5
            sky.change_speed(round(speed))

        if keys[bindings["boost"]] or keys[bindings["slow"]]: pass
        elif speed > base_speed:
            speed -= deceleration
            sky.change_speed(round(speed))
            # if x % int(1/deceleration) == 0:
            #     scroll_speed -= 1
            #     sky.change_speed(scroll_speed)
        sky.move()
        sky.draw()
        
        for enemy in enemies:
            enemy.move(speed)
            if characters.collision(player, enemy, enemy_node_visible) == True: 
                
                player.y += enemy.speed*speed/6
                player.xv = (player.xv *-1)
                collisions+=1
                lives -= 1
                enemies.remove(enemy)
                enemies.append(characters.new_enemy())
                #killer = enemy
            enemy.draw()
            if enemy.y - enemy.size/2 > height: 
                enemies.remove(enemy)
                enemies.append(characters.new_enemy())
        
        player.move(keys, bindings, speed, base_speed)
        player.draw()
        # if collision > 0:
        #     player.y += collide.speed*speed/6
        #     if collide.x < player.x: player.x += collide.speed*speed/6
        #     elif collide.x > player.x: player.x -= collide.speed*speed/6
        #     collision-=1
        #     player.draw()

        if lives == 0: 
            game_state, lose = "round_over", True
            loss_time = time.time()

    elif game_state == "round_over":
        if lose == True:
            sky.colors[1] = (100, 0, 40)
            sky.colors[0] = (120, 130, 255)
            sky.draw()
            player.color, text_color = (255, 255, 255), (255, 255, 255)
            player.draw()
            #killer.draw()
            if time.time() - loss_time > 5 or keys[K_SPACE]:
                sky.colors[1] = (120, 130, 255)
                sky.colors[0] = (210, 210, 215)
                
                sky, player, enemies, speed, scroll_speed, score, colissions, lives, text_color, base_speed = setup()
                colliding = False
                game_state="playing"
        
            
    
    
    score_txt = myfont.render("Score: "+str(round(score)), 1, text_color)
    lives_txt = myfont.render("Lives: "+str(lives), 1, text_color)
    
    screen.blit(score_txt, (20, 10))
    screen.blit(lives_txt, (500, 10))
    pygame.display.flip() 
    elapsed = time.time()-now
    if elapsed < cycle_time:
        time.sleep(cycle_time-elapsed)