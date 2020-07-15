def kinimatics_run():
    import math
    import cmath
    import pygame
    import time
    import sys
    from random import randint
    ##from Equations import formula2_eq,formula3_eq,formula4_eq,formula5_eq,formula6_eq,quad_form
    ##from Sliders import Slider
    def formula2_eq(vi,vf,a,t,d,desired): 
        if 'vi'==desired:
            return(vf-a*t)#rearanged formula for vi
        elif 'vf'==desired:
            return(vi+a*t)#rearanged formula for vf
        elif 'a'==desired:
            return((vf-vi)/t)#rearanged formula for a
        elif 't'==desired:
            return((vf-vi)/a)#rearanged formula for t
        else:
            return False
    def formula3_eq(vi,vf,a,t,d,desired):
        if 'vi'==desired:
            return((2*d/t)-vf)#rearanged formula for vi
        elif 'vf'==desired:
            return((2*d/t)-vi) #rearanged formula for vf
        elif 't'==desired:
            return(2*d/(vf+vi)) #rearanged formula for t
        elif 'd'==desired:
            return(((vi+vf)/2)*t) #rearanged formula for d
        else:
            return False
    def formula4_eq(vi,vf,a,t,d,desired):
        if 'vi'==desired:
            return((d-(0.5*a*t**2))/t)#rearanged formula for vi
        elif 'a'==desired:
            return((d-vi*t)/(0.5*(t**2))) #rearanged formula for a
        elif 't'==desired:
            return(quad_form((1/2)*a,vi,-d)) #rearanged formula for t
        elif 'd'==desired:
            return((vi*t+(1/2)*a*t**2)) #rearanged formula for d
        else:
            return False
    def formula5_eq(vi,vf,a,t,d,desired):
        if 'vf'==desired:
            return((d+0.5*a*t**2)/t) #rearanged formula for vf
        elif 'a'==desired:
            return((d-vf*t)/(-0/5*t**2))  #rearanged formula for a
        elif 't'==desired:
            return(quad_form((-0.5)*a,vf,-d)) #rearanged formula for t
        elif 'd'==desired:
            return(vf*t-((1/2)*a*t**2)) #rearanged formula for d
        else:
            return False    
    def formula6_eq(vi,vf,a,t,d,desired):
        if 'vi'==desired:
            return(math.sqrt(vf**2-2*a*d)) #rearanged formula for vi
        elif 'vf'==desired:
            return(math.sqrt(vi**2+2*a*d)) #rearanged formula for vf
        elif 'a'==desired:
            return((vf**2-vi**2)/(2*d)) #rearanged formula for a
        elif 'd'==desired:
            return((vf**2-vi**2)/(2*a)) #rearanged formula for d
        else:
            return False
        
    def quad_form(a,b,c): 
        d = (b**2) - (4*a*c)                    #Calculates the discrimenent 
        solution1 = (-b-math.sqrt(d))/(2*a)     #Finds both plus and minus vareints
        solution2 = (-b+math.sqrt(d))/(2*a)
        if solution1>0:                         #Returns the positive value 
            return round(solution1,2)
        elif solution2>0:
            return round(solution2,2)

    pygame.init()                                           #Starting pygame
    WIDTH = 900                  
    HEIGHT = 650

    WHITE =  (255, 255, 255)#---------------------#
    BLUE =   (0, 0, 255)                          #|
    YELLOW = (255, 255, 0)                        #|Declaring
    RED =    (255, 0, 0)                          #|
    GREEN =  (0, 255, 0)                          #|Colors
    BLACK =  (0,  0,  0)                          #|
    GREY =   (192, 192, 192)                      #|
    TRANS = (1, 1, 1)                             #|
    ORANGE = (200, 100, 50)#----------------------#

    class Slider():
        def __init__(self, name, val, maxi, mini, pos, unit):
            self.val = val                                          # start value
            self.maxi = maxi                                        # maximum at slider position right
            self.mini = mini                                        # minimum at slider position left
            self.xpos = 700                                         # x-location on screen
            #self.x_max = self.xpos+80
            self.ypos = pos                                         # y-location on screen
            self.surf = pygame.surface.Surface((180, 50))           # creates the sliders surface
            self.surf2 = pygame.surface.Surface((50, 50))           # creates the secondary surface
            self.hit = False                                        # the hit attribute indicates slider movement due to mouse interaction
            self.display="Gucci"                                    # Starting display for the small box
            self.boxCol=GREY                                        # Starting display color for the smaller box (Starts as nutral color)
            self.unit = unit                                        # Sliders corrisponding unit
            self.string = ''                                        # Starting string value
            self.name = name                                        # Sliders name 
            
            self.txt_surf = font1.render(name, 1, BLACK)            # Creates the text for the sliders 
            self.txt_rect = self.txt_surf.get_rect(center=(50, 15))

            # Static graphics - slider background #
            pygame.draw.rect(self.surf, GREY, [0, 0, 180, 50], 3)   # Creates the display
            pygame.draw.rect(self.surf, ORANGE, [10, 10, 80, 10], 0)
            pygame.draw.rect(self.surf, WHITE, [10, 30, 80, 5], 0)

            pygame.draw.rect(self.surf2, self.boxCol, [0, 0, 50, 50], 3) # Creates the secondary display
            
            self.surf.blit(self.txt_surf, self.txt_rect)            # Displays the text for the sliders

            # dynamic graphics - button surface #
            self.button_surf = pygame.surface.Surface((20, 20))     # Creates the smaller circle for the sliders
            self.button_surf.fill(TRANS)
            self.button_surf.set_colorkey(TRANS)
            pygame.draw.circle(self.button_surf, BLACK, (10, 10), 6, 0)
            pygame.draw.circle(self.button_surf, ORANGE, (10, 10), 4, 0)

        def draw(self):
            # static
            surf = self.surf.copy()                                 # makes a copy of both surfaces
            surf2= self.surf2.copy()
            # dynamic
            pos = (10+int((self.val-self.mini)/(self.maxi-self.mini)*80), 33)
            self.button_rect = self.button_surf.get_rect(center=pos)
            surf.blit(self.button_surf, self.button_rect)
            self.button_rect.move_ip(self.xpos, self.ypos)          # move of button box to correct screen position

            # screen
            mouseX,mouseY=pygame.mouse.get_pos()
            if mouseX>self.xpos-50 and mouseX<self.xpos and mouseY>self.ypos and mouseY<self.ypos+50: #Finds if the mouse is within secondary surface location
                for event in pygame.event.get():                    
                    if event.type == pygame.MOUSEBUTTONDOWN:        #If the mouse is clicked changes the display property and and secondary surface color to match
                        if event.button == 1:
                            if self.display==True:
                                self.display=False
                                self.boxCol=RED
                            elif self.display==False or self.display=="Gucci":
                                self.display=True
                                self.boxCol=GREEN
                        
            if self.display==False:                                 # If slider is not displayed, the string has no value
                self.string='None'
            else:                                                   # If slider is displayed, the string gets the value of the objects val
                self.string=str(self.val)
            pygame.draw.rect(self.surf2, self.boxCol, [0, 0, 50, 50], 3) #Creates a rectangle of to display on the secondary surface
            
            if self.display==True or self.display=="Gucci":         # Displays the surface when its display is not False   
                screen.blit(surf, (self.xpos, self.ypos))
                value = font1.render("= "+str(round(self.val,2))+self.unit,False,WHITE)
                screen.blit(value,(self.xpos+100,self.ypos+15))
                
            screen.blit(surf2,(self.xpos-50,self.ypos))             # Displays the secondary surface
            
        def move(self):

            self.val = (pygame.mouse.get_pos()[0] - self.xpos - 10) / 80 * (self.maxi - self.mini) + self.mini #the objects value is determined by this formula

            if self.val < self.mini:       #If the value falls below its givin miniumum, keepts the minimum value
                self.val = self.mini
            if self.val > self.maxi:       #If the value surpasses the givin maximum, keeps the maximum value
                self.val = self.maxi
            if self.name!='Acceleration': #Only acceleration can have float values
                self.val=int(self.val)

    font1 = pygame.font.SysFont("Verdana", 12)
    screen=pygame.display.set_mode((WIDTH,HEIGHT))

    #####-=All formulas used=-###########
    formula0='v=d/t'
    formula1='a=(vf-vi)/t'
    formula2='vf=vi+a*t'            #d
    formula3='d=(vi+vf)/2*t'        #a
    formula4='d=vi*t+(1/2)*a*t**2'  #vf
    formula5='d=vf*t-(1/2)*a*t**2'  #vi
    formula6='vf**2=vi**2+2*a*d'    #t

    #####-=Fonts for start and main program=-#####
    font = pygame.font.SysFont("Arial",int(25))
    font_start1 = pygame.font.SysFont("Arial",int(20))

    #####-=Creates baseball picture=-#####
    baseball = pygame.image.load("baseball.png")
    baseball = baseball.convert_alpha()
    baseball = pygame.transform.scale(baseball,(20,20))
    rectbaseball = baseball.get_rect()

    #####-=Creates secondary baseball picture=-#####
    base_extra = pygame.image.load("baseball.png")
    base_extra = base_extra.convert_alpha()
    base_extra = pygame.transform.scale(base_extra,(30,30))

    #####-=Imports backgrounds=-#####
    background1=pygame.image.load("background1_kinematics.jpg")
    background1=pygame.transform.scale(background1,(WIDTH,HEIGHT))
    background2=pygame.image.load("background2_kinematics.png")
    background2=pygame.transform.scale(background2,(WIDTH,HEIGHT))

    #####-=Imports 1D and 2D pictures=-#####
    choose_image = pygame.image.load('choose_images.png')
    twoD_click = pygame.image.load('2d_click.png')
    oneD_click = pygame.image.load('1d_click.png')

    middle = True

    def redraw_2d():                 #Redraws the 2D sliders
        for s in slides:
            if s.hit:
                s.move()

        pygame.display.update()
        screen.blit(background1,(0,0))
        for s in slides:
            s.draw()
        message0 = font_start1.render('         -=Information and Rules=-',False,BLACK)      
        message1 = font_start1.render('-Click and slide the bars to chose your values.',False,BLACK)         
        message2 = font_start1.render('-Click on the smaller black box to validate and unvalidate the values.',False,BLACK)
        message3 = font_start1.render('-Please make Acceleration or Time unknown to prevent contradictions.',False,BLACK)
        message4 = font_start1.render('-Pressing down will display the legend and "r" will restart.',False,BLACK)
        message5 = font_start1.render('-Press SPACE when you are ready to start. \_(^-^)_/',False,BLACK)
        message6 = font_start1.render("- Press 'h' to go back to the home page.",False,BLACK)
        #-=Displays messages=-#
        screen.blit(message0,(10,10))
        screen.blit(message1,(10,40))
        screen.blit(message2,(10,70))
        screen.blit(message3,(10,100))
        screen.blit(message4,(10,130))
        screen.blit(message5,(10,160))
        screen.blit(message6,(10,190))
        if middle:
            screen.blit(message,(325,350))
        else:
            screen.blit(message,(100,350))

    def redraw_1d():                #Redraws the 1D sliders
        for s in slides:
            if s.hit:
                s.move()

        pygame.display.update()
        screen.fill(BLACK)
        screen.blit(background2,(0,0))
        for s in slides:
            s.draw()
            
        message0 = font_start1.render('          -=Information and Rules=-',False,WHITE)            
        message1 = font_start1.render('-Click and slide the bars to chose your values.',False,WHITE)         
        message2 = font_start1.render('-Click on the smaller black box to validate and unvalidate the values.',False,WHITE)
        message3 = font_start1.render('-Two unknown values is REQUIRED to prevent contridictions.',False,WHITE)
        message4 = font_start1.render('-Pressing down will display the legend and "r" will restart.',False,WHITE)
        message5 = font_start1.render('-Press SPACE when you are ready to start. \_(^-^)_/',False,WHITE)
        message6 = font_start1.render("- Press 'h' to go back to the home page.",False,WHITE)
        #-=Displays messages=-#
        screen.blit(message0,(10,10))
        screen.blit(message1,(10,40))
        screen.blit(message2,(10,70))
        screen.blit(message3,(10,100))
        screen.blit(message4,(10,130))
        screen.blit(message5,(10,160))
        screen.blit(message6,(10,190))
        if middle:
            screen.blit(message,(325,350))
        else:
            screen.blit(message,(100,350))
        
    def choose_component():             #Redraws choose component pictures and allows user to click and chose
        while True:
            event = pygame.event.poll()
            mousex, mousey = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            twoD_width=233
            twoD_x=239
            oneD_width=233
            oneD_x=497
            h=351
            y=137
            if oneD_x <= mousex <= oneD_x+oneD_width and y <= mousey <= y+h and event.type == pygame.MOUSEBUTTONDOWN:
                return '1D'
            elif twoD_x <= mousex <= twoD_x+twoD_width and y <= mousey < y+h and event.type == pygame.MOUSEBUTTONDOWN:
                return '2D'
            
            screen.blit(choose_image,(0,0))
            if oneD_x <= mousex <= oneD_x+oneD_width and y <= mousey <= y+h :
                screen.blit(oneD_click,(0,0))
            elif twoD_x <= mousex <= twoD_x+twoD_width and y <= mousey < y+h:
                screen.blit(twoD_click,(0,0))

            pygame.display.update()

    restart=False
    start_program = True

    while restart or start_program:
        thing=choose_component()                                            #Calls the choose component function
        if thing=='2D':                                                     #If you choose 2D
            Velocity = Slider("Initial Velocity", 50 ,100 ,0 ,50, "m/s")    #Calls the Sliders class for the variables needed with the Name, start val, Max, Min, pos, unit
            Acceleration = Slider("Acceleration", 9.8 , 17, 1 ,110,"m/s²")
            Time = Slider("Time", 12,25,1,170, "s")
            Displacment = Slider("Height", 30 ,100,0, 230, "m")
            Theta = Slider("Theta", 45,90,0,290, "°")
            slides = [Velocity, Acceleration, Time,Displacment,Theta]
            message = font.render("",False,WHITE)
            message2 = font.render("",False,WHITE)
            
            Missing_Amount=1
            counter=0
            Value_inputs=True
            while Value_inputs==True:                                       #Starts the slidders loop
                DisplayList=[slides[0],slides[1],slides[2],slides[3],slides[4]]
                counter=0
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key ==pygame.K_SPACE:                      #If you click space to start the program...
                            for i in DisplayList:
                                if i.display == False or i.display == 'Gucci':
                                    counter+=1
                            if counter>Missing_Amount:                      #If there isn't enough data 
                                message = font.render("You don't have enough data",False,BLACK)
                                middle = True
                            if counter == 0:                                #If theres too much data, the program will ignore one value
                                message = font.render('Contridictions might occour, Time will be recalculated just incase',False,BLACK)
                                middle = False
                                redraw_2d()
                                pygame.display.update()
                                pygame.time.delay(3000)
                                Time.string='None'
                                Value_inputs=False
                                
                            elif counter==Missing_Amount:                   #If theres enough data
                                if Acceleration.display==True and Time.display==True:   #If one of these two are not the missing value, the program will not start
                                    message=font.render('Acceleration or Time must be the only missing value',False,BLACK)
                                if Acceleration.display==True and (Time.display==False or Time.display=='Gucci'):   #If one is missing the program will begin
                                    message=font.render('The program will begin now',False,BLACK)
                                    middle = True
                                    redraw_2d()
                                    pygame.display.update()
                                    pygame.time.delay(3000)
                                    Value_inputs=False
                                if (Acceleration.display==False or Acceleration.display=='Gucci') and Time.display==True:   #If one is missing the program will begin
                                    message=font.render('The program will begin now',False,BLACK)
                                    middle = True
                                    redraw_2d()
                                    pygame.display.update()
                                    pygame.time.delay(3000)
                                    Value_inputs=False
                                    
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:      #If you click the slider button, you can move it with your mouse position
                        pos = pygame.mouse.get_pos()
                        for s in slides:
                            if s.button_rect.collidepoint(pos):
                                s.hit = True
                    elif event.type == pygame.MOUSEBUTTONUP:
                        for s in slides:
                            s.hit = False
                redraw_2d()                                         #Redraws the sliders
                
        if thing=='1D':                                                             #If you chose the 1D component     
            Velocity = Slider("Initial Velocity", 10 ,100 ,0 ,50, "m/s")            #Calls the Sliders class for the variables needed with the Name, start val, Max, Min, pos, unit
            Velocity_Final = Slider("Velocity_Final", 50 , 100, 0,110,"m/s")
            Time = Slider("Time", 5,50,1,170, "s")
            Acceleration = Slider("Acceleration.", 10 ,25,0, 230, "m/s²")
            Displacment = Slider("Displacment", 125,250,1,290, "m")
            slides = [Velocity, Velocity_Final, Time,Acceleration,Displacment]
            message = font.render("",False,WHITE)
            message2 = font.render("",False,WHITE)
            
            Missing_Amount=2
            counter=0
            Value_inputs=True
            
            while Value_inputs==True:
                DisplayList=[slides[0],slides[1],slides[2],slides[3],slides[4]]
                counter=0
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key ==pygame.K_SPACE:                          #If you press SPACE
                            for i in DisplayList:
                                if i.display == False or i.display == 'Gucci':
                                    counter+=1
                            if counter>Missing_Amount:                          #If there is not enough data
                                message = font.render("You don't have enough data",False,WHITE)
                                middle = True
                            if counter == 0 or counter == 1:                    #If there is too much data
                                message = font.render('Contridictions might occour, Please decrease the number of variables present',False,WHITE)
                                middle = False
                            elif counter==Missing_Amount:                       #If there is just enough data 
                                message = font.render('The program will begin now',False,WHITE)
                                middle = True
                                redraw_1d()
                                pygame.display.update()
                                pygame.time.delay(3000)
                                Value_inputs=False
                           
                                       
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:                  #If you click the slider button, you can move it with your mouse position
                        pos = pygame.mouse.get_pos()
                        for s in slides:
                            if s.button_rect.collidepoint(pos):
                                s.hit = True
                    elif event.type == pygame.MOUSEBUTTONUP:
                        for s in slides:
                            s.hit = False
                redraw_1d()                                                     #Redraws the sliders

        ###############2D######################
        if thing=='2D':                                                                         #If you chose 2D section 
            def redraw():
                #-=Redraws the ball while running the program-=#
                pygame.draw.line(screen,WHITE,(ballX+40,HEIGHT-90),(ballX+40,HEIGHT-90),1)
                rectbaseball.center = (ballX+40,ballY-100)
                screen.blit(baseball,rectbaseball)
                pygame.display.update()
                pygame.draw.circle(screen,BLACK,(ballX+40,ballY-100),9,0)
                pygame.draw.circle(screen,WHITE,(ballX2+40,ballY2-100),3,0)
                
            def redraw_start():
                #-=Redraws the starting lines and sections=-#
                pygame.draw.line(screen,WHITE,(0,Height-100),(20,Height-100),1)
                pygame.draw.line(screen,WHITE,(10,Height-100),(10,HEIGHT-90),1)
                pygame.draw.line(screen,WHITE,(0,HEIGHT-90),(20,HEIGHT-90),1)
                
            def redraw_end():
                #-=Redraws the end projectile motion=-#
                font = pygame.font.SysFont("Ariel Black",30)
                message = font.render("Initial Values",1,BLACK)
                pygame.draw.line(screen,WHITE,(40,HEIGHT-90),(ballX+40,HEIGHT-90),1)
                pygame.draw.line(screen,WHITE,(40,HEIGHT-100),(40,HEIGHT-80),1)
                pygame.draw.line(screen,WHITE,(ballX+40,HEIGHT-100),(ballX+40,HEIGHT-80),1)
                rectbaseball.center = (ballX+40,ballY-100)
                screen.blit(baseball,rectbaseball)
                pygame.display.update()

            def ledge(Color):
                #-=The redraw for the legend=-#
                pygame.draw.rect(screen,GREY,(615,5,300,170))
                font = pygame.font.SysFont("Arial",int(15))
                screen.blit(base_extra,(582,117-110))
                Velocity1 = font.render('Vi: '+str(round(vi,2))+' m/s',1,Color)
                screen.blit(Velocity1,(620,120-110))
                Velocity2 = font.render('Vf: '+str(round(VF,2))+' m/s ['+str(angle)+'° From the horizontal]',1,Color)
                screen.blit(Velocity2,(620,140-110))
                Height = font.render('h: '+str(round(d,4))+' m',1,Color)
                screen.blit(Height,(620,160-110))
                Time = font.render('Δt: '+str(round(timeA,2))+' s',1,Color)
                screen.blit(Time,(620,180-110))
                Accelaration = font.render('a: '+str(round(a,2))+' m/s²',1,Color)
                screen.blit(Accelaration,(620,200-110))
                Range = font.render('The range is:'+str(length)+' m',1,Color)
                screen.blit(Range,(620,220-110))
                Max = font.render('The time at the max height is: '+str(timeB/2)+' s',1,Color) 
                screen.blit(Max,(620,240-110))
                Max2 = font.render('The max height is '+str(round(maxH,2))+' m',1,Color)
                screen.blit(Max2,(620,260-110))
                pygame.display.update()
                
            #-=Creates the appropriate values depending on its objects string=-#
            for i in range(len(DisplayList)):
                if DisplayList[i].string=='None':
                    DisplayList[i].val = ''
                else:
                    DisplayList[i].val=float(DisplayList[i].string)

            #-=Each variable gets its objects value=-#
            vi=Velocity.val
            a=Acceleration.val
            t=Time.val
            d=Displacment.val
            theta=Theta.val
            theta=theta*(math.pi/180)  #Convert to stupid rads
            #-=Initial Velocity's component calculation=-#
            yVi=round(vi*(math.sin(theta)),2)
            xVi=round(vi*(math.cos(theta)),2)
            
            if t=='' or (t!='' and a!=''):              #If the time is missing or both are missing
                #-=Time and Range calculation-=#
                timeA=quad_form((-a/2),yVi,d)
                length=round(xVi*timeA,2)
                #-=Final Velocity calculation-=#
                yVf=round(-formula2_eq(yVi,-0,-a,timeA,-0,'vf'),2)
                VF=round(math.sqrt(xVi**2+yVf**2),2)
                angle=math.atan(yVf/xVi)
                angle=round(angle*(180/math.pi),2)
                #-=Max height calculation=-#
                timeB=quad_form((-a/2),yVi,0)
                maxH=d+round(formula4_eq(yVi,-0,-a,timeB/2,-0,'d'),2)
            if a=='':
                #-=Time and Range calculation=-#
                timeA=t
                length=round(xVi*timeA,2)
                #-=Acceleration calculation=-#
                a=-round(formula4_eq(yVi,-0,-0,timeA,-d,'a'),2)
                #-=Final Velocity calculation=-#
                yVf=round(-formula2_eq(yVi,-0,-a,t,-0,'vf'),2)
                VF=round(math.sqrt(xVi**2+yVf**2),2)
                angle=math.atan(yVf/xVi)
                angle=round(angle*(180/math.pi),2)
                #-=Max height calculation=-#
                timeB=quad_form((-a/2),yVi,0)
                maxH=d+round(formula4_eq(yVi,-0,-a,timeB/2,-0,'d'),2)

            #-=Creates a Multiplyer to ensure the program lands within the limits of the screen=-#
            multList=[]
            if ((WIDTH-200)/length)>=1:
                multList.append((WIDTH-200)/length)
            if ((HEIGHT-150)/maxH)>=1:
                multList.append((HEIGHT-150)/maxH)
            multiplyer=(min(multList))
            if ((WIDTH-200)/length)<1 or ((HEIGHT-150)/maxH)<1:                                      
                count=0                                                            
                while True:                                                         
                    if (length*(count+0.01))<(WIDTH-200) and (maxH*(count+0.01))<(HEIGHT-150):   
                        count+=0.01                                                 
                    else:                                                          
                        multiplyer=count 
                        break

            screen=pygame.display.set_mode((WIDTH,HEIGHT))
            
            screen.blit(background2,(0,0))
            height=round(formula4_eq(yVi,-0,-a,0,-0,'d'))
            Height=int(HEIGHT-multiplyer*(d+height))
            redraw_start()
            
            legend=False
            end=False
            #-=Starts a loop for the program to run=-#
            for t in range(int(timeA*1000)):
                t=t/1000                                            #Causes the time to go 1/1000 the speed so the program dosnt go to fast
                ballX=int((xVi*t)*multiplyer)                       #Calculates the Balls X position 
                height=round(formula4_eq(yVi,-0,-a,t,-0,'d'),2)
                ballY=int(HEIGHT-multiplyer*(d+height))             #Calculates the Balls Y position
                if t>(200/1000):                                    #Creates the secondary path following the ball
                    t=t-(200/1000)
                    ballX2=int((xVi*t)*multiplyer)
                    height=round(formula4_eq(yVi,-0,-a,t,-0,'d'),2)
                    ballY2=int(HEIGHT-multiplyer*(d+height))
                else:                                               #If the ball is to close to the secondary ball, it will not move
                    ballX2=0
                    ballY2=int(HEIGHT-multiplyer*d)    
                redraw()                                            #Redraws the screen
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:              #Pressing down displays the legend
                            ledge(BLACK)
                        if event.key == pygame.K_r:                 #pressing R restarts the program
                            for i in DisplayList:
                                i.val=0
                                i.string=''
                            message = font.render("",False,WHITE)
                            end=True
                            restart = True                          #Restarts the program
                            
            while end==False:                                       #After the ball lands
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:              #Pressing down displays the legend
                            ledge(BLACK)
                        if event.key == pygame.K_r:                 #pressing R restarts the program
                            for i in DisplayList:
                                i.val=0
                                i.string=''
                            message = font.render("",False,WHITE)
                            end=True
                            restart = True                          #Restarts the program
                        if event.key == pygame.K_h:
                            restart=False
                            start_program = False
                            end = True
                            
                redraw_end()                                        #Redraws the end screen

        elif thing=='1D':                                           #If the component is 1D
            #-=Creates the appropriate values depending on its objects string=-#        
            for i in range(len(DisplayList)):
                if DisplayList[i].string=='None':
                    DisplayList[i].val = ''
                else:
                    DisplayList[i].val=float(DisplayList[i].string)
            #-=Each variable gets its objects value=-#                
            vi=Velocity.val
            a=Acceleration.val
            vf=Velocity_Final.val
            d=Displacment.val
            t=Time.val
            #-=Calculates the missing variables depending on the the ones givin=-#
            for e in range(2):
                if vi=='':
                    if vf=='':
                        vf,vi=formula5_eq(vi,vf,a,t,d,'vf',formula4_eq(vi,vf,a,t,d,'vi'))
                    elif a=='':
                        vi,a=formula3_eq(vi,vf,a,t,d,'vi'),formula5_eq(vi,vf,a,t,d,'a')
                    elif t=='':
                        vi,t=formula6_eq(vi,vf,a,t,d,'vi'),formula5_eq(vi,vf,a,t,d,'t')
                    elif d=='':
                        vi,d=formula2_eq(vi,vf,a,t,d,'vi'),formula5_eq(vi,vf,a,t,d,'d')
                    else:
                        vi=formula2_eq(vi,vf,a,t,d,'vi')
                        
                elif vf=='':
                    if vi=='':
                        vf,vi=formula5_eq(vi,vf,a,t,d,'vf'),formula4_eq(vi,vf,a,t,d,'vi')
                    elif a=='':
                        vf,a=formula3_eq(vi,vf,a,t,d,'vf'),formula4_eq(vi,vf,a,t,d,'a')
                    elif t=='':
                        vf,t=formula6_eq(vi,vf,a,t,d,'vf'),formula4_eq(vi,vf,a,t,d,'t')
                    elif d=='':
                        vf,d=formula2_eq(vi,vf,a,t,d,'vf'),formula4_eq(vi,vf,a,t,d,'d')
                    else:
                        vf=formula6_eq(vi,vf,a,t,d,'vf')
                        
                elif a=='':
                    if vf=='':
                        a,vf=formula4_eq(vi,vf,a,t,d,'a'),formula3_eq(vi,vf,a,t,d,'vf')
                    elif vi=='':
                        a,vi=formula5_eq(vi,vf,a,t,d,'a'),formula3_eq(vi,vf,a,t,d,'vi')
                    elif t=='':
                        a,t=formula6_eq(vi,vf,a,t,d,'a'),formula3_eq(vi,vf,a,t,d,'t')
                    elif d=='':
                        a,d=formula2_eq(vi,vf,a,t,d,'a'),formula3_eq(vi,vf,a,t,d,'d')
                    else:
                        a=formula2_eq(vi,vf,a,t,d,'a')
                        
                elif t=='':
                    if vf=='':
                        t,vf=formula4_eq(vi,vf,a,t,d,'t'),formula6_eq(vi,vf,a,t,d,'vf')
                    elif a=='':
                        t,a=formula3_eq(vi,vf,a,t,d,'t'),formula6_eq(vi,vf,a,t,d,'a')
                    elif vi=='':
                        t,vi=formula5_eq(vi,vf,a,t,d,'t'),formula6_eq(vi,vf,a,t,d,'vi')
                    elif d=='':
                        t,d=formula2_eq(vi,vf,a,t,d,'t'),formula6_eq(vi,vf,a,t,d,'d')
                    else:
                        t=formula2_eq(vi,vf,a,t,d,'t')
                        
                elif d=='':
                    if vf=='':
                        d,vf=formula4_eq(vi,vf,a,t,d,'d'),formula2_eq(vi,vf,a,t,d,'vf')
                    elif a=='':
                        d,a=formula3_eq(vi,vf,a,t,d,'d'),formula2_eq(vi,vf,a,t,d,'a')
                    elif t=='':
                        d,t=formula6_eq(vi,vf,a,t,d,'d'),formula2_eq(vi,vf,a,t,d,'t')
                    elif vi=='':
                        d,vi=formula5_eq(vi,vf,a,t,d,'d'),formula2_eq(vi,vf,a,t,d,'vi')
                    else:
                        d=formula4_eq(vi,vf,a,t,d,'d')


            def redraw():
                #-=Redraws the ball while running the program-=#
                pygame.draw.line(screen,WHITE,(ballX+40,HEIGHT-90),(ballX+40,HEIGHT-90),1)
                rectbaseball.center = (ballX+40,HEIGHT-120)
                screen.blit(baseball,rectbaseball)
                pygame.display.update()
                pygame.draw.circle(screen,BLACK,(ballX+40,HEIGHT-120),9,0)
                pygame.draw.circle(screen,WHITE,(ballX2+40,HEIGHT-120),3,0)

            def redraw_end():
                #-=Redraws the end projectile motion=-#
                pygame.draw.line(screen,WHITE,(40,HEIGHT-90),(ballX+40,HEIGHT-90),1)
                pygame.draw.line(screen,WHITE,(40,HEIGHT-100),(40,HEIGHT-80),1)
                pygame.draw.line(screen,WHITE,(ballX+40,HEIGHT-100),(ballX+40,HEIGHT-80),1)
                rectbaseball.center = (ballX+40,HEIGHT-120)
                screen.blit(baseball,rectbaseball)
                pygame.display.update()
                    
            def ledge(Color):
                #-=The redraw for the legend=-#
                pygame.draw.rect(screen,GREY,(795,5,300,105))
                font = pygame.font.SysFont("Arial",int(16))
                screen.blit(base_extra,(762,117-110))
                Velocity1 = font.render('Vi: '+str(round(vi,2))+' m/s',1,Color)
                screen.blit(Velocity1,(800,120-110))
                Velocity2 = font.render('Vf: '+str(round(vf,2))+' m/s',1,Color)
                screen.blit(Velocity2,(800,140-110))
                Displacment = font.render('Δd: '+str(round(d,4))+' m',1,Color)
                screen.blit(Displacment,(800,160-110))
                Time = font.render('Δt: '+str(round(time,2))+' s',1,Color)
                screen.blit(Time,(800,180-110))
                Accelaration = font.render('a: '+str(round(a,2))+' m/s²',1,Color)
                screen.blit(Accelaration,(800,200-110))
                pygame.display.update()

                
            screen.blit(background2,(0,0))
            
            legend=False
            end=False
            
            time=t
            count=0
            
            #-=Creates a Multiplyer to ensure the program lands within the limits of the screen=-#
            while True:                                                         
                if (d*(count+0.01))<(WIDTH-200):       
                    count+=0.01                                                
                else:                                                           
                    multiplyer=count 
                    break
                
            #-=Starts a loop for the program to run=-#        
            for t in range(int(time*1000)):
                t=t/1000                                                        #Causes the time to go 1/1000 the speed so the program dosnt go to fast
                ballX=int(formula4_eq(vi,vf,a,t,d,'d')*multiplyer)              #Calculates the Balls x position
                if t>(500/1000):
                    t=t-(500/1000)
                    ballX2=int(formula4_eq(vi,vf,a,t,d,'d')*multiplyer)         #Calculates the balls secondary position
                else:
                    ballX2=0

                redraw()                                                        #Redraws the screen
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:                          #If you press down the legend apears
                            ledge(BLACK)
                        if event.key == pygame.K_r:                             #If you press r the program restarts
                            for i in DisplayList:
                                i.val=0
                                i.string=''
                            message = font.render("",False,WHITE)
                            end=True
                            restart = True                                      #Restarts the program
                        if event.key == pygame.K_h:
                            restart=False
                            start_program = False
                            end = True

            while end == False:            
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:                          #If you press down the legend apears
                            ledge(BLACK)
                        if event.key == pygame.K_r:                             #If you press r the program restarts
                            for i in DisplayList:
                                i.val=0
                                i.string=''
                            message = font.render("",False,WHITE)
                            end=True
                            restart = True                                      #Restarts the program
                        if event.key == pygame.K_h:
                            restart=False
                            start_program = False
                            end = True
                redraw_end()                                                    #Redraws the end screen

        
