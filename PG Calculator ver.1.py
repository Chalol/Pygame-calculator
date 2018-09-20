# This  code is about calculator by PyGame for calculate
# This is first version
# for subject Software development and practice I
# Code by 6001012630021  Chanakan  Thimkham
# Ref. of my code :
#     Module : https://www.pygame.org/docs/ 
#     Change button color : https://bit.ly/2p3bSUI 

# Github : https://github.com/Chalol/Pygame-calculator
# my blog about Pygame calculator : https://bit.ly/2MjUXGU 

import pygame, sys
from pygame.locals import *

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
logo = pygame.font.SysFont('Arial',25)
DISP.fill(colorblack)                            #set screen color
# img = pygame.image.load('Layer 2.png').convert()

#  set button color
class buttonnum():
    
    def __init__(self,x,y,width,height,color,text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        
    def btnum(self):                              #function that check mouse position and change button's color
        mouse = pygame.mouse.get_pos()
        if self.x+80 > mouse[0] > self.x and self.y+60 > mouse[1] > self.y:
            pygame.draw.rect(DISP,colorsofty,(self.x,self.y,80,60))
            DISP.blit(fontText.render(self.text,True,colorblack),(self.x+30,self.y+10))
        else:
            pygame.draw.rect(DISP,colormbred,(self.x,self.y,80,60))
            DISP.blit(fontText.render(self.text,True,colorwhite),(self.x+30,self.y+10))
            
    def btsym(self):
        mouse = pygame.mouse.get_pos()
        if self.x+80 > mouse[0] > self.x and self.y+60 > mouse[1] > self.y:
            pygame.draw.rect(DISP,colorsofty,(self.x,self.y,80,60))
            DISP.blit(fontText.render(self.text,True,colorblack),(self.x+30,self.y+10))
        else:
            pygame.draw.rect(DISP,colormbgreen,(self.x,self.y,80,60))
            DISP.blit(fontText.render(self.text,True,colorwhite),(self.x+30,self.y+10))
            
    def btans(self):
        mouse = pygame.mouse.get_pos()
        if self.x+160 > mouse[0] > self.x and self.y+250 > mouse[1] > self.y:
            pygame.draw.rect(DISP,colorsofty,(self.x,self.y,80,125))
            DISP.blit(fontText.render(self.text,True,colorblack),(self.x+30,self.y+10))
        else:
            pygame.draw.rect(DISP,coloryellow,(self.x,self.y,80,125))
            DISP.blit(fontText.render(self.text,True,colorwhite),(self.x+30,self.y+10))
            
    def finalbut(self):                        #function that will using for check x,y aka mouse position
        return pygame.draw.rect(DISP,colorsofty,(self.x,self.y,self.width,self.height))

# set x,y,width,height,color and text on each button
num0 = buttonnum(95,410,80,60,(colormbred),'0')
num1 = buttonnum(10,345,80,60,(colormbred),'1')
num2 = buttonnum(95,345,80,60,(colormbred),'2')
num3 = buttonnum(180,345,80,60,(colormbred),'3')
num4 = buttonnum(10,280,80,60,(colormbred),'4')
num5 = buttonnum(95,280,80,60,(colormbred),'5')
num6 = buttonnum(180,280,80,60,(colormbred),'6')
num7 = buttonnum(10,215,80,60,(colormbred),'7')
num8 = buttonnum(95,215,80,60,(colormbred),'8')
num9 = buttonnum(180,215,80,60,(colormbred),'9')

sym_sum = buttonnum(95,150,80,60,(colormbgreen),'+')
sym_mi = buttonnum(180,150,80,60,(colormbgreen),'-')
sym_mul = buttonnum(265,150,80,60,(colormbgreen),'*')
sym_div = buttonnum(265,215,80,60,(colormbgreen),'/')
sym_clear = buttonnum(265,280,80,60,(colormbgreen),'C')
sym_dot = buttonnum(10,410,80,60,(colormbgreen),'•')
sym_del = buttonnum(180,410,80,60,(colormbgreen),'Del')

ans = buttonnum(265,345,80,125,(coloryellow),'=')

def cal_loop():
    ty = True
    Num = " "
    while ty:
#         DISP.blit(img,(0,0))

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
        sym_del.btsym()

        ans.btans()

        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                ty = False

            if e.type == pygame.KEYDOWN:               # Keyboard input

                if e.key == K_0:
                    Num += '0'
                if e.key == K_1:
                    Num += '1'
                if e.key == K_2:
                    Num += '2'
                if e.key == K_3:
                    Num += '3'
                if e.key == K_4:
                    Num += '4'
                if e.key == K_5:
                    Num += '5'
                if e.key == K_6:
                    Num += '6'
                if e.key == K_7:
                    Num += '7'
                if e.key == K_8:
                    Num += '8'
                if e.key == K_9:
                    Num += '9'
                if e.key == K_EQUALS:
                    Num += '+'
                if e.key == K_MINUS:
                    Num += '-'
                if e.key == K_RSHIFT:
                    Num += '*'
                if e.key == K_SLASH:
                    Num += '/'
                if e.key == K_PERIOD:
                    Num += '.'
                if e.key == K_DELETE:
                    Num = Num[:-1]
                if e.key == K_SPACE:
                    Num = str(eval(Num))
                # Show input and answer on screen
                show = fontText.render(str(Num), True,colorblack)                   
                DISP.blit(show, (20,55))



            if e.type == pygame.MOUSEBUTTONDOWN:          # Mouse click input
                mouse = pygame.mouse.get_pos()            # get mouse position
                if num0.finalbut().collidepoint(mouse):   # test if a point is inside a rectangle
                    Num += '0'
                if num1.finalbut().collidepoint(mouse):
                    Num += '1'
                if num2.finalbut().collidepoint(mouse):
                    Num += '2'
                if num3.finalbut().collidepoint(mouse):
                    Num += '3'
                if num4.finalbut().collidepoint(mouse):
                    Num += '4'
                if num5.finalbut().collidepoint(mouse):
                    Num += '5'
                if num6.finalbut().collidepoint(mouse):
                    Num += '6'
                if num7.finalbut().collidepoint(mouse):
                    Num += '7'
                if num8.finalbut().collidepoint(mouse):
                    Num += '8'
                if num9.finalbut().collidepoint(mouse):
                    Num += '9'
                if sym_sum.finalbut().collidepoint(mouse):
                    Num += '+'
                if sym_mi.finalbut().collidepoint(mouse):
                    Num += '-'
                if sym_mul.finalbut().collidepoint(mouse):
                    Num += '*'
                if sym_div.finalbut().collidepoint(mouse):
                    Num += '/'
                if sym_dot.finalbut().collidepoint(mouse):
                    Num += '.'
                if sym_clear.finalbut().collidepoint(mouse):
                    Num = ' '
                if sym_del.finalbut().collidepoint(mouse):
                    Num = Num[:-1]
                if ans.finalbut().collidepoint(mouse):
                    Num = str(eval(Num))
            # text not out of the screen    
            if len(Num) >= 22: 
                Num = Num[:-1]
                    
            pygame.draw.rect(DISP,colorsofty,(10,30,330,90))
            DISP.blit(logo.render('Tangmo',True,colormbred),(15,165))
            show = fontText.render(str(Num), True,colorblack)              
            DISP.blit(show, (20,55))



        pygame.display.update()            # Update portions of the screen

cal_loop()                                 # call function to run programme
pygame.quit()                              # uninitialize all pygame modules
quit()

