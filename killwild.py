import pygame
import random
import math
from pygame import mixer
#intializing pygame
pygame.init()

#making the screen
screen = pygame.display.set_mode((800, 600))

#background
background=pygame.image.load("background.png")

#background music
mixer.music.load("background music.mp3")
mixer.music.play(-1)

#title and icon 
pygame.display.set_caption("wild kill")
icon=pygame.image.load("angry.png")
pygame.display.set_icon(icon)

#player 
playerImg=pygame.image.load('angry.png')
playerX=3702
playerY= 480
playerY_change=0
playerX_change=0

score= 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# score
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score1 = font.render("Score : " + str(score), True, (0, 255, 0))
    screen.blit(score1, (x, y))



def player(x,y):
    screen.blit(playerImg, (x,y))

#enemy
enemyImg=pygame.image.load('death.png')
enemyX=random.randint(0,800)
enemyY=random.randint(50,150)
enemyX_change=0
enemyY_change=3
def enemy(x,y):
    screen.blit(enemyImg, (x,y))
  
def iscollision(enemyX,enemyY,playerX,playerY):
    distance=math.sqrt((math.pow(enemyX-playerX,2))+(math.pow(enemyY-playerY,2)))
    if distance<27:
        return True
    else:
        return False

#GAME LOOP [infinite loop] 
running=True
 
while running:
    screen.fill((0,0,0))
    #background image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        #Intergrating key strokes
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                playerY_change=-8
                
            if event.key==pygame.K_DOWN:
                playerY_change=8
                
            if event.key==pygame.K_LEFT:
                playerX_change=-8
                
            if event.key==pygame.K_RIGHT:
                playerX_change=8
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                playerX_change=0
                playerY_change=0  

    
    playerY+=playerY_change
    playerX+=playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    if playerY<=0:
        playerY=0
    elif playerY>=536:
        playerY=536

    enemyY+=enemyY_change
    if enemyY>=536:
        while score>0:
            score-=1
            break
        enemyY=00
        

    collision=iscollision(enemyX,enemyY,playerX,playerY)
    if collision:
        score+=1
        eat_sound=mixer.Sound("laser.wav")
        eat_sound.play()
        enemyX=random.randint(0,700)
        enemyY=random.randint(50,150)
    
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    show_score(textX,textY)
    pygame.display.update()