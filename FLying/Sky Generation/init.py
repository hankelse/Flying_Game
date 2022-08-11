import pygame, sys, time, random
from pygame.constants import K_SPACE, K_w, K_a, K_s, K_d
pygame.init()

size = width, height =  800, 800
cycle_time = 0.1

screen = pygame.display.set_mode(size)

class Sky:
    def __init__(self, pixel_size, colors):
        self.grid = []
        self.pixel_size = pixel_size
        self.color1, self.color2 = colors["1"], colors["2"]
        for i in range(int(height/pixel_size)):
            row = []
            for i in range(int(width/pixel_size)):
                row.append(random.choice([self.color1, self.color2]))
            self.grid.append(row)
    def new_row(self, grid):
        row = []

        prev = grid[1]
        for i in range(10): print(" ")
        print(prev)
        print(len(prev))
        for i in range(10): print(" ")

        row_info = {}
        for i in range(int(width/self.pixel_size)):
            row_info[str(i)] = [50]
        
        
    
        for i in range(len(row_info)):
            #print(i, row_info)
            if i == 0:
                #print(prev)
                if prev[i] == prev[i+1]:
                    row_info[str(i)][0] += 25
                    #print(row_info)
            elif i == int(width/self.pixel_size)-1:
                if prev[i] == prev[i-1]:
                    row_info[str(i)][0] += 25
                    pass
            else:
                print(i, print(len(prev)))
                if prev[i] == prev[i+1] and prev[i-1] == prev[i]:
                    row_info[str(i)][0] += 25
                elif prev[i] == prev[i+1] and prev[i-1] == prev[i]:
                    row_info[str(i)][0] += 10
            
        for i in range(len(row_info)):
            if random.randint(1, 100) < row_info[str(i)][0]:
                row.append(prev[i])
            else:
                if prev[i] == 1: row.append(0)
                elif prev[i] == 0: row.append(1)
        return(row)



        # #get decisions
        # for i in range(int(width/self.pixel_size)):
        #     if random.randint(1, 100) < thresholds[i]: decisions.append("same")
        #     else: decisions.append("change")

        # #decisions enforcement
        # for i in range(len(row)):
        #     if decisions[i] == "same": row[i] = prev[i]
        #     else:
        #         if prev[i]== self.color1:row[i] = self.color2
        #         elif prev[i]== self.color2: row[i] = self.color1
        #         #row.append(random.choice([self.color1, self.color2]))
        # return(row)
    def move(self):
        new_grid = [[]]
        for n in range(1, len(self.grid)):
            new_grid.append(self.grid[n-1])
        new_grid[0] = self.new_row(new_grid)
        self.grid = new_grid
    def draw(self):
        for row in range(len(self.grid)):
            for pixel in range(len(self.grid[row])):
                pygame.draw.rect(screen, self.grid[row][pixel], pygame.Rect(pixel*self.pixel_size, row*self.pixel_size, self.pixel_size, self.pixel_size))



colors = {
    "1":(200, 200, 255),
    "2":(100, 100, 255)
}

sky = Sky(10, colors)

while 1:
    #x+=1
    now = time.time()
    screen.fill((160, 160, 160))
    keys=pygame.key.get_pressed()
    if keys[K_SPACE]:
        quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    #
    sky.move()
    sky.draw()
    
    pygame.display.flip()
    elapsed = time.time()-now
    if elapsed < cycle_time:
        time.sleep(cycle_time-elapsed)