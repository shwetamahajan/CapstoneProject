import pygame
import inputbox
import time
pygame.init()

# Colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
cqorange = (254,197,2)
cqblue = (60,129,248)

# Font Sizes
Sfont = pygame.font.SysFont("comicsansms", 25)
Mfont = pygame.font.SysFont("comicsansms", 45)
Lfont = pygame.font.SysFont("comicsansms", 55)

# Screen Size
display_w = 1024 
display_h = 768

#Button Size
rect_w = 325
rect_h = 200
pos_x = 50
pos_y = 100

# Default Display Stuff
Display = pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption("Teacher’s Side")
Display.fill(white)
pygame.display.update()

#Logo
Logo = pygame.image.load("LogoImg.png")
newLogo = pygame.transform.scale(Logo, (200,175))
CQ = pygame.image.load("CQ.png")
newCQ = pygame.transform.scale(CQ, (500,300))

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = Mfont):
    color = black
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    Display.blit(textSurf, textRect)

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(Display, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "Stats":
<<<<<<< HEAD
                __import__('stats')
=======
                pass
>>>>>>> origin/master
            elif action == "Send":
                main()
    else:
        pygame.draw.rect(Display, inactive_color, (x,y,width,height))
    text_to_button(text, black, x, y, width, height, size = Mfont)

def text_objects(text,color,fontSize):
    if fontSize == Sfont:
        textSurf = Sfont.render(text,True,color)
    elif fontSize == Mfont:
        textSurf = Mfont.render(text,True,color)
    elif fontSize == Lfont:
        textSurf = Lfont.render(text,True,color)
    return textSurf, textSurf.get_rect()

def screen_text(msg,color,pos_x, pos_y, fontSize = Mfont):
    textSurf, textRect = text_objects(msg,color,fontSize)
    textRect.center = pos_x, pos_y
    Display.blit(textSurf, textRect)

def main():

    inmain = True

    i = 0;
    clock = pygame.time.Clock()
    Display.fill(white)
    Display.blit(newLogo, (0,10))   

    Display.blit(newLogo, (800,10))
    Display.blit(newCQ, (250,-50))

    while inmain:
        for event in pygame.event.get():
            button("Stats",0,200,display_w/2, 50, cqorange, cqblue, "Stats")
            button("Question",display_w/2,200,display_w/2, 50, cqblue, cqblue, "Question")
            while i < 7:
                inp = inputbox.ask(Display, 'Question',-100, -50)
                i = 1
                inp = inputbox.ask(Display, 'A)',-100, -10)
                i = 2
                inp = inputbox.ask(Display, 'B)',-100, 20)
                i = 3
                inp = inputbox.ask(Display, 'C)',-100, 50)
                i = 4
                inp = inputbox.ask(Display, 'D)',-100, 80)
                i = 5
                inp = inputbox.ask(Display, 'Exp Reward',-100, 110)
                i = 6
                inp = inputbox.ask(Display, 'Money Reward',-100, 140)
                i = 7
            button("Send",display_w/4,600,display_w/2, 50, cqorange, cqblue, "Send")
            pygame.display.flip()
            
    pygame.display.update()
    clock.tick(20)

main()
