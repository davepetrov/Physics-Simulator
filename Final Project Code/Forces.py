import math
import pygame
from time import sleep
from Sliders_1d import *
from Forces_2d import twoD_Play
def forces_run():
    pygame.init()
    #Defining the variables
    WIDTH, HEIGHT = 900, 650
    screen=pygame.display.set_mode((WIDTH, HEIGHT))
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    GREY = WHITE

    myfont = pygame.font.SysFont('Arial', 13)
    myfont = pygame.font.SysFont("Arial", 12)
    choose_image = pygame.image.load('choose_images_forces.png')
    twoD_click = pygame.image.load('2d_click_forces.png')
    vert_click = pygame.image.load('vert_click_forces.png')
    horiz_click = pygame.image.load('horiz_click_forces.png')
    #Plane images for Horizontal Animation
    horiz_plane = pygame.image.load("horiz_plane.png")
    horiz_plane = pygame.transform.scale(horiz_plane,(60,60))
    horiz_plane_extra=pygame.image.load("horiz_plane.png")
    horiz_plane_extra=pygame.transform.scale(horiz_plane_extra,(30,30))
    #Planes images for vertical Animation
    vert_plane = pygame.image.load("vert_plane.png")
    vert_plane = pygame.transform.scale(vert_plane,(60,60))
    vert_plane_extra=pygame.image.load("vert_plane.png")
    vert_plane_extra=pygame.transform.scale(vert_plane,(30,30))

    #Backgrounds depending on the component (Vertical or Horizontal)
    background2 = pygame.image.load('background2_forces.jpg')
    background3 = pygame.image.load('background3_forces.jpg')

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
            pygame.time.delay(3)
            
    class One:
        def __init__(self):
            self.mass = None
            self.a = None
            self.displacement = None
            self.time = None
            self.coef = None
            self.force_app = None
            self.fair = None
            self.start = False
            self.fair_restriction = None
            self.ball_x = 0
            self.mousex, self.mousey = pygame.mouse.get_pos()

        def legend(self,component):
                                                                                                                #Legend with all the variables on the top left screen; called when animation starts.
                                                                                                                #Variable vary whether animation is horizontal or vertical
                                                                                                                #Horizontal Variables: Mass, Applied Force, Accelertaion, Force of Friction, Coef. of Friction
                                                                                                                #Vertical Variables: Mass, Force of Gravity, Acceleration, Air resistance
            if component =='horizontal':
                screen.blit(horiz_plane_extra,(7,50))
                m_text = myfont.render('Mass: '+str(round(self.mass,2))+'kg', False, BLACK)
                screen.blit(m_text,(45, 10+10))
                fa_text = myfont.render('Applied Force: '+str(round(self.force_app,2))+'N', False, BLACK)
                screen.blit(fa_text,(45, 30+10))
                a_text = myfont.render('Acceleration: '+str(round(self.a,2))+'m/s²', False, BLACK)
                screen.blit(a_text,(45, 50+10))
                ff = self.mass*9.8*self.coef
                ff_text = myfont.render('Force of Friction: '+str(round(ff,2))+'N', False, BLACK)
                screen.blit(ff_text,(45, 70+10))
                mu_text = myfont.render('mu: '+str(round(self.coef,2)), False, BLACK)
                screen.blit(mu_text,(45, 90+10))
            elif component =='vertical':
                screen.blit(vert_plane_extra,(7,50))
                m_text = myfont.render('Mass: '+str(round(self.mass,2))+'kg', False, WHITE)
                screen.blit(m_text,(45, 10+10))
                fg=self.mass*9.8
                fg_text = myfont.render('Gravity Force: '+str(round(fg,2))+'N', False, WHITE)
                screen.blit(fg_text,(45, 30+10))
                a_text = myfont.render('Acceleration: '+str(round(self.a,2))+'m/s²', False, WHITE)
                screen.blit(a_text,(45, 50+10))
                fair_text = myfont.render('Air Resistance: '+str(round(self.fair,2))+'N', False, WHITE)
                screen.blit(fair_text,(45, 70+10))
                
        def draw(self, component):
            clock = pygame.time.Clock()
            if component == 'horizontal':
                t = myfont.render('Change in time is '+str(round(self.time,2))+' seconds', False, BLACK)
                d = myfont.render('Displacement is '+str(round(self.displacement,2))+' meters', False, BLACK)
                start_x=100
                x=start_x                                                                                                                   #Initial x position is 100 pixels from the left
                max_dist = int(start_x+self.displacement*(WIDTH-2*start_x)/100)                                                             #Maximum distance beforet to stop the object from continuing
                speed=0                                                                                                                     #Initial speed is 0 since object is in freefall, v1=0
                dt = clock.tick(60)                                                                                                         #Adjusts animation to 60Hz screen
                while start_x <= x < max_dist:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                    speed+=self.a*dt/20
                    x+=int(speed/20)
                    screen.blit(background3,(0,0))
                    self.legend('horizontal')
                    screen.blit(t,(WIDTH/2-100, HEIGHT/2+120))
                    screen.blit(d,(WIDTH/2-100, HEIGHT/2+100))
                    for i in range(3, 24, 1):
                        pygame.draw.line(screen, BLACK, [i*(WIDTH-2*start_x)/20-5, HEIGHT/2+70-5],[i*(WIDTH-2*start_x)/20-5,HEIGHT/2+70+10]) #Draws the line from 0 to 100
                        mark = myfont.render(str((i-3)*5), False, BLACK)                                                                     #Defines the marks
                        screen.blit(mark,(i*(WIDTH-2*start_x)/20-5-3, HEIGHT/2+70+10))                                                       #Draws the marks

                    
                    if x >= max_dist:x=max_dist                                                                                              #Caps the maximum distance so the object would not continue moving off the screen
                    pygame.draw.line(screen, BLACK, [start_x, HEIGHT/2+70],[x,HEIGHT/2+70])
                    screen.blit(horiz_plane,(x,HEIGHT/2))

                    pygame.display.update()
        
                    
            elif component == 'vertical':
                start_y = 50
                y=start_y                                                                                                   #Initial y position is 50 pixels from the top
                speed=0                                                                                                     #Initial speed is 0 since object is in freefall, v1=0
                dt = clock.tick(60)                                                                                         #Adjusts animation to 60Hz screen
                while start_y <= y < HEIGHT-start_y:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                    speed+=self.a*dt/20
                    y+=int(speed/20)
                    screen.blit(background2,(0,0))
                    self.legend('vertical')
                    if y >HEIGHT-start_y:                                                                                   #Caps the maximum distance so the object would not continue moving off the screen
                        pygame.draw.line(screen, WHITE, [WIDTH/2+70-5,start_y],[WIDTH/2+70+5,start_y])
                        pygame.draw.line(screen, WHITE, [WIDTH/2+70-5,HEIGHT-start_y+10],[WIDTH/2+70+5,HEIGHT-start_y+10])
                        y=HEIGHT-start_y
                        
                    pygame.draw.line(screen, WHITE, [WIDTH/2+70, start_y],[WIDTH/2+70,y+5])
                    screen.blit(vert_plane,(WIDTH/2,y))

                    pygame.display.update()
                
        
    #-------------------------------------------------------------Adjustments BAR-------------------------------------------------------------#
        def before_start_vertical(self):
            m = Slider("Mass", 30, 1, HEIGHT/2-30, "kg")                                            #Object of the Sliders Class
            fair = Slider("Air Resistance", 20, 1, HEIGHT/2+30, "N")                                #Object of the Sliders Class
            slides=[m,fair]

            self.mass,self.fair=call_sliders(slides, "Vertical")                                    #Calls the sliders with the mass and air resistance objects as parameters
            
            force_gravity = self.mass*9.8                                                           #Solves for force of gravity
            self.a = (force_gravity - self.fair)/self.mass                                          #Solves for acceleration
            return True
        
        def  before_start_horizontal(self):
            m = Slider("Mass", 20, 1, 15+60+60+60, "kg")                                            #Object of the Sliders Class
            fa = Slider("Applied Force", 50, 1, 15+60+60+60+60, "N")                                #Object of the Sliders Class
            coef = Slider("Fric. Coef", 0.99, 0, 15+60+60+60+60+60, "")                             #Object of the Sliders Class
            displacement = Slider("Displacement", 100, 0, 15+60+60+60+60+60+60, "m")                #Object of the Sliders Class
            slides=[m,fa,coef,displacement]
            self.mass,self.force_app,self.coef,self.displacement=call_sliders(slides, "Horizontal") #Calls the sliders with the mass, applied force, coef and displacement as parameters
            
            force_friction = self.mass*9.8*self.coef                                                #Once the sliders values are sent in to calculate, the rest of the missing variables are solved for 
            one.a = (self.force_app - force_friction)/self.mass                                     #Solves for acceleraion
            self.time=math.sqrt(self.displacement/self.a)                                           #Solves for time

            return True

    #-------------------------------------------------------------MAIN-------------------------------------------------------------#
        
        def start_button_press(self):
            self.mousex, self.mousey = pygame.mouse.get_pos()
            pop = 7
            event = pygame.event.poll()
            if 10 <= self.mousex <= 10+50 and  75 <= self.mousey <= 75+25:
                    pygame.draw.rect(screen, GREEN, (10, 75, 50, 25))
                    pygame.display.update()
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(screen, WHITE, (10, 75, 50, 25))
                        pygame.display.update()
                        return True
            if self.a >1:
                pygame.draw.rect(screen, GREEN, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
            else:
                pygame.draw.rect(screen, RED, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
            pygame.display.update()
            return False


    def redraw_buttons( component):
        screen.fill(WHITE)
        twoD_width=228  #####
        twoD_x=99           #
        vert_width=233      #
        vert_x=340          # Width, height, x and y variables for the 2d and 1d buttons
        horiz_width=217     #  
        horiz_x=585         #   
        h=351               #
        y=137           #####
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        click = pygame.mouse.get_pressed()  
        screen.blit(choose_image,(0,0))
        mousex, mousey = pygame.mouse.get_pos()
        if vert_x <= mousex <= vert_x+vert_width and y <= mousey <= y+h :         #
            screen.blit(vert_click,(0,0))                                                   #If the user hovers on the button, the  -
        elif horiz_x <= mousex <= horiz_x+horiz_width and y <= mousey < y+h :     #the "hover" image of that particular -
            screen.blit(horiz_click,(0,0))                                                  #button pops up
        elif twoD_x <= mousex <= twoD_x+twoD_width and y <= mousey < y+h:         #
            screen.blit(twoD_click,(0,0))                                               #####

        pygame.display.update()


    def choose_component():
        event = pygame.event.poll()
        mousex, mousey = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        twoD_width=228  #####
        twoD_x=99           #
        vert_width=233      #
        vert_x=340          # Width, height, x and y variables for the 2d and 1d buttons
        horiz_width=217     #  
        horiz_x=585         #   
        h=351               #
        y=137           #####
        if vert_x <= mousex <= vert_x+vert_width and y <= mousey <= y+h and event.type == pygame.MOUSEBUTTONDOWN:         #####
            return 'vertical'                                                                                                           #
        elif horiz_x <= mousex <= horiz_x+horiz_width and y <= mousey < y+h and event.type == pygame.MOUSEBUTTONDOWN:         #If the user clicks on the button, the function returns
            return 'horizontal'                                                                                                         #either 2d, vertical or horizontal, according to the button
        elif twoD_x <= mousex <= twoD_x+twoD_width and y <= mousey < y+h and event.type == pygame.MOUSEBUTTONDOWN:            #
            return '2d'                                                                                                             #####                                                                                                       

    one = One()
    one_dimention_choose = True

    component = None
    while component == None:
        component = choose_component()
        redraw_buttons(component)

    if component == '2d':
        twoD_Play()
        
    elif component == 'vertical':
        start=one.before_start_vertical()
        if start == True :
            fade(WIDTH,HEIGHT)
            print('s')
            one.draw('vertical')
            sleep(3)
            
    elif component == 'horizontal':
        start=one.before_start_horizontal()   
        if start == True :
            fade(WIDTH,HEIGHT)
            one.draw('horizontal')
            sleep(3)


    fade(WIDTH,HEIGHT)          
    one.mass = None             #####
    one.a = None                    #
    one.displacement = None         #
    one.time = None                 #Resets all the 1d variables to default
    one.coef = None                 #
    one.force_app = None            #
    one.fair = None                 #
    one.start = False           #####
    unit=''
    
