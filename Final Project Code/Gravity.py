def gravity_run():
    import math
    import pygame
    from random import randint
    ##from Inputs_ting import Inputs
    ##from Equations import formula1_eq,formula2_eq,formula3_eq,formula4_eq

    G=(6.67*10**-11)                    #Gravitational Constant

    def formula3_eq(v,G,m1,r,desired):
        if 'v'==desired:
            return ((G*m1)/r)**(1/2) #rearanged formula for v
        elif 'r'==desired:
            return (G*m1)/(v**2) #rearanged formula for r
        elif 'm1'==desired:
            return ((v**2)*r)/G #rearanged formula for m1

    def formula4_eq(r,m1,T,G,desired):
        if 'r'==desired:
            return ((G*m1*T**2)/(4*math.pi**2))**(1/3) #rearanged formula for r
        elif 'm1'==desired:
            return ((r**3)*4*math.pi**2)/(G*T**2) #rearanged formula for m1
        elif 'T'==desired:
            return (((r**3)*4*math.pi**2)/(G*m1))**(1/2) #rearanged formula for T

    WIDTH,HEIGHT=900,650
    pygame.init()

    WHITE =  (255, 255, 255)#---------------------#
    BLUE =   (0, 0, 255)                          #|
    YELLOW = (255, 255, 0)                        #|Declaring
    RED =    (255, 0, 0)                          #|
    GREEN =  (0, 255, 0)                          #|Colors
    BLACK =  (0,  0,  0)                          #|
    GREY =   (192, 192, 192)#---------------------#
    TRANS = (1, 1, 1)
    ORANGE = (200, 100, 50)

    class Inputs():
        def __init__(self, name, pos, unit):
            self.xpos = 700                                 # x-location on screen
            self.ypos = pos                                 # y-pos on screen
            self.unit = unit                                # Sliders corrisponding unit
            self.string = ''                                # Sliders string val
            self.val = None                                 # Sliders value
            self.surf = pygame.surface.Surface((165, 50))   # Creates the sliders surface
            self.surf2 = pygame.surface.Surface((50, 50))   # Creates the secondary surface
            self.display="Gucci"                            # Starting display for the dmall box
            self.boxCol=GREY                                # Starting display color for the smaller box (Starts as nutral color)             
            
            
            self.txt_surf = font2.render(name, 1, BLACK)                #Creates the text for the sliders
            self.txt_rect = self.txt_surf.get_rect(center=(82, 15))
            
            pygame.draw.rect(self.surf, GREY, [0, 0, 165, 50], 3)       #Creates the display
            pygame.draw.rect(self.surf, ORANGE, [10, 10, 145, 10], 0)

            pygame.draw.rect(self.surf2, self.boxCol, [0, 0, 50, 50], 3)#Creates the secondary display
            
            self.surf.blit(self.txt_surf, self.txt_rect)                #Displays the text for the sliders
     

        def draw(self):
            surf = self.surf.copy()                                 #Makes a copy of both surfaces
            surf2= self.surf2.copy()
                
            if len(self.string)>=1:                                 #If the value is too big it converts to sci notation form
                self.val=float(self.string)
            elif len(self.string)==0:
                self.val=''
            if len(self.string)>16:
                self.val=float(self.string)
                self.val=("{:.2e}".format(self.val))
                self.val=float(self.val)
            pygame.draw.rect(self.surf2, self.boxCol, [0, 0, 50, 50], 3)    #Creates a rectangle of to display on the secondary surface
            
            if self.display==True or self.display=="Gucci":         # Displays the surface when its display is not False        
                screen.blit(surf,(self.xpos,self.ypos))
                value = font2.render(str(self.val)+self.unit,False,WHITE)
                screen.blit(value,(self.xpos+10,self.ypos+30))

            screen.blit(surf2,(self.xpos-50,self.ypos))             #Displays the secondary surface
            
        def move(self):
            mouseX,mouseY=pygame.mouse.get_pos()
            if mouseX>self.xpos and mouseX<self.xpos+165 and mouseY>self.ypos and mouseY<self.ypos+50: #Finds if the mouse is within the primary surface location
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:                #Pressing the keyboard will add the values to the string 
                        if event.key == pygame.K_0:
                            self.string+='0'
                        elif event.key == pygame.K_1:
                            self.string+='1'
                        elif event.key == pygame.K_2:
                            self.string+='2'
                        elif event.key == pygame.K_3:
                            self.string+='3'
                        elif event.key == pygame.K_4:
                            self.string+='4'
                        elif event.key == pygame.K_5:
                            self.string+='5'
                        elif event.key == pygame.K_6:
                            self.string+='6'
                        elif event.key == pygame.K_7:
                            self.string+='7'
                        elif event.key == pygame.K_8:
                            self.string+='8'
                        elif event.key == pygame.K_9:
                            self.string+='9'
                        elif event.key == pygame.K_BACKSPACE:
                            self.string=self.string[0:-1]
                        elif event.key == pygame.K_PERIOD:
                            self.string+='.'
            elif mouseX>self.xpos-50 and mouseX<self.xpos and mouseY>self.ypos and mouseY<self.ypos+50: #Finds if the mouse is within secondary surface location
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:                    #If the mouse is clicked changes the display property and and secondary surface color to match
                        if event.button == 1:
                            if self.display==True:
                                self.display=False
                                self.boxCol=RED
                            elif self.display==False or self.display=="Gucci":
                                self.display=True
                                self.boxCol=GREEN
                        pygame.time.delay(100)

    #-=Creates the Screen-=#
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    #-=Fonts for start and main program=-#
    font = pygame.font.SysFont("Arial",int(18))
    font1 = pygame.font.SysFont("Arial",int(30))
    font2 = pygame.font.SysFont("Verdana",12)
    bigfont = pygame.font.SysFont("Arial",int(21))
    #-=Creates background pictures=-#
    background=pygame.image.load("background_gravity.jpg")
    background=pygame.transform.scale(background,(WIDTH,HEIGHT))
    #-=List containing all the planets names=-#
    planet_names=['Mars.png','Neptune.png','Saturn.png','Uranus.png','Venus.png']#,'Earth.png']
    #-=Chooses a random planet as the main planet and loads the pictures=-#
    planet=randint(0,len(planet_names)-1)
    planet_name=planet_names[planet]
    pic1=pygame.image.load(planet_name).convert_alpha()
    pic1_extra=pygame.image.load(planet_name).convert_alpha()
    pic1_extra=pygame.transform.scale(pic1_extra,(30,30))
    #-=Loads the satelite picture=-#
    pic2_image = "satelite.png"
    pic2=pygame.image.load(pic2_image).convert_alpha()
    pic2_extra=pygame.image.load(pic2_image).convert_alpha()
    pic2_extra=pygame.transform.scale(pic2_extra,(30,30))
    #-=Loads all the images for the notes=-#
    Restart=pygame.image.load('Restart.png').convert_alpha()
    CTRL=pygame.image.load('CTRL.png').convert_alpha()
    Scroll=pygame.image.load('Scroll.png').convert_alpha()
    Click=pygame.image.load('Click.png').convert_alpha()
    Notes_Pic=pygame.image.load('Notes.png').convert_alpha()
    #-=Scales all the images for the notes=-#
    Restart=pygame.transform.scale(Restart,(40,40))
    CTRL=pygame.transform.scale(CTRL,(40,40))
    Scroll=pygame.transform.scale(Scroll,(45,45))
    Click=pygame.transform.scale(Click,(45,45))
    Notes_Pic=pygame.transform.scale(Notes_Pic,(40,40))
    ###-=All Formulas Used=-####
    formula1='Fg=(G • m1 • m2)/(r**2)'
    formula2='g=(G•M)/(r**2)'
    formula3='v=sqrt((G•M)/r)'
    formula4='r=((G•M•T**2)/(4•π**2))**(1/3)'

    #Calls the Inputs class for the variables needed with the Name, pos, unit=-#
    Mass1 = Inputs("Mass1", 25, "kg")
    Radius = Inputs("Radius", 100, "m")
    Period = Inputs("Period", 175, "s")
    slides = [Mass1, Radius, Period]
    message = font.render("",False,WHITE)
    #-=Loads all messages for the main screen=-#
    information0 = font.render("                     -= Information and Rules =-",False,WHITE)
    information1 = font.render("- Leave one value as unknown to allow the program to run properly.",False,WHITE)
    information2 = font.render("- To set values, move your mouse inside the intened box and type.",False,WHITE)
    information3 = font.render("- Click on the smaller black box on the left to validate and unvalidate the values.",False,WHITE)
    information4 = font.render("- Press Space-Bar when you are ready to start.",False,WHITE)
    information5 = font.render("- Press down arrow to bring up the legend when running the program.",False,WHITE)
    information6 = font.render("- Press 'n' to display the notes and 'r' to restart.",False,WHITE)
    information7 = font.render("- Press 'h' to go back to the home page.",False,WHITE)

    middle = True

    def fade(width,height,redraw_screen):   #Fade function for fading from sliders to program for visual pleasure
        fade=pygame.Surface((width,height))
        fade.fill(BLACK)
        for alpha in range(0,300):
            fade.set_alpha(alpha)
            redraw_screen()
            screen.blit(fade,(0,0))
            pygame.display.update()
            pygame.time.delay(1)
            
    def Rfade(width,height,redraw_screen): #Reverse Fade function for fading from program to sliders for visual pleasure
        fade=pygame.Surface((width,height))
        fade.fill(BLACK)
        for alpha in reversed(range(0,300)):
            fade.set_alpha(alpha)
            redraw_screen()
            screen.blit(fade,(0,0))
            pygame.display.update()
            pygame.time.delay(1)
            
    def redraw_Inputs():                    #Redraws the inputs while in the input selection
        screen.blit(background,(0,0))
        for s in slides:                    #Draws the sliders
            s.draw()
            s.move()
        if middle:
            screen.blit(message,(280,300))
        else:
            screen.blit(message,(100,300))
        #-=Displays messages=-#
        screen.blit(information0,(10,10))        
        screen.blit(information1,(10,40))
        screen.blit(information2,(10,70))
        screen.blit(information3,(10,100))
        screen.blit(information4,(10,130))
        screen.blit(information5,(10,160))
        screen.blit(information6,(10,190))
        screen.blit(information7,(10,220))
        
    unit='gravity'
    while unit=='gravity': #While the visualizer is set to gravity
        Missing_Amount=1
        counter=0
        Value_inputs=True
        while Value_inputs==True: #Starts the slidders loop
            redraw_Inputs()                                 #Redraws the inputs
            DisplayList=[slides[0],slides[1],slides[2]]
            counter=0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:         #if click space to start the program...
                        for i in DisplayList:
                            if i.display == False or i.display=="Gucci" or (i.display==True and i.val==''):
                                counter+=1
                                i.val = ''
                        if counter>Missing_Amount:          #If theres not enough data
                            middle = True
                            message = font1.render("You don't have enough data.",False,WHITE)
                        if counter==0:                      #If theres to much data, the program will ignore one value
                            middle = False
                            message = bigfont.render('Contridictions might occour, Period will be recalculated just incase.',False,WHITE)
                            redraw_Inputs()
                            pygame.display.update()
                            pygame.time.delay(4000)
                            middle = True
                            message = font1.render('The program will begin now.',False,WHITE)
                            fade(WIDTH,HEIGHT,redraw_Inputs)
                            Value_inputs=False
                            Period.val=''
                        elif counter==Missing_Amount:       #If theres just enough data
                            middle = True   
                            message = font1.render('The program will begin now.',False,WHITE)
                            redraw_Inputs()
                            pygame.display.update()
                            pygame.time.delay(4000)
                            fade(WIDTH,HEIGHT,redraw_Inputs)
                            Value_inputs=False
                                 
            pygame.display.update()
            
        #-=Each variable gets its objects value=-#        
        r=Radius.val
        m1=Mass1.val
        T=Period.val

        #-=All other variables are givin the "missing" attrabute=-#
        Fg,Gf,m2,v='','','',''

        #-=Calculates all missing values-=
        for e in range(3):                          #In a loop so if it finds one it can be used to find others
            VarList3=[v,m1,r]
            VarList4=[T,m1,r]
            count3=0
            count4=0
              
            for i in range(3):
                if VarList3[i]=='':
                    count3+=1
                if VarList4[i]=='':
                    count4+=1
                    
            if count3==1:
                if v=='':
                    v=formula3_eq(v,G,m1,r,'v')
                elif m1=='':
                    m1=formula3_eq(v,G,m1,r,'m1')
                elif r=='':
                    r=formula3_eq(v,G,m1,r,'r')
            if count4==1:
                if r=='':
                    r=formula4_eq(r,m1,T,G,'r')
                elif m1=='':
                    m1=formula4_eq(r,m1,T,G,'m1')
                elif T=='':
                    T=formula4_eq(r,m1,T,G,'T')

        def circular_orbit(center, radius, speed, t):               #Function used to find the position in a circular orbit 
            theta = math.fmod(t * speed, math.pi * 2)
            c = math.cos(theta)
            s = math.sin(theta)
            return center[0] + radius * c, center[1] + radius * s

        def ledge():
            #-=The redraw for the legend=-#
            Radius = Radiusfont.render('r: '+str(round(radius,2))+' m',1,WHITE)
            screen.blit(Radius,(WIDTH/2+5,HEIGHT/2+(R1+(r+2*R1))/2-FontSize))

            screen.blit(pic1_extra,(7,117-110))
            mass1 = font.render('Mass: '+str(round(m1,2))+' Kg',1,WHITE)
            screen.blit(mass1,(45,120-110))
            
            screen.blit(pic2_extra,(7,185-110))
            Velocity = font.render('Velocity: '+str(round(v,4))+' m/s',1,WHITE)
            screen.blit(Velocity,(45,180-110))
            Period = font.render('Period: '+str(round(T,2))+' s',1,WHITE)
            screen.blit(Period,(45,200-110))

            Speed = font.render('Speed: '+str(round(speed,2))+'X',1,WHITE)
            screen.blit(Speed,(10,HEIGHT-30))
            
        def redraw():
            #-=Redraws all aspects such as planets, Notes, and legend-=#
            if notes==False:
                screen.fill(BLACK)
               
                pygame.draw.circle(screen,YELLOW,(int(SunX),int(HEIGHT/2)),int(SunSize),0)
                pygame.draw.circle(screen,WHITE,(int(WIDTH/2),int(HEIGHT/2)),int(r+2*R1),int(R3))
                screen.blit(pic1,(WIDTH/2-R1,HEIGHT/2-R1))
                screen.blit(pic2,(ballX-R2,ballY-R2))
                if R2<=4:
                    pygame.draw.circle(screen,RED,(ballX,ballY),int(8),2)
                
                pygame.draw.line(screen,WHITE,(WIDTH/2,HEIGHT/2+int(R1+R1/4)),(WIDTH/2,HEIGHT/2+int(r+2*R1)-R1/2),1)

                if legend==True:
                    ledge()
            if notes==True:
                 Notes()
        def Notes():
            #-=Redraw for the legend tab-=#
            screen.fill(BLACK)
            
            Note = bigfont.render('-=NOTES=-',1,WHITE)
            
            Note_Message = font.render('The sun represents 86400s or one earth day, after one rotation this time has passed',1,WHITE)
            Note_Message2 = font.render('Scaling is blown out of proportion to increase viewability',1,WHITE)
            
            Speed_Message1 = font.render('Right click will slow down the program by 10%',1,WHITE)
            Speed_Message2 = font.render('Left click will speed up the program by 10%',1,WHITE)
            
            Scroll_Message1 = font.render('Scrolling down will zoom the image out',1,WHITE)
            Scroll_Message2 = font.render('Scrolling up will zoom the image in',1,WHITE)
            
            CTRL_Scroll_Message1 = font.render('Holding CTRL and scrolling down will decrease the size of the images if they are too big',1,WHITE)
            CTRL_Scroll_Message2 = font.render('Holding CTRL and scrolling up will increase the size of the images if they are too small',1,WHITE)
            
            Legend_Message = font.render('Pressing the down button will display the legend',1,WHITE)
            Restart_Message = font.render('Pressing "r" will restart the program',1,WHITE)


            screen.blit(Note,Note.get_rect(center=(WIDTH/2, 150)))
            
            screen.blit(Notes_Pic,(WIDTH/2-400,175))
            screen.blit(Note_Message,Note_Message.get_rect(center=(WIDTH/2, 180)))
            screen.blit(Note_Message2,Note_Message2.get_rect(center=(WIDTH/2, 210)))

            screen.blit(Click,(WIDTH/2-220,250))
            screen.blit(Speed_Message1,Speed_Message1.get_rect(center=(WIDTH/2, 260)))
            screen.blit(Speed_Message2,Speed_Message2.get_rect(center=(WIDTH/2, 290)))

            screen.blit(Scroll,(WIDTH/2-190,330))
            screen.blit(Scroll_Message1,Scroll_Message1.get_rect(center=(WIDTH/2, 340)))
            screen.blit(Scroll_Message2,Scroll_Message2.get_rect(center=(WIDTH/2, 370)))

            screen.blit(CTRL,(WIDTH/2-420,415))
            screen.blit(Scroll,(WIDTH/2-390,410))
            screen.blit(CTRL_Scroll_Message1,CTRL_Scroll_Message1.get_rect(center=(WIDTH/2, 420)))
            screen.blit(CTRL_Scroll_Message2,CTRL_Scroll_Message2.get_rect(center=(WIDTH/2, 450)))

            screen.blit(Restart,(WIDTH/2-235,500))
            screen.blit(Legend_Message,Legend_Message.get_rect(center=(WIDTH/2, 500)))
            screen.blit(Restart_Message,Restart_Message.get_rect(center=(WIDTH/2, 530)))

            pygame.display.update()

        radius=r
        speed=1
        count=1

        #-=Creates a mass ratio to ensure the planets are not to big to crash the program=-#
        if m2=='':
            m2=1

        mR=m1/m2
        if mR==1:
            R1,R2=10,10
            pass
        else:
            while True:
                if 0<(mR/(10**count))<10:
                    mR=mR/10**count
                    break
                else:
                    count+=1
            R1=mR*300
            R2=mR*100
        counter=1

        #-=Creats a ratio to ensure the program dosnt start at insane values=-#
        while True:
            if r<500:
                if r*(1.05**counter)>=500:
                    r=r*(1.05**counter)
                    secondC=counter
                    while True:
                        if R1*(1.05**secondC)<800:
                            R1=R1*(1.05**secondC)
                            R2=R2*(1.05**secondC)
                            break
                        else:
                            secondC-=1
                    break #-=ask=-, take away and makes it start small =-=-=-=-=-=-=
                else:
                    counter+=1
            elif r>=500:
                if r*(0.95**counter)<=500:
                    r=r*(0.95**counter)
                    R1=R1*(0.95**counter)
                    R2=R2*(0.95**counter)
                    break
                else:
                    counter+=1


        if R1<=8:       #if the images are to small, they dont get any smaller
            R1=8
        if R2<=4:
            R2=4
        #-=All variables needed for the loop=-#    
        mult=0
        i=0
        Ratio=(86400/T)
        SunSize=40
        SunMult=0
        game=True
        legend=False
        delay=15
        R1Counter=0
        R2Counter=0
        thing=0
        end=False
        notes=False
        #-=Transforms the pictures before use=-#
        pic2=pygame.transform.scale(pic2,(int(R2*2),int(R2*2)))
        pic1=pygame.transform.scale(pic1,(int(R1*2),int(R1*2)))
        
        while end==False:                           #-=Loops starting the simulation-=#

            ballX,ballY=circular_orbit([0,0],r+2*R1,(0.000125),i)
            SunX=(i*(1/Ratio)/26.6666666)-((mult*WIDTH*2)+40+40*SunMult)        #Calculates the suns X position
            
            if notes==False:                        #If the notes are not displayed 
                i+=(86400/T)/(1/speed)              #The time increases
                if SunX>WIDTH*2:                    #If the sun passes a rotation it is moved to the its original position
                    mult+=1
                    SunMult+=1
                if SunX<WIDTH/2:                    #If the sun is on the left side of the screen it decreases in size
                    SunSize=SunSize-0.0019*speed
                elif SunX>WIDTH+30:                 #If the sun is not on the screen its values stay constant
                    SunSize+=0
                    SunSize=40
                elif SunX>400:                      #If the sun is on the right side of the screen it increases in size
                    SunSize=SunSize+0.0019*speed
                    
            if notes==True:                         #If the notes are displayed the time stops
                i+=0  
                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  #Pressing down will display the legend
                        if legend==False:
                            legend=True
                        elif legend==True:
                            legend=False
                    elif event.key == pygame.K_r:     #Pressing r will restart the program
                        for i in DisplayList:
                            i.val=0
                            i.string=''
                        end=True
                        message = font.render("",False,WHITE)
                    elif event.key == pygame.K_n:     #pressing N will display the notes
                        if notes==False:
                            notes=True
                        elif notes==True:
                            notes=False
                    elif event.key == pygame.K_h:
                        unit = ''
                        end = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    keys=pygame.key.get_pressed()
                        
                    if event.button == 1:           #right clicking speeds up the program by 10%
                        speed=speed*1.1
                    elif event.button == 3:         #right clicking slows down the program by 10%
                        speed=speed*0.9
                        
                    if keys[pygame.K_LCTRL] and event.button==4:                #If you hold CTRL and scroll up just the images increase in size by 5%
                        R1=R1*1.05
                        R2=R2*1.05
                        pic2=pygame.image.load(pic2_image).convert_alpha()
                        pic1=pygame.image.load(planet_name).convert_alpha()
                        pic2=pygame.transform.scale(pic2,(int(R2*2),int(R2*2)))
                        pic1=pygame.transform.scale(pic1,(int(R1*2),int(R1*2)))
                    elif event.button == 4:                                     #If you just scroll up enerything increase in size by 5%
                        screen.fill(BLACK)
                        R1=R1*1.05
                        R2=R2*1.05
                        r=r*1.05
                        pic2=pygame.image.load(pic2_image).convert_alpha()
                        pic1=pygame.image.load(planet_name).convert_alpha()
                        pic2=pygame.transform.scale(pic2,(int(R2*2),int(R2*2)))
                        pic1=pygame.transform.scale(pic1,(int(R1*2),int(R1*2)))
                        
                    if keys[pygame.K_LCTRL] and event.button==5:                #If you hold CTRL and scroll down just the images decrease in size by 5%
                        R1=R1*0.95
                        R2=R2*0.95
                        pic2=pygame.image.load(pic2_image).convert_alpha()
                        pic1=pygame.image.load(planet_name).convert_alpha()
                        pic2=pygame.transform.scale(pic2,(int(R2*2),int(R2*2)))
                        pic1=pygame.transform.scale(pic1,(int(R1*2),int(R1*2)))
                    elif event.button == 5:                                      #If you just scroll down enerything decreases in size by 5%
                        screen.fill(BLACK)
                        R1=R1*0.95
                        R2=R2*0.95
                        r=r*0.95
                        if R1<=8:       #if the images are to small, they dont get any smaller
                            R1=8
                        if R2<=4:
                            R2=4
                            
                        pic2=pygame.image.load(pic2_image).convert_alpha()
                        pic1=pygame.image.load(planet_name).convert_alpha()
                        pic2=pygame.transform.scale(pic2,(int(R2*2),int(R2*2)))
                        pic1=pygame.transform.scale(pic1,(int(R1*2),int(R1*2)))            
                        
            if int(R2/3)==0:        #Calculating the size of the orbits path
                R3=1
            else:
                R3=R2/3
            
            FontSize=((r+2*R1)*2)/34                                         #Font size of the radius as you scroll
            Radiusfont = pygame.font.SysFont("Arial Black",int(FontSize))    #Creating said font
            ballX=int(WIDTH/2+(int(ballX)))                                  #Calculating the balls x & y position
            ballY=int(HEIGHT/2+(int(ballY)))

            if thing==0:                                                     #If you press r the program fades out
                Rfade(WIDTH,HEIGHT,redraw)
                thing+=1
            else:                                                            #If you dont the program runs normaly
                redraw()
                
            pygame.display.update()
            
        fade(WIDTH,HEIGHT,redraw)
