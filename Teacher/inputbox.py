# by Timothy Downs, inputbox written for my map editor

# This program needs a little cleaning up
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message, x_pos, y_pos):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (254,197,2),
                   ((screen.get_width() / 2) + x_pos,
                    (screen.get_height() / 2) + y_pos,
                    200,20), 0)
  pygame.draw.rect(screen, (60,129,248),
                   ((screen.get_width() / 2) + x_pos-2,
                    (screen.get_height() / 2) + y_pos-2,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (0,0,0)),
                ((screen.get_width() / 2) + x_pos, (screen.get_height() / 2) + y_pos))
  pygame.display.flip()

def ask(screen, question, x_posz, y_posz):
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + "".join(current_string), x_posz, y_posz)
  while True:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey <= 127:
      if pygame.key.get_mods() & KMOD_SHIFT or  pygame.key.get_mods() & KMOD_CAPS: # if shift is pressed  or caps is on
        if inkey == K_BACKQUOTE:
          current_string.append("~")
        elif inkey == K_MINUS:
          current_string.append("_")
        elif inkey == K_EQUALS:
          current_string.append("+")
        elif inkey == K_LEFTBRACKET:
          current_string.append("{")
        elif inkey == K_RIGHTBRACKET:
          current_string.append("}")
        elif inkey == K_BACKSLASH:
          current_string.append("|")
        elif inkey == K_SEMICOLON:
          current_string.append(":")
        elif inkey == K_QUOTE:
          current_string.append('"')
        elif inkey == K_COMMA:
          current_string.append("<")
        elif inkey == K_PERIOD:
          current_string.append(">")
        elif inkey == K_SLASH:
          current_string.append("?")
        elif inkey == K_0:
          current_string.append(")")
        elif inkey == K_1:
          current_string.append("!")
        elif inkey == K_2:
          current_string.append("@")
        elif inkey == K_3:
          current_string.append("#")
        elif inkey == K_4:
          current_string.append("$")
        elif inkey == K_5:
          current_string.append("%")
        elif inkey == K_6:
          current_string.append("^")
        elif inkey == K_7:
          current_string.append("&")
        elif inkey == K_8:
          current_string.append("*")
        elif inkey == K_9:
          current_string.append("(")
        else:
          current_string.append(chr(inkey).upper()) 
      else:
        current_string.append(chr(inkey))
        
    display_box(screen, question + ": " + "".join(current_string),x_posz,y_posz)
  return "".join(current_string)

if __name__ == '__main__': main()
