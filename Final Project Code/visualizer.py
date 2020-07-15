from Kinematics import kinimatics_run
from Forces import forces_run
from Momentum import momentum_run
from Gravity import gravity_run
from Waves import waves_run

import pygame
pygame.init()
from time import sleep

white = (255,255,255)
blue1 = (102, 153, 153)
blue2 = (64, 127, 127)
blue3 = (13, 77, 77)
blue4 = (0, 51, 51)

d_blue1 = (41, 56, 96)
d_blue2 = (24, 44, 93)
d_blue3 = (69, 92, 148)
d_blue4 = (77, 98, 151)

green1 = (38, 108, 53)
green2 = (60, 140, 80)
green3 = (42, 155, 67)
green4 = (46, 158, 71)
green5 = (32, 114, 19)

WIDTH, HEIGHT = 900, 650
screen=pygame.display.set_mode((WIDTH, HEIGHT))

#-=Setting the background=-#
background = pygame.image.load("background_visualizer.jpg")
background = background.convert_alpha()
background = pygame.transform.scale(background,(900,650))
#-=Importing all kinimatics pictures=-#
kin = pygame.image.load("1_noclick.png")
kin = kin.convert_alpha()
kin = pygame.transform.scale(kin,(137,57))
hover1 = pygame.image.load("1_hover.png")
hover1 = hover1.convert_alpha()
hover1 = pygame.transform.scale(hover1,(137,57)) 
#-=Importing all dynamics pictures=-#
dyn = pygame.image.load("2_noclick.png")
dyn = dyn.convert_alpha()
dyn = pygame.transform.scale(dyn,(137,57))
hover2 = pygame.image.load("2_hover.png")
hover2 = hover2.convert_alpha()
hover2 = pygame.transform.scale(hover2,(137,57)) 
#-=Importing all impulse and momentum pictures=-#
imp = pygame.image.load("3_noclick.png")
imp = imp.convert_alpha()
imp = pygame.transform.scale(imp,(137,57))
hover3 = pygame.image.load("3_hover.png")
hover3 = hover3.convert_alpha()
hover3 = pygame.transform.scale(hover3,(137,57)) 
#-=Importing all gravity pictures=-#
grv = pygame.image.load("4_noclick.png")
grv = grv.convert_alpha()
grv = pygame.transform.scale(grv,(137,57))
hover4 = pygame.image.load("4_hover.png")
hover4 = hover4.convert_alpha()
hover4 = pygame.transform.scale(hover4,(137,57)) 
#-=Importing all wave pictures=-#
wav = pygame.image.load("5_noclick.png")
wav = wav.convert_alpha()
wav = pygame.transform.scale(wav,(137,57))
hover5 = pygame.image.load("5_hover.png")
hover5 = hover5.convert_alpha()
hover5 = pygame.transform.scale(hover5,(137,57))
#-=For shits and gigs=-#
BLACK=(0,0,0)
funFont = pygame.font.SysFont("Impact", 100)
funMessage = funFont.render('\_(^-^)_/',False, BLACK)

def unit_buttons(x,y): # Pick-the-unit button
    width = 137
    height = 57
    increment = 33.5
    pop = 7
    click = pygame.mouse.get_pressed()
    wi= width+increment
    for i in range(len(visualizer.units)):
        if 33.5+(137+33)*i < x < (33.5+(137+33)*i)+137 and  6 < y < 57:
            #pygame.draw.rect(screen, blue1, [increment+wi*i, 6, width, height])
            if click[0] == 1:
                #pygame.draw.rect(screen, white, [increment+wi*i, 6, width, height])
                for j in range(len(visualizer.units)):
                    if i == j:
                        visualizer.units[j].choose = True
                    else:
                        visualizer.units[j].choose = False
                    visualizer.units[j].display()
                   # print(visualizer.units[j],':',visualizer.units[j].choose)
                print()
            pygame.display.update()
                         
        else:
            #pygame.draw.rect(screen, blue2, [increment-pop/2+wi*i, 6, width+pop, height+pop])
            screen.blit(kin,(33.5,6.5))
            screen.blit(dyn,(203.5,6.5))
            screen.blit(imp,(373.5,6.5))
            screen.blit(grv,(543.5,6.5))
            screen.blit(wav,(713.5,6.5))
            pygame.display.update()
        
##def start_button(x,y): # Start-the-animation button
##    pop = 7
##    click = pygame.mouse.get_pressed()
##    if 10 < x < 10+50 and  75 < y < 75+25:
##        pygame.draw.rect(screen, green3, (10, 75, 50, 25))
##        if click[0] == 1:
##            pygame.draw.rect(screen, white, (10, 75, 50, 25))
##    else:
##        pygame.draw.rect(screen, green1, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
##    pygame.display.update()
    
class Visualizer():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
        kinematics = Kinematics()
        dynamics = Dynamics()
        impulseAndMomentum = ImpulseAndMomentum()
        gravFields = GravFields()
        waves = Waves()

        self.units = [kinematics, dynamics, impulseAndMomentum, gravFields, waves]
        
    def display(self):
        pygame.display.update()
        screen.blit(background,(0,0))
        screen.blit(funMessage,(300,180))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        x,y = pygame.mouse.get_pos()
        unit_buttons(x,y)
##        start_button(x,y)
    
class Kinematics():
    def __init__(self):
        self.choose = False

    def display(self):
        if self.choose:
            screen.blit(hover1,(33.5,6.5))
            pygame.display.update()
            kinimatics_run()
            
    def __str__(self):
        return 'Kinematics'
    
class Dynamics():
    def __init__(self):
        self.choose = False
        
    def display(self):
        if self.choose:
            screen.blit(hover2,(203.5,6.5))
            pygame.display.update()
            forces_run()
            
    def __str__(self):
        return 'Dynamics'
    
class ImpulseAndMomentum():
    def __init__(self):
        self.choose = False
        
    def display(self):
        if self.choose:
            screen.blit(hover3,(373.5,6.5))
            pygame.display.update()
            momentum_run()
    
    def __str__(self):
        return 'Impulse And Momentum'

class GravFields():
    def __init__(self):
        self.choose = False
        
    def display(self):
        if self.choose:
            screen.blit(hover4,(543.5,6.5))
            pygame.display.update()
            gravity_run()
    def __str__(self):
        return 'Gravitational Fields'
    
class Waves():
    def __init__(self):
        self.choose = False
        
    def display(self):
        if self.choose:
            screen.blit(hover5,(713.5,6.5))
            pygame.display.update()
            waves_run()
    def __str__(self):
        return 'Waves'

run = True
screen=pygame.display.set_mode((WIDTH, HEIGHT))
screen.blit(background,(0,0))
visualizer = Visualizer(WIDTH, HEIGHT)

screen.fill(blue4)
while run:
    visualizer.display()
    
