import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

pygame.display.set_caption('Slither') #sets title of game
icon = pygame.image.load("apple.png")
pygame.display.set_icon(icon)

button = pygame.image.load('back.png')
play = pygame.image.load('play.png')
img = pygame.image.load('snakehead.png')
appleImg = pygame.image.load('apple.png')

appleSpeed = 10

block_size = 30
block_speed = 20
appleThickness = 30
FPS = 24

direction = "up"

smallFont = pygame.font.SysFont("comicsansms", 25) #font size 25
medFont = pygame.font.SysFont("comicsansms", 50)
largeFont = pygame.font.SysFont("comicsansms", 80)

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
    randAppleY = 50
    return randAppleX,randAppleY
def gameIntro():
    intro = True
    while intro:
        
        pos = pygame.mouse.get_pos()
        b = gameDisplay.blit(button, (300, 200))
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if b.collidepoint(pos):
                    pygame.quit()
                    quit()
                else:
                    intro = False

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        message_to_screen("Catch as Much Food as you Can!", green, -100, "small")
        message_to_screen("Move left and right", black, +10, "small")
        message_to_screen("Good Luck!", black, +60, "small")
        message_to_screen("Click to Start!", black, +110, "small")
        pygame.display.update()
        clock.tick(15)
        

def snake(block_size, snakelist):
    head = img
    gameDisplay.blit(head,(snakelist[-1][0], snakelist[-1][1]))
    
def text_objects(text,color,size):
    if size == "small":
        textSurface = smallFont.render(text,True,color)
    if size == "medium":
        textSurface = medFont.render(text,True,color)
    if size == "large":
        textSurface = largeFont.render(text,True,color)
        
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color, y_displace=0, size = "small"):

    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width/2), (display_height/2+y_displace)
    gameDisplay.blit(textSurf, textRect)
def gameLoop():

    global direction
    direction = "up"
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height-100
    lead_a = 50
    lead_x_change = 0
    lead_y_change = 0
    lead_a_change = 10
    pointNum = 0

    goRight = True
    
    snakeList = []
    snakeLength = 1
    
    randAppleX,randAppleY = randAppleGen()
    while not gameExit:

        while gameOver == True:
            pos = pygame.mouse.get_pos()
            gameDisplay.fill(white)
            #message_to_screen("Game over", red, -50, size="large")
            message_to_screen("You Caught "+str(pointNum)+" Food!",black, 50, size="medium")
            a = gameDisplay.blit(play, (display_width/2, display_height-200))
            b = gameDisplay.blit(button, (0, 0))
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if b.collidepoint(pos):
                        gameExit = True
                        gameOver = False
                    elif a.collidepoint(pos):
                        gameLoop()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
        if lead_x >= display_width:
            lead_x = 0
        elif lead_x <= 0:
            lead_x = display_width

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if goRight == True:
                    goRight = False
                    direction = "left"
                    lead_x_change = -block_speed
                    lead_y_change = 0
                elif goRight == False:
                    goRight = True
                    direction = "right"
                    lead_x_change = block_speed
                    lead_y_change = 0
                    
##            if event.type == pygame.KEYDOWN:
##                if event.key == pygame.K_LEFT:
##                    direction = "left"
##                    lead_x_change = -block_size
##                    lead_y_change = 0
##                elif event.key == pygame.K_RIGHT:
##                    direction = "right"
##                    lead_x_change = block_size
##                    lead_y_change = 0
            
                
            if lead_y >= display_height or lead_y <= 0: #bounds
                gameOver = True
        
        if pointNum >= 5: #limit of catches
            gameOver = True
                
        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(white)
        
        message_to_screen(str(pointNum), black, -200, "large")

        gameDisplay.blit(appleImg, (randAppleX,lead_a))
        lead_a_change = 10
        lead_a += lead_a_change

        if lead_a >= display_height:
            randAppleX,lead_a = randAppleGen()
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)  
        snake(block_size, snakeList)     
        pygame.display.update()

        if lead_x > randAppleX and lead_x < randAppleX+appleThickness or lead_x+block_size > randAppleX and lead_x+block_size < randAppleX+appleThickness:
            if lead_y > lead_a and lead_y < lead_a+appleThickness or lead_y+block_size > lead_a and lead_y+block_size < lead_a+appleThickness:
                randAppleX,lead_a = randAppleGen()
                pointNum += 1
        
            
        clock.tick(FPS)

    pygame.quit()
    quit

gameIntro()
gameLoop()
