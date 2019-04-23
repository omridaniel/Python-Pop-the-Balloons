#########################################################################
# Programmer: Omri Daniel
# Date:  April 11th 2018
# File Name: pop_the_balloons.py
# Description: Pop as many balloons as you can!
##########################################################################

import pygame
pygame.init()

from math import sqrt                                                                # only sqrt function is needed from the math module
from random import randint                                                      # only randint function is needed from the random module

HEIGHT = 600
WIDTH  = 800
game_window=pygame.display.set_mode((WIDTH,HEIGHT))

pop=0

WHITE = (255,255,255)                   
BLACK = (  0,  0,  0)                                                                       # used colours
outline=0                                                                                       # thickness of the shapes' outline

sky=pygame.image.load('sky.jpg')
sky=sky.convert_alpha()
sky=pygame.transform.scale(sky,(WIDTH,HEIGHT))

font = pygame.font.SysFont("Ariel Black",50)                                # create a variable font
font2 = pygame.font.SysFont("Ariel Black",100)                             # create a variable font


#------------------------------------------------------------------------------#
# function that calculates distance     
# between two points in coordinate system
#------------------------------------------------------------------------------#
def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)                                                # Pythagorean theorem    

#-------------------------------------------------------------------------------#
# function that redraws all objects     
#-------------------------------------------------------------------------------#
def redraw_game_window():
    game_window.blit(sky,(0,0))
    pygame.draw.rect(game_window,(0,100,0),(0,(HEIGHT-60),WIDTH,60))
    
    for i in range(20):
        if balloonPop[i]==False:
            pygame.draw.circle(game_window, (R[i],G[i],B[i]), (balloonX[i], balloonY[i]), balloonR[i], outline)
            
    popTxt=font.render('Balloons popped:'+str(pop),1,WHITE)
    timeTxt=font.render('Time:'+timer[:-2],1,BLACK)
    
    game_window.blit(timeTxt,(645,HEIGHT-50))
    game_window.blit(popTxt,(10,HEIGHT-50))
    
    pygame.display.update()                                                                # display must be updated, in order
                                                                                                            # to show the drawings
def end_game_window():
    game_window.fill(BLACK)

    timeTxt=font.render('Total time:'+timer[:-2]+' seconds',1,WHITE)
    game_window.blit(timeTxt,(440,HEIGHT-50))

    popTxt=font.render('Total popped:'+str(pop)+' ballons',1,WHITE)
    game_window.blit(popTxt,(10,HEIGHT-50))

    font_size=100
    endTxt=font2.render('Game Over.',1,WHITE)
    game_window.blit(endTxt,(WIDTH/4,HEIGHT/3))

    pygame.display.update()
       
#-----------------------------------------------------------------------------#
# the main program begins here          
#-----------------------------------------------------------------------------#
exit_flag = False                       


balloonR = [0]*20                                                                                    # create lists of 20 items each
balloonX = [0]*20                                                                                    # for balloons' properties
balloonY = [0]*20                       
balloonSPEED = [0]*20                   
R=[0]*20
G=[0]*20
B=[0]*20
balloonPop=[False]*20

for i in range(20):
    balloonX[i] = randint(0, WIDTH)                                                             # initialize the coordinates and the size of the balloons
    balloonY[i] = randint(HEIGHT/2, HEIGHT)
    balloonR[i] = randint(20,50)
    balloonSPEED[i] = randint(3,6)
    R[i]=randint(0,255)
    G[i]=randint(0,255)
    B[i]=randint(0,255)
    
while not exit_flag:                    
    for event in pygame.event.get():                                                               # check for any events
        if event.type == pygame.QUIT:                                                              # If user clicked close
            exit_flag = True                                                                                 # Flag that we are done so we exit this loop

        if event.type == pygame.MOUSEBUTTONDOWN:                                    # act upon mouse events
            for i in range(20):
                (cursorX,cursorY)=pygame.mouse.get_pos()
                if distance(cursorX, cursorY, balloonX[i], balloonY[i])< balloonR[i] and balloonPop[i]==False:
                    balloonPop[i] = True
                    pop+=1
                    print('Balloons popped:',pop)

    if pop>=20 or False not in balloonPop:
        ###################
        '''Issue with balloons overlapping'''
        ###################
        exit_flag=True
        
    timer=str(round(pygame.time.get_ticks()/1000,0))    
    for i in range(20):
        balloonY[i] = balloonY[i] - balloonSPEED[i]
        if balloonY[i]<0-balloonR[i]:                                                                       #check if balloon out of screen
            balloonPop[i]=True
    redraw_game_window()                                                                                #update the screen
    pygame.time.delay(75)

end_game_window()
print('Total time:',timer[:-2])
pygame.time.delay(6000)
pygame.quit()                                                                                                    # always quit pygame when done!
