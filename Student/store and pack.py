
import pygame
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
display_w = 800
display_h = 600

# Default Display Stuff
Display = pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption("VCP")
Display.fill(white)
pygame.display.update()

# Rich - Store and Pack stuff
instore = True
inpack = True
items = ["1","2","3","4"]
packitems = [False,False,False,False]
money = 100.00

# Rich - Inital positions
pos_x = 50
pos_y = 100
rect_w = 325
rect_h = 200

# Rich - Button Positions
button1 = [pos_x,pos_y,rect_w,rect_h]
button3 = [pos_x, pos_y + 250,rect_w,rect_h]
button2 = [pos_x + 375,pos_y,rect_w,rect_h]
button4 = [pos_x + 375 ,pos_y + 250 ,rect_w,rect_h]
back = [pos_x + 650, 25, 50,50]

## Images
# Teddy Bear
bear = pygame.image.load("bear.png")
newbear = pygame.transform.scale(bear, (150,150))
button1center = ((rect_w/2 - 37.5 + 10),(rect_h/2 + 37.5 - 10))
# Kendama
kendama = pygame.image.load("Kendama.png")
newkendama = pygame.transform.scale(kendama, (175,150))
button2center = ((rect_w/2 - 37.5 + 10),(250 + rect_h/2 + 37.5 - 10))
# Bricks
bricks = pygame.image.load("bricks.png")
newbricks = pygame.transform.scale(bricks, (150,150))
button3center = ((375 + rect_w/2 - 37.5 + 10),(rect_h/2 + 37.5 - 10))
# Books
books = pygame.image.load("books.png")
newbooks = pygame.transform.scale(books, (150,150))
button4center = ((375 + rect_w/2 - 37.5 + 10),(250 + rect_h/2 + 37.5 - 10))
# Backpack
backpack = pygame.image.load("backpack.png")
newbackpack = pygame.transform.scale(backpack, (50,50))
packcenter = ((pos_x + 550),(25))
# Back arrow
backarrow = pygame.image.load("backarrow.png")
newbackarrow = pygame.transform.scale(backarrow, (50,50))
backcenter = ((pos_x + 650),(25))

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = Mfont):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    Display.blit(textSurf, textRect)

def store_button(text, x, y, width, height, inactive_color, active_color, action = None):
    global money
    global pack
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(Display, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "1" and money >=10 and packitems[0] == False:
                money -= 10
##                Display.fill(white)
##                pygame.display.update()
                packitems[0] = True
            elif action == "2" and money >=20 and packitems[1] == False:
                money -= 20
                Display.fill(white)
                pygame.display.update()
                packitems[1] = True
            elif action == "3" and money >=30 and packitems[2] == False:
                money -= 30
                Display.fill(white)
                pygame.display.update()
                packitems[2] = True
            elif action == "4" and money >=40 and packitems[3] == False:
                money -= 40
                Display.fill(white)
                pygame.display.update()
                packitems[3] = True
            elif action == "Pack":
                Display.fill(white)
                pack()
            elif action == "Back":
                print("Back")
    else:
        pygame.draw.rect(Display, inactive_color, (x,y,width,height))
    
    text_to_button(text,black,x,y,width,height)
    Display.blit(newbear,button1center)
    Display.blit(newbricks,button3center)
    Display.blit(newkendama,button2center)
    Display.blit(newbooks,button4center)
    Display.blit(newbackpack,packcenter)
    Display.blit(newbackarrow,backcenter)
    
def pack_button(text, x, y, width, height, inactive_color, active_color, action = None):
    global money
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(Display, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "Back":
                Display.fill(white)
                store()
    else:
        pygame.draw.rect(Display, inactive_color, (x,y,width,height))

    Display.blit(newbackarrow,backcenter)

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

def store():

    pack = [pos_x + 625, 25, 50,50]

    while instore:
        for event in pygame.event.get():

            # Banner, wallet and back
            screen_text("Welcome to the Store!!!", black, 400, 325)
            screen_text("Money = " + repr(money), black, 200, 50)

            # The grid of buttons
            store_button("", pos_x,pos_y,rect_w,rect_h, cqorange, cqblue, action = "1" )
            store_button("", pos_x + 375,pos_y,rect_w,rect_h, cqorange, cqblue, action = "2" )
            store_button("", pos_x, pos_y + 250,rect_w,rect_h, cqorange, cqblue, action = "3" )
            store_button("", pos_x + 375 ,pos_y + 250 ,rect_w,rect_h, cqorange, cqblue, action = "4" )
            store_button("", pos_x + 650, 25, 50,50, cqorange, cqblue, action = "Back" )
            store_button("", pos_x + 550, 25, 50,50, white, white, action = "Pack" )        
            pygame.display.update()

def pack():

    # Banner, wallet and back
    screen_text("Backpack", black, 150, 50)
    screen_text("Money = " + repr(money), black, 500, 50)

    while inpack:
        for event in pygame.event.get():
            pack_button("", pos_x + 650, 25, 50,50, cqorange, cqblue, action = "Back" )
            pygame.display.update()
    
            # The grid of buttons 
            pygame.draw.rect(Display, cqorange, button1)
            pygame.draw.rect(Display, cqorange, button2)
            pygame.draw.rect(Display, cqorange, button3)
            pygame.draw.rect(Display, cqorange, button4)

            # If they bought the item, display it
            if packitems[0] == True:
                Display.blit(newbear,button1center)
            if packitems[1] == True:
                Display.blit(newbricks,button3center)
            if packitems[2] == True:
                Display.blit(newkendama,button2center)
            if packitems[3] == True:
                Display.blit(newbooks,button4center) 

    pygame.display.update()

store()
