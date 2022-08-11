import pygame, sys, time, random
from pygame.constants import K_SPACE, K_w, K_a, K_s, K_d
pygame.init()

size = width, height =  800, 800
cycle_time = 0.05

screen = pygame.display.set_mode(size)

class Sky:
    def __init__(self, pixel_size, colors):
        self.grid = []
        self.pixel_size = pixel_size
        self.color1, self.color2 = colors[0], colors[1]
        for i in range(int(height/pixel_size)):
            row = []
            for i in range(int(width/pixel_size)):
                row.append(random.choice([0, 1]))
            self.grid.append(row)
    def new_row(self):
        prev = self.grid[6]
        # row = prev
        # for bit in row:
        #     if bit == 1: bit = 0
        #     elif bit ==0: bit = 1
        print("prev",prev)
        row = prev
        threshold = []
        for n in range(len(prev)):

            if n == 0:  #it is the first pixel
                if prev[1] == prev[0]: threshold.append(75) #if the next one is the same
                else: threshold.append(25)
            
            elif n== len(prev)-1: # it is the last pixel
                if prev[-2]==prev[-1]: threshold.append(75) #if the previos is the same
                else: threshold.append(25)

            else: 
                if prev[n-1]==prev[n] and prev[n+1]==prev[n]: #neighbors are both the same
                    threshold.append(100)
                elif prev[n-1] == prev[n] or prev[n+1] == prev[n]: #just one neighbor is the same
                    threshold.append(50)
                else: threshold.append(10) #neither are the same
        #print(threshold)
        
        for i in range(len(threshold)):
            if random.randint(1, 100) > threshold[i]: #row bit needs to change
                if row[i] ==0: row[i] = 1
                elif row[i] ==1: row[i] = 0
                
        print("new row", row[0:8])
        return(row)

        

        

        pass
    def move(self):
        for i in range(6):
            print(self.grid[i][0:5])
        for i in range(2): print(" ")
        # new_grid = [[]]
        # for i in range(len(self.grid)-1):
        #     new_grid.append(self.grid[i])
        
        # new_grid = self.grid[0:-1]
        # new_grid.insert(0, self.new_row(self.grid[0]))
        


        
        # #new_grid[0] = self.new_row(new_grid[1])
        # self.grid = new_grid

        self.grid.insert(0, self.new_row())
        #self.grid = self.grid[0:-1]
        

    def draw(self):
        for row in range(len(self.grid)):
            for pixel in range(len(self.grid[row])):
                pygame.draw.rect(screen, colors[self.grid[row][pixel]], pygame.Rect(pixel*self.pixel_size, row*self.pixel_size, self.pixel_size, self.pixel_size))


 
colors = {
    0 :(220, 220, 255),
    1 :(100, 100, 255)
}

sky = Sky(10, colors)

x = 0
while 1:
    x+=1
    now = time.time()
    screen.fill((160, 160, 160))
    keys=pygame.key.get_pressed()
    if keys[K_SPACE]:
        quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
 
    
    sky.move()
    sky.draw()
    
    pygame.display.flip()
    elapsed = time.time()-now
    if elapsed < cycle_time:
        time.sleep(cycle_time-elapsed)
 
