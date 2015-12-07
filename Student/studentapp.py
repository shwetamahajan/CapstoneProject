#student app interface
import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (200,0,0)
light_red = (255,0,0)
cqorange = (254,197,2)
cqblue = (60,129,248)

screen_width=800
screen_height=400

Exit = False

Pet = False

screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(white)
pygame.display.update()

pygame.display.set_caption('Class Quest')

smallfont = pygame.font.SysFont(None, 25)
medfont = pygame.font.SysFont(None, 50)
largefont = pygame.font.SysFont(None, 85)

def text_objects(text, color,size = "medium"):
    
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "medium"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    screen.blit(textSurf, textRect)
   
def message_to_screen(msg,color, y_displace = 0, size = "medium"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(screen_width / 2), int(screen_height / 2)+y_displace)
    screen.blit(textSurf, textRect)

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(screen, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "home":
                home_screen()

            if action == "create":
                create_pet()

            if action == "confirm":
                confirm_pet()

            
    else:
        pygame.draw.rect(screen, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)

#Functions

#Home Page
def home_screen():
    screen.fill(white)
    home = True
    while home:
        for event in pygame.event.get():

            message_to_screen("Hi User!", black, -150)            

            button("Pet", 200,100,150,150, cqorange, cqblue, action="None")
            button("Answer", 450,100,150,150, cqorange, cqblue, action="None")
            button("Menu", 50,250,100,100, cqorange, cqblue, action="home")
            button("Bag", 650,250,100,100, cqorange, cqblue, action="None")
            pygame.display.update()
            
#home_screen()

#Pet Accept

def confirm_pet():
    screen.fill(white)
    Question = True

    while Question:
        for event in pygame.event.get():
            message_to_screen("Are you sure", black, -180)
            message_to_screen("you want this companion?", black, -150)
            button("Yes", 100,100,250,250, cqorange, cqblue, action="home")
            button("No", 450,100,250,250, cqorange, cqblue, action="create")
            pygame.display.update()

#confirm_pet()

#Create Pet

def create_pet():
    screen.fill(white)
    Pet = True
    #print("Start loop")
    while Pet:
        for event in pygame.event.get():
            message_to_screen("Meet your new friend!!", black, -150)  
            button("Human", 50,100,200,250, cqorange, cqblue, action="confirm")
            button("Creature", 300,100,200,250, cqorange, cqblue, action="confirm")
            button("Animal", 550,100,200,250, cqorange, cqblue, action="confirm")
            pygame.display.update()

#create_pet()


def welcome_screen():

    intro = True
    while intro:
        for event in pygame.event.get():

            message_to_screen("Press Start!", black)            

            button("Start", 250,250,300,50, cqorange, cqblue, action="create")
            pygame.display.update()

welcome_screen()


#Exit the game

while not Exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()



pygame.quit()
quit()
