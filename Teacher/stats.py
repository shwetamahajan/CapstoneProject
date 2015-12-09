#Has placeholder data
#Exit not working
#Figuring out how to change text size for individual lines (the start button, Class Stat header)

#teacher app interface
import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (200,0,0)
light_red = (255,0,0)
cqorange = (254,197,2)
cqblue = (60,129,248)

screen_width=1024
screen_height=768

Exit = False

Pet = False

screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(white)
pygame.display.update()

#Logo
Logo = pygame.image.load("LogoImg.png")
newLogo = pygame.transform.scale(Logo, (200,175))
CQ = pygame.image.load("CQ.png")
newCQ = pygame.transform.scale(CQ, (500,300))

pygame.display.set_caption('Class Quest- Teacher Edition')


smallfont = pygame.font.SysFont(None, 25)
medfont = pygame.font.SysFont(None, 50)
largefont = pygame.font.SysFont(None, 85)

def text_objects(text, color,size):

    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    screen.blit(textSurf, textRect)

#use for headers
def message_to_screen(msg,color, y_displace = 0, size = "medium"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(screen_width / 2), int(screen_height / 2)+y_displace)
    screen.blit(textSurf, textRect)

#use for text
def screen_text(msg,color,pos_x, pos_y, size = 'small'):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = pos_x, pos_y
    screen.blit(textSurf, textRect)

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(screen, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "menu":
                menu_screen()

            if action == "question":
                pass

    else:
        pygame.draw.rect(screen, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)

def menu_screen():
    menu = True

    while menu:
        for event in pygame.event.get():
            screen.fill(white)
            button("Stats", 0,200,screen_width/2,50, cqblue, cqblue, action="None")
            button("Questions", screen_width/2,200,screen_width/2,50, cqorange, cqblue, action="question")

#student section headers
            screen_text("Student", red, 350,280, "small")
            screen_text("Pet LVL", red, 500,280, "small")
            screen_text("Pet EXP", red, 600,280, "small")
            screen_text("Pet :)", red, 700,280, "small")
            screen_text("Reward History", red, 900,280, "small")

#student name items
            screen_text("Fred", black, 350,350, "small")
            screen_text("Bob", black, 350,400, "small")
            screen_text("Sarah", black, 350,450, "small")
            screen_text("Ashley", black, 350,500, "small")
            screen_text("Kait", black, 350,550, "small")
            screen_text("Mike", black, 350,600, "small")

#student pet level
            screen_text("5", black, 500,350, "small")
            screen_text("1", black, 500,400, "small")
            screen_text("2", black, 500,450, "small")
            screen_text("3", black, 500,500, "small")
            screen_text("2", black, 500,550, "small")
            screen_text("4", black, 500,600, "small")
            
#student pet experience
            screen_text("85%", black, 600,350, "small")
            screen_text("10%", black, 600,400, "small")
            screen_text("25%", black, 600,450, "small")
            screen_text("55%", black, 600,500, "small")
            screen_text("75%", black, 600,550, "small")
            screen_text("0%", black, 600,600, "small")

#student pet happiness
            screen_text("happy", black, 700,350, "small")
            screen_text("sad", black, 700,400, "small")
            screen_text("so so", black, 700,450, "small")
            screen_text("fair", black, 700,500, "small")
            screen_text("content", black, 700,550, "small")
            screen_text("extremely sad", black, 700,600, "small")

#student reward history
            screen_text("daily", black, 900,350, "small")
            screen_text("rare", black, 900,400, "small")
            screen_text("sometimes", black, 900,450, "small")
            screen_text("frequent", black, 900,500, "small")
            screen_text("often", black, 900,550, "small")
            screen_text("never", black, 900,600, "small")

#stat values
            participation_val="70%"
            correct_val="80%"
            avg_val="60%"
            best_stud="Fred"
            worst_stud="Bob"
            unhealthy_pet="Jane"
#stat headers
            screen_text("Class Stats", black, 150, 280)

            screen_text("Participation: ", black, 150, 350)
            screen_text(participation_val, black, 150, 380)
            screen_text("Avg % in Categories:", black, 150, 400)
            screen_text(avg_val, black, 150, 430)
            screen_text("Correctness: ", black, 150, 450)
            screen_text(correct_val, black, 150, 480)
            screen_text("Student with Best %: ", black, 150, 500)
            screen_text(best_stud, black, 150, 530)
            screen_text("Student with Worst %: ", black, 150, 550)
            screen_text(worst_stud, black, 150, 580)
            screen_text("Unhealthy Pets: ", black, 150,600)
            screen_text(unhealthy_pet, black, 150, 630)


            pygame.display.update()
#menu_screen()

def welcome_screen():

    intro = True
    while intro:
        for event in pygame.event.get():

            message_to_screen("Press Start!", black, 100)

            button("Start", 250,600,500,100, cqorange, cqblue, action="menu")
            pygame.display.update()

welcome_screen()


#Exit doesnt work

while not Exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


pygame.quit()
quit()
