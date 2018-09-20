# This  code is about calculator by PyGame for calculate
# This is second version
# for subject Software development and practice I
# Code by 6001012630021  Chanakan  Thimkham
# Ref. of my code :
#     Module : https://www.pygame.org/docs/ 
#     Change button color : https://bit.ly/2p3bSUI 

# Github : https://github.com/Chalol/Pygame-calculator
# my blog about Pygame calculator : https://bit.ly/2MjUXGU 
import pygame, sys
from pygame.locals import *
from Button import *

pygame.init()                                    # initialize pygame
#color
colormbred = (208,23,42)
coloryellow = (255,191,23)
colormbblue = (178,232,232)
colormbgreen = (90,224,58)
colorsofty = (255,248,183)
colorwhite = (255,255,255)
colorblack = (0,0,0)

DISP = pygame.display.set_mode((350,475))        #set width and height of display
pygame.display.set_caption('PYGAME Calculator')
fontText = pygame.font.SysFont('Arial',30)       #set font and font size that will show on screen
sound_button = pygame.mixer.Sound('beep.wav')
DISP.fill(colorblack)                            #set screen color
width = 80
height = 60

# set x,y,width,height,color and text on each button
num0 = buttonnum(95,410,width,height,(colormbred),'0')
num1 = buttonnum(10,345,width,height,(colormbred),'1')
num2 = buttonnum(95,345,width,height,(colormbred),'2')
num3 = buttonnum(180,345,width,height,(colormbred),'3')
num4 = buttonnum(10,280,width,height,(colormbred),'4')
num5 = buttonnum(95,280,width,height,(colormbred),'5')
num6 = buttonnum(180,280,width,height,(colormbred),'6')
num7 = buttonnum(10,215,width,height,(colormbred),'7')
num8 = buttonnum(95,215,width,height,(colormbred),'8')
num9 = buttonnum(180,215,width,height,(colormbred),'9')

sym_sum = buttonnum(10,150,width,height,(colormbgreen),'+')
sym_mi = buttonnum(95,150,width,height,(colormbgreen),'-')
sym_mul = buttonnum(180,150,width,height,(colormbgreen),'*')
sym_div = buttonnum(265,150,width,height,(colormbgreen),'/')
sym_clear = buttonnum(265,280,width,height,(colormbgreen),'C')
sym_dot = buttonnum(265,345,width,height,(colormbgreen),'•')
sym_open = buttonnum(10,410,width,height,(colormbgreen),'(')
sym_close = buttonnum(180,410,width,height,(colormbgreen),')')
sym_del = buttonnum(265,215,width,height,(colormbgreen),'Del')

ans = buttonnum(265,410,width,height,(coloryellow),'=')

def cal_loop():
    ty = True
    Num = " "
    while ty:
        # set button change color
        num0.btnum()
        num1.btnum()
        num2.btnum()
        num3.btnum()
        num4.btnum()
        num5.btnum()
        num6.btnum()
        num7.btnum()
        num8.btnum()
        num9.btnum()

        sym_sum.btsym()
        sym_mi.btsym()
        sym_mul.btsym()
        sym_div.btsym()
        sym_clear.btsym()
        sym_dot.btsym()
        sym_open.btsym()
        sym_close.btsym()
        sym_del.btsym()

        ans.btans()
  
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                ty = False
        
            if e.type == pygame.KEYDOWN:               # Keyboard input
                if e.key == K_0:                       # put 0 on keyboard then show 0
                    Num += '0'
                if e.key == K_1:                       # put 1 on keyboard then show 1
                    Num += '1'
                if e.key == K_2:                       # put 2 on keyboard then show 2
                    Num += '2'
                if e.key == K_3:                       # put 3 on keyboard then show 3
                    Num += '3'
                if e.key == K_4:                       # put 4 on keyboard then show 4
                    Num += '4'
                if e.key == K_5:                       # put 5 on keyboard then show 5
                    Num += '5'
                if e.key == K_6:                       # put 6 on keyboard then show 6
                    Num += '6'
                if e.key == K_7:                       # put 7 on keyboard then show 7
                    Num += '7'
                if e.key == K_8:                       # put 8 on keyboard then show 8
                    Num += '8'
                if e.key == K_9:                       # put 9 on keyboard then show 9
                    Num += '9'
                if e.key == K_EQUALS:                  # put + on keyboard then show +
                    Num += '+'
                if e.key == K_MINUS:                   # put - on keyboard then show -
                    Num += '-'
                if e.key == K_RSHIFT:                  # put shift on keyboard then show *
                    Num += '*'
                if e.key == K_SLASH:                   # put / on keyboard then show /
                    Num += '/'
                if e.key == K_PERIOD:                  # put . on keyboard then show .
                    Num += '.'
                if e.key == K_z:                       # put z on keyboard then show (
                    Num += '('
                if e.key == K_x:                       # put x on keyboard then show )
                    Num += ')'
                if e.key == K_DELETE:                  # put delete on keyboard for delete
                    Num = Num[:-1]
                if e.key == K_SPACE:                   # put space bar on keyboard for show answer
                    if Num == ' ':                     # if Num is blank then pass
                        pass
                    elif Num[-1] == '+' or Num[-1] == '-' or Num[-1] == '*' or Num[-1] == '/': # if the last one is operand then show error
                        try:
                            Num = eval(Num)
                        except:
                            Num = "Error the last one"
                    elif '/0' in Num:                  # if divide by zero then show error
                        Num = "Can't divide by 0"
                    elif '++' in Num or '--' in Num or'**' in Num or '//' in Num: #if has operand more than 1 then show error
                        Num = 'operation Error'
                    else:
                        Num = str(eval(Num))
                # Show input and answer on screen
                show = fontText.render(str(Num), True,colorblack)                   
                DISP.blit(show, (20,55))



            if e.type == pygame.MOUSEBUTTONDOWN:          # Mouse click input
                mouse = pygame.mouse.get_pos()            # get mouse position
                # test if a point is inside a rectangle
                if num0.finalbut().collidepoint(mouse):   # if click on button 0 then show 0
                    Num += '0'
                if num1.finalbut().collidepoint(mouse):   # if click on button 1 then show 1
                    Num += '1'
                if num2.finalbut().collidepoint(mouse):   # if click on button 2 then show 2
                    Num += '2'
                if num3.finalbut().collidepoint(mouse):   # if click on button 3 then show 3
                    Num += '3'
                if num4.finalbut().collidepoint(mouse):   # if click on button 4 then show 4
                    Num += '4'
                if num5.finalbut().collidepoint(mouse):   # if click on button 5 then show 5
                    Num += '5'
                if num6.finalbut().collidepoint(mouse):   # if click on button 6 then show 6
                    Num += '6'
                if num7.finalbut().collidepoint(mouse):   # if click on button 7 then show 7
                    Num += '7'
                if num8.finalbut().collidepoint(mouse):   # if click on button 8 then show 8
                    Num += '8'
                if num9.finalbut().collidepoint(mouse):   # if click on button 9 then show 9
                    Num += '9'
                if sym_sum.finalbut().collidepoint(mouse):  # if click on button + then show +
                    Num += '+'
                if sym_mi.finalbut().collidepoint(mouse):   # if click on button - then show -
                    Num += '-'
                if sym_mul.finalbut().collidepoint(mouse):  # if click on button * then show *
                    Num += '*'
                if sym_div.finalbut().collidepoint(mouse):  # if click on button / then show /
                    Num += '/'
                if sym_dot.finalbut().collidepoint(mouse):  # if click on button . then show .
                    Num += '.'
                if sym_open.finalbut().collidepoint(mouse): # if click on button ( then show (
                    Num += '('
                if sym_close.finalbut().collidepoint(mouse): # if click on button ) then show )
                    Num += ')'
                if sym_clear.finalbut().collidepoint(mouse): # if click on button C then show nothing
                    Num = ' '
                if sym_del.finalbut().collidepoint(mouse):   # if click on button Del then show delete
                    Num = Num[:-1]
                if ans.finalbut().collidepoint(mouse):       # if click on button = then show answer
                    if Num == ' ':                           # if Num is blank then pass
                        pass
                    elif Num[-1] == '+' or Num[-1] == '-' or Num[-1] == '*' or Num[-1] == '/':  # if the last one is operand then show error
                        try:
                            Num = eval(Num)
                        except:
                            Num = "Error at the last one"
                    elif '/0' in Num:                        # if divide by zero then show error
                        Num = "Can't divide by 0"
                    elif '++' in Num or '--' in Num or'**' in Num or '//' in Num:   #if has operand more than 1 then show error
                        Num = 'operation Error'
                    else:
                        Num = str(eval(Num))
                sound_button.play()

            # text not out of the screen    
            if len(Num) >= 22: 
                Num = Num[:-1]
                    
            pygame.draw.rect(DISP,colorsofty,(10,30,330,90))
            show = fontText.render(str(Num), True,colorblack)              
            DISP.blit(show, (20,55))

        pygame.display.update()            # Update portions of the screen

cal_loop()                                 # call function to run programme
pygame.quit()                              # uninitialize all pygame modules
quit()
