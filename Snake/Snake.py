import pygame
import random
import time
from pygame.locals import *

pygame.init()
#width and height of screen
width=400
height=400
grid_size=20
food=(0,0)
mouv=(1,0)
cell_size=width//grid_size
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
butFont = pygame.font.SysFont('comicsans',60)

snake=[(grid_size//2-2, grid_size//2),(grid_size//2-1, grid_size//2),(grid_size//2, grid_size//2)]

def create_food():
    x=random.randint(0,grid_size-1)
    y=random.randint(0,grid_size-1)
    return (x,y)

def draw_snake(pos):
    pygame.draw.rect(screen, (50,255,50), (pos[0]*cell_size, pos[1]*cell_size, cell_size-1, cell_size-1))

def draw_food(food):
    pygame.draw.rect(screen, (255,0,0), (food[0]*cell_size, food[1]*cell_size, cell_size, cell_size))

def draw():
    for i in range(grid_size):
        for j in range(grid_size):
            pygame.draw.rect(screen, (175,175,175), (i*cell_size, j*cell_size, cell_size, cell_size),1)
    for i in snake:
        draw_snake(i)
    draw_food(food)

def move_snake(mvt):
    tmp=snake[-1]
    if(snake[-1][0]+mvt[0]>=grid_size):
        snake[-1] = (0, snake[-1][1]+mvt[1])
    elif(snake[-1][0]+mvt[0]<0):
        snake[-1] = (grid_size-1, snake[-1][1]+mvt[1])
    elif(snake[-1][1]+mvt[1]>=grid_size):
        snake[-1] = (snake[-1][0]+mvt[0], 0)
    elif(snake[-1][1]+mvt[1]<0):
        snake[-1] = (snake[-1][0]+mvt[0], grid_size-1)
    else:
        snake[-1] = (snake[-1][0]+mvt[0], snake[-1][1]+mvt[1])
    for i in range(len(snake)-2,-1,-1):
        tmp2=snake[i]
        snake[i]=tmp
        tmp=tmp2

def loose(mvt):
    for i in range(len(snake)-1):
        if(snake[-1][0]+mvt[0], snake[-1][1]+mvt[1])==snake[i]:
            return True
    return False

def eat_food(pos):
    if(snake[-1]==pos):
        snake.insert(0,pos)
        return create_food()

def user_input():
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    return (-1,0)
                elif event.key == pygame.K_RIGHT:
                    return (1,0)
                elif event.key == pygame.K_UP:
                    return (0,-1)
                elif event.key == pygame.K_DOWN:
                    return (0,1)
                else:
                    return True
            elif event.type == QUIT:
                return False

while(True):
    clock.tick(10)
    mvt=user_input()
    if(mvt==False):
        break
    elif(mvt!=None and mvt!=True and (abs(mvt[0])!=abs(mouv[0]) or mouv==(0,0))):
        mouv=mvt
    if(loose(mouv) and mouv!=(0,0)):
        mouv=(0,0)
        snake=snake[len(snake)-3:]
        img = butFont.render("You lost !", True, (255,255,255))
        sizeOfImg=butFont.size("You lost !")
        screen.blit(img, ((width-sizeOfImg[0])//2, (height-sizeOfImg[1])//2))
        pygame.display.flip()
        us=user_input()
        while(us!=True and us != False):
            us=user_input()
        if(us==False):
            break

    move_snake(mouv)
    eaten=eat_food(food)
    if(eaten):
        food=eaten
    screen.fill((0,0,0))
    draw()
    pygame.display.flip()


pygame.quit()