import pygame, sys, time, random
from pygame.constants import K_SPACE, K_ESCAPE,K_w, K_a, K_s, K_d
pygame.init()

size = width, height =  800, 800
cycle_time = 0.025

screen = pygame.display.set_mode(size)

class Sky:
    def __init__(self, pixel_size, cycle_speed=None, type="clouds"):
        self.pixel_size = pixel_size
        self.type = type
        self.colors = colors
        self.cycle_speed = cycle_speed
        self.grid =[]
        for i in range(int(height/pixel_size)):
            row = []
            for i in range(int(width/pixel_size)):
                row.append(random.choice([1,1,1,0]))
            self.grid.append(row)

        if self.type == "clouds":
            self.number = 0

    def waves(self):
        row = self.grid[0]

        direction = random.choice([0, -1])
        row.insert(direction, random.choice([0, 1, 1, 1]))
        
        if direction == 0: row = row[0:-1]
        elif direction ==-1: row = row[1::]
        return(row)
    
    def clouds(self):
        row = []
        prev = self.grid[0]
        for pixel in self.grid[0]:
            row.append(pixel)
        
        white = row.count(0)
        blue = row.count(1)
        if white > blue*0.2: dominant, submissive = 1, 0
        else: dominant, submissive = 0, 1

        def change(x, y, chance):
            if random.randint(1, 100) > chance: return(x)
            else: return(y)

        for i in range(len(row)):
            if i == 0:
                if prev[i] == submissive:
                    if prev[i+1] == dominant:
                        row[i]=change(submissive, dominant, 75)

        
            elif i == len(row)-1:
                if prev[i] == submissive:
                    if prev[i-1]== dominant:
                        row[i]=change(submissive, dominant,75)

            else:
                if prev[i] == submissive:
                    if prev[i+1] == dominant and prev[i-1] == dominant:
                        row[i]=change(submissive, dominant, 95)
                    elif prev[i+1] == dominant or prev[i-1] == dominant:
                        row[i]=change(submissive, dominant, 75)
                    else:
                        row[i]=change(submissive, dominant, 10)
                else:
                    if prev[i-1] == submissive and prev[i+1]==submissive:
                        row[i] = submissive



        



        return(row)

    def move(self):
        for i in range(self.cycle_speed):
            self.grid.insert(0, self.new_row())
        self.grid = self.grid[0:-1*self.cycle_speed]

    def new_row(self):
        if self.type == "waves": return(self.waves())
        elif self.type == "clouds": return(self.clouds())
    
    def draw(self):
        for row in range(len(self.grid)):
            for pixel in range(len(self.grid[row])):
                pygame.draw.rect(screen, self.colors[self.grid[row][pixel]], pygame.Rect(pixel*self.pixel_size, row*self.pixel_size, self.pixel_size, self.pixel_size))

    def change_speed(self, speed):
        self.cycle_speed = speed

colors= {
    0 : (210, 210, 215),
    1 : (120, 130, 255)
}

speed = 10
deceleration = 0.1
#sky = Sky(5, speed)

# x = 0
# while 1:
#     x+=1
#     now = time.time()
#     screen.fill((160, 160, 160))
#     keys=pygame.key.get_pressed()
#     if keys[K_ESCAPE]:
#         quit()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
    
#     #sky.move()
#     #sky.draw()

#     if keys[K_SPACE] and speed < 10:
#         speed += 5

    
#     if speed > 4:
#         if x % int(1/deceleration) == 0:
#             speed -= 1
#             sky.change_speed(speed)

    
#     pygame.display.flip()
#     elapsed = time.time()-now
#     if elapsed < cycle_time:
#         time.sleep(cycle_time-elapsed)