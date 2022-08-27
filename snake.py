import pygame as pg
import random

speed = 100 #Lower = faster

grid = (30, 30)
apple_pos = (random.randint(0, grid[0]-1), random.randint(0, grid[1]-1))
head_pos = (5, 10)
head_pos_history = []
move_dir = "r"
apples_eaten = 0

pg.init()
WINDOW = pg.display.set_mode((grid[1]*30, grid[0]*30))
pg.display.set_caption("SNAKE")
FONT = pg.font.SysFont("comicsans", 50)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def draw():
    #Grid
    WINDOW.fill(BLACK)
    for i in range(grid[0]):
        for n in range(grid[1]):
            pg.draw.rect(WINDOW, GREY, (n*30, i*30, 30, 30), 2)
    #Snake
    pg.draw.circle(WINDOW, RED, (head_pos[1]*30+15, head_pos[0]*30+15), 10)
    for i in range(apples_eaten):
        pg.draw.circle(WINDOW, BLUE, (head_pos_history[i][1]*30+15, head_pos_history[i][0]*30+15), 10)
    #Apple
    pg.draw.circle(WINDOW, GREEN, (apple_pos[1]*30+15, apple_pos[0]*30+15), 10)
    #Score
    WINDOW.blit(FONT.render(str(apples_eaten), True, WHITE), (50, 50))
    pg.display.update()

while True:
    head_pos_history.insert(0, (head_pos[0], head_pos[1]))
    #Inputs
    events = pg.event.get()
    for event in events:
        #Quit
        if event.type == pg.QUIT:
            print(apples_eaten)
            pg.quit()
            quit()
        #Arrows
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and move_dir != "d":
                move_dir = "u"
                head_pos = (head_pos[0]-1, head_pos[1])
            elif event.key == pg.K_DOWN and move_dir != "u":
                move_dir = "d"
                head_pos = (head_pos[0]+1, head_pos[1])
            elif event.key == pg.K_LEFT and move_dir != "r":
                move_dir = "l"
                head_pos = (head_pos[0], head_pos[1]-1)
            elif event.key == pg.K_RIGHT and move_dir != "l":
                move_dir = "r"
                head_pos = (head_pos[0], head_pos[1]+1)
    if head_pos[0] == head_pos_history[0][0] and head_pos[1] == head_pos_history[0][1]:
        if move_dir == "u":
            head_pos = (head_pos[0]-1, head_pos[1])
        elif move_dir == "d":
            head_pos = (head_pos[0]+1, head_pos[1])
        elif move_dir == "l":
            head_pos = (head_pos[0], head_pos[1]-1)
        elif move_dir == "r":
            head_pos = (head_pos[0], head_pos[1]+1)
    #Head crashes into snake
    for i in range(apples_eaten):
        if head_pos == head_pos_history[i]:
            print(apples_eaten)
            pg.quit()
            quit()
    #Head crashes into wall
    if head_pos[0] < 0 or head_pos[0] > grid[0]-1 or head_pos[1] < 0 or head_pos[1] > grid[1]-1:
        print(apples_eaten)
        pg.quit()
        quit()
    #Snake eats apple
    if head_pos == apple_pos:
        apples_eaten += 1
        apple_pos = (random.randint(0, grid[0]-1), random.randint(0, grid[1]-1))
            
    draw()
    pg.time.delay(speed)