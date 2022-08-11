from cmath import pi
import math, pygame, random
from re import L
pygame.init()

size = width, height =  800, 800
cycle_time = 0.025

screen = pygame.display.set_mode(size)

class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.startingx, self.startingy = x, y
        self.angle = pi/2
        self.speed = 2
        self.color = (0, 0, 0)
        self.radius = 25
        self.rotate_speed = 0.2
        self.xv, self.yv = 0, 0
        self.deceleration = 0.1
        self.min_speed, self.max_speed = -10, 10
        self.point1, self.point2, self.point3 = (self.x+self.radius*math.cos(self.angle), self.y-self.radius*math.sin(self.angle)), (self.x+self.radius*math.cos(self.angle-(2*pi/3)), self.y-self.radius*math.sin(self.angle-(2*pi/3))), (self.x+self.radius*math.cos(self.angle+(2*pi/3)), self.y-self.radius*math.sin(self.angle+(2*pi/3)))
    def move(self, keys, bindings, speed, base_speed):
        
        if speed == base_speed: self.y = self.startingy
        else:
            self.y = self.startingy + (speed-base_speed)*15
        

        if keys[bindings["left"]]:
            if self.xv - self.speed > self.min_speed:
                self.xv -= self.speed
            
            if self.angle%(2*pi)<3*pi/4:
                self.angle += self.rotate_speed
        elif keys[bindings["right"]]:
            if self.xv + self.speed < self.max_speed:
                self.xv += self.speed
            if self.angle%(2*pi)>pi/4:
                self.angle -= self.rotate_speed
        else:
            if abs(self.angle%(2*pi) - pi/2) > self.rotate_speed:
                if self.angle > pi/2:
                    self.angle -= self.rotate_speed
                else: self.angle += self.rotate_speed
            else: self.angle = pi/2

            if self.xv > 0:
                self.xv -= self.deceleration*self.xv
            elif self.xv < 0:
                self.xv -= self.deceleration*self.xv
        
        if self.xv<0 and self.x > self.radius:
                self.x += self.xv *(speed/6)
        elif self.xv > 0 and self.x < width-self.radius:
                self.x += self.xv *(speed/6)


        #pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 800), 10)
    def draw(self):
        self.point1, self.point2, self.point3 = (self.x+self.radius*math.cos(self.angle), self.y-self.radius*math.sin(self.angle)), (self.x+self.radius*math.cos(self.angle-(2*pi/3)), self.y-self.radius*math.sin(self.angle-(2*pi/3))), (self.x+self.radius*math.cos(self.angle+(2*pi/3)), self.y-self.radius*math.sin(self.angle+(2*pi/3)))
        pygame.draw.polygon(screen, self.color, [self.point1, self.point2, self.point3], 2)

    def point_in_tri(self, px, py, buffer=0):
        ax, ay = self.point1[0], self.point1[1]
        bx, by = self.point2[0], self.point2[1]
        cx, cy = self.point3[0], self.point3[1]

        w1 = (ax*(cy-ay) + (py-ay)*(cx-ax)-px*(cy-ay))  /  ((by-ay)*(cx-ax) - (bx-ax)*(cy-ay))
        w2 = (py-ay-w1*(by-ay)) / (cy-ay)

        if w1 >= 0-buffer and w2 >= 0-buffer and (w1+w2) <= 1+buffer: return(True)
        return(False)


class Enemy:
    def __init__(self, x, speed, size):
        self.x, self.y = x, -1*size-random.randint(0, 100)
        self.size, self.speed = size, speed
    def move(self, speed):
        self.y+=self.speed*speed/6
    def draw(self):
        pygame.draw.ellipse(screen, (0, 0, 0), pygame.Rect(self.x-self.size/2, self.y-self.size/2, self.size, self.size), 3)


def new_enemy():
    return(Enemy(random.randint(25, width-25), random.randint(6, 10), random.randint(25, 75)))


def collision(player, enemy, node_visible):
    if enemy.x < player.x: factor = -1
    else:factor = 1

    #check top
    horo_distance, vert_distance = abs(player.point1[0]-enemy.x), abs(player.point1[1]-enemy.y)
    if math.sqrt(horo_distance**2 + vert_distance**2) <= enemy.size/2:
        return True


    #one side
    perp_slope = -1/((player.point1[1]-player.point2[1])/(player.point1[0]-player.point2[0]))
    enemy_contact_angle = math.atan(perp_slope)
    px, py = enemy.x+ math.cos(enemy_contact_angle)*enemy.size/2 *-1*factor, enemy.y+math.sin(enemy_contact_angle)*enemy.size/2 *-1
    if node_visible == True: pygame.draw.ellipse(screen, (255, 0, 0), pygame.Rect(px-5, py-5, 10, 10))
    if player.point_in_tri(px, py) == True: return True
    
    # bottom side
    if player.point2[1] != player.point3[1]:
        perp_slope = -1/((player.point2[1]-player.point3[1])/(player.point2[0]-player.point3[0]))
        enemy_contact_angle = math.atan(perp_slope)
    else: enemy_contact_angle = pi/2*factor

    px, py = enemy.x+ math.cos(enemy_contact_angle)*enemy.size/2 *-1*factor, enemy.y+math.sin(enemy_contact_angle)*enemy.size/2 *-1

    if node_visible == True: pygame.draw.ellipse(screen, (0, 255, 0), pygame.Rect(px-5, py-5, 10, 10))
    if player.point_in_tri(px, py) == True: return True
    
    
    return False


    pass

def test_collision(player, enemy, node_visible):

    buffer = ((enemy.size/2)/player.radius-1)/3

    #buffer = (enemy.size/2)/((player.radius)*2)

    if node_visible == True: pygame.draw.ellipse(screen, (255, 0, 0), pygame.Rect(enemy.x-5, enemy.y-5, 10, 10))
    if player.point_in_tri(enemy.x, enemy.y, buffer) == True: return True

    


    
    
    return False
