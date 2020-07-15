import pygame
from time import sleep
import sys
from math import acos, asin, sin, cos, tan, pi, sqrt
from Sliders_2d_2 import *
from formulas import *
pygame.init()                                           #Starting pygame

WHITE =  (255, 255, 255)#---------------------#
BLUE =   (0, 0, 255)                          #|
YELLOW = (255, 255, 0)                        #|Declaring
RED =    (255, 0, 0)                          #|
GREEN =  (0, 255, 0)                          #|Colors
BLACK =  (0,  0,  0)                          #|
GREY =   (50, 50, 50)                         #|
BLACK =  (0,  0,  0)                          #|
ORANGE = (200, 100, 50)#----------------------#

#Declare width and height of screen
WIDTH = 900                  
HEIGHT = 650

#Delare font and screen
myfont2 = pygame.font.SysFont('Arial', 20)
myfont = pygame.font.SysFont('Arial', 15)
screen=pygame.display.set_mode((WIDTH,HEIGHT))

def fade(width,height):
    """
    Fading in effect with width and height of the screen as parameters
    """
    fade=pygame.Surface((width,height))
    fade.fill(WHITE)
    for alpha in range(0,300):
        fade.set_alpha(alpha)
        screen.blit(fade,(0,0))
        pygame.display.update()
        pygame.time.delay(3)
        
def Rfade(width,height):
    """
    Fading out effect with width and height of the screen as parameters
    """
    fade=pygame.Surface((width,height))
    fade.fill(WHITE)
    for alpha in reversed(range(0,300)):
        fade.set_alpha(alpha)
        screen.blit(fade,(0,0))
        pygame.display.update()
        
def twoD_Play():
    #Definding all the images
    car = pygame.image.load("car.png")
    car = pygame.transform.scale(car,(60,20))
    car_extra=pygame.image.load("car.png")
    car_extra=pygame.transform.scale(car_extra,(30,10))
    background = pygame.image.load("background_forces.jpg")
    background = background.convert_alpha()
    background = pygame.transform.scale(background,(WIDTH,HEIGHT))
    
    a = Slider("Acceleration", 25, 1, 15+60+60+60, "m/s²")              #Object of the Sliders Class  
    m = Slider("Mass", 10, 1, 15+60+60+60+60, "kg")                     #Object of the Sliders Class
    mu = Slider("Fric. Coef", 0.99, 0, 15+60+60+60+60+60, "")           #Object of the Sliders Class
    fa = Slider("Applied Force", 200, 0, 15+60+60+60+60+60+60, "N")     #Object of the Sliders Class
    theta = Slider("Angle", 89,1, 15+60+60+60+60+60+60+60, "°")         #Object of the Sliders Class

    slides=[a,m,mu,fa,theta]
    a,m,mu,fa,theta=call_sliders(slides)                                #Calls the sliders with the acceleration, mass, coef, applied force and theta as parameters

    theta *= (pi/180)
    if a == None: a=formula1(a,theta,m,mu,fa,'a')                       #####
    if m == None: m=formula1(a,theta,m,mu,fa,'m')                           #Solves for the -
    if mu == None: mu=formula1(a,theta,m,mu,fa,'mu')                        #missing variables
    if fa == None: fa=formula1(a,theta,m,mu,fa,'fa')                    #####

        
    g=9.8                                                               #####
    fn=m*g*cos(theta)                                                       #
    ff=mu*fn                                                                #Defines all the constants, later to be used
    fg=m*g*sin(theta)                                                       #for the legend function.
    draw_displacement=450                                                   #
    draw_height=draw_displacement*sin(theta)                                #
    draw_length=draw_displacement*cos(theta)                            #####

    #-------------------------ENERGY-----------------------#
            
    energy = 'N'#input("Is Energy involved in the question? (Y/N): ")
    fade(WIDTH,HEIGHT)
##        if energy == 'Y':
##            v1=float(input("v1: "))
##            v2=float(input("v2: "))
##            dlh = 'd'#input("Displacement, Length or Height: ")
##            if dlh == 'd':
##                displacement=400#float(("displacement: ") #MANDATORY
##                height=displacement*sin(theta)
##                length=displacement*cos(theta)
##
##            elif dlh == 'h':
##                height=float(input("height: ")) #MANDATORY
##                displacement=height/sin(theta)
##                length=height/tan(theta)
##
##            elif dlh == 'l':
##                length=float(input("length: ")) #MANDATORY
##                displacement=length/cos(theta)
##                height=length*tan(theta)


##            count=0
##            varList=[v1,v2,height,displacement]
##            varName = ['v1','v2','h','d']
##            for i in range(len(varList)):
##                if varList[i] == -666:
##                    varList[i]=formula2(v1,v2,height,displacement,varName[i],ff,fa,m,theta)
##                    count+=1
##                                        
##                if count>=2:
##                    print("ERROR: Not enough data")
##                    quit_completely()
##
##                if i == len(varList)-1 and count == 0:
##                    print("ERROR: Variables Contradict eachother")
##                    quit_completely()
##                    
##            v1,v2 = varList[0],varList[1]
    
    horizontal_a, vertical_a = a*cos(theta), -1*a*sin(theta)
    x,y = 0,-10
    speed_x,speed_y = 0,0
    car = pygame.transform.rotate(car, -theta*180/pi)

#------------------------------------------------- MAIN -------------------------------------------------#

    def redraw():
        screen.blit(background,(0,0))
        redraw_background()
        start_pointx = main_pointx-10
        start_pointy = main_pointy-draw_height-10
        screen.blit(car,(x+start_pointx,y+start_pointy))
        pygame.display.update() 

    def legend():
        screen.blit(car_extra,(7,50+10))
        m_text = myfont.render('Mass: '+str(round(m,2))+'kg', False, WHITE)
        screen.blit(m_text,(45, 10+10))
        fa_text = myfont.render('Applied Force: '+str(round(fa,2))+'N', False, WHITE)
        screen.blit(fa_text,(45, 30+10))
        a_text = myfont.render('Acceleration: '+str(round(a,2))+'m/s²', False, WHITE)
        screen.blit(a_text,(45, 50+10))
        ff_text = myfont.render('Force of Friction: '+str(round(ff,2))+'N', False, WHITE)
        screen.blit(ff_text,(45, 70+10))
        mu_text = myfont.render('mu: '+str(round(mu,2)), False, WHITE)
        screen.blit(mu_text,(45, 90+10))
        
    def redraw_background():
        t = myfont.render(str(round(theta*180/pi,2))+'°', False, WHITE)
        pygame.draw.line(screen,WHITE,(main_pointx,main_pointy),(main_pointx+draw_length,main_pointy),3)             #Length
        pygame.draw.line(screen,WHITE,(main_pointx,main_pointy),(main_pointx,main_pointy-draw_height),3)            #Height
        pygame.draw.line(screen,WHITE,(main_pointx+draw_length,main_pointy),(main_pointx,main_pointy-draw_height),3) #Displacement
        pygame.draw.arc(screen, WHITE, (main_pointx+draw_length-25,main_pointy-25,50,50), pi-theta, pi, 3)
        if energy == 'Y':
            h = myfont.render('Height: '+str(round(height,2))+'m', False, WHITE)
            l = myfont.render('Length: '+str(round(length,2))+'m', False, WHITE)
            d = myfont.render('Displacement: '+str(round(displacement,2))+'m', False, WHITE)
            screen.blit(h,(main_pointx-100, main_pointy-draw_height/2))
            screen.blit(l,(main_pointx+draw_length/2-75, main_pointy))
            screen.blit(d,(main_pointx+5, main_pointy-20))
        screen.blit(t,(main_pointx+draw_length+5, main_pointy-25))

        legend()
        if energy == 'Y':
            v1_text = myfont.render('v₁: '+str(round(v1,2))+'m/s', False, BLACK)
            screen.blit(v1_text,(15, 110))
            v2_text = myfont.render('v₂: '+str(round(v2,2))+'m/s', False, BLACK)
            screen.blit(v2_text,(15, 130))

    main_pointx = (WIDTH-draw_length)/2 #Centers the entire mechanism
    main_pointy = HEIGHT-50
    clock = pygame.time.Clock()
    while y<=(HEIGHT-(HEIGHT-main_pointy)-(main_pointy-draw_height))-20:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 quit_completely()
        if a > 0: 
            dt = clock.tick(60)
            speed_x += horizontal_a*dt/30
            speed_y += vertical_a*dt/30

            x+=speed_x/30
            y-=speed_y/30
        redraw()
    y-=20
    car = pygame.transform.rotate(car, theta*180/pi)
    while x<=WIDTH:
        x+=2#speed_x/30
        redraw()
    sleep(5)
    
    #fade(WIDTH,HEIGHT)


