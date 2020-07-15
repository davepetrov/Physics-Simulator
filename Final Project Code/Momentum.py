import math
import pygame
from math import pi,sin,cos,tan,sqrt,atan,degrees,radians
from time import sleep
from _momentum_sliders import *
def momentum_run():
    #-=-=-=-=Impulse and momnetum =-=-=-=-#
    '''
    Do not type anything for the variable we need to solve for

    ##Example:

    >>> acceleration:
    >>> Force1: 2
    >>> Force2: 2
    >>> Mass: 1.3

    3.08 is the acceleration
    ''' 
    WIDTH, HEIGHT = 900, 650
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (200, 200, 200)      #----------------------------------------------------------------------------------------------# Colors
    ORANGE = (200, 100, 50)
    RED = (255,0,0)
    GREEN = (0,255,0)
    TRANS = (1, 1, 1)
    WHITE = (255,255,255)

    center=(int(WIDTH/2),int(HEIGHT/2))
    full_screen_radius=sqrt((WIDTH/2)**2+(HEIGHT/2)**2)#---------------------------------------------------------------# Screen setting 

    font = pygame.font.SysFont("Arial",int(16))
    font2 = pygame.font.SysFont("Arial",int(21))#--------------------------------------------------------------------------# Font setting 

    choose_image = pygame.image.load('_momentum_choose_image.png')
    twoD_click = pygame.image.load('_momentum_2d_click.png')
    oneD_click = pygame.image.load('_momentum_1d_click.png')
    up=pygame.transform.scale(pygame.image.load("_momentum_arrow_up.png").convert_alpha(),(35,35))
    down=pygame.image.load("_momentum_arrow_down.png")                                           
    down=down.convert_alpha()                                                       
    down=pygame.transform.scale(down,(35,35))#-----------------------------------------------------------------------# Images imported 
    right=pygame.image.load("_momentum_arrow_right.png")                                           
    right=right.convert_alpha()                                                       
    right=pygame.transform.scale(right,(35,35))
    left=pygame.image.load("_momentum_arrow_left.png")                                           
    left=left.convert_alpha()                                                       
    left=pygame.transform.scale(left,(35,35))


    def ratio_conversion(lst):#----------------------------------------------------------------------------------------------# Function that change the speed of the ball to have noticeable velocity difference
        v_max=max([abs(i) for i in lst if i!=0])
        v_min=min([abs(i) for i in lst if i!=0])                                                                                                # Velocity maximum and minimum are chosen from a list of variables 
        if v_max>5:
            ratio=4/v_max                                                                                                                           # If the max velocity if bigger than 5, then find the ratio between the value and 5
            for i in range(len(lst)):
                lst[i]= lst[i]*ratio
        elif v_min<0.7:
            ratio=0.7/v_min                                                                                                                         # If the min velocity is smaller than 0.7, then find the ration between the two values
            for i in range(len(lst)):
                lst[i]= lst[i]*ratio                                                                                                                   # Apply the obtained ratio and apply it to all variables in the list imported
        return lst

    def initial_pos(v1x,v1y,v2x,v2y,ang1,ang2):#------------------------------------------------------------------------# Function that always center the location of collision while inputted variables are reasonable
        ang1=radians(ang1)+pi
        ang2=radians(ang2)+pi                                                                                                                   # The angle formed with the horizontal at which the balls will collide in the center 
        if v1y==0 and v1x!=0:
            if v1x>0:
                ang1=2*pi+pi
            elif v1x<0:
                ang1=2*pi
        if v2y==0 and v2x!=0:                                                                                                                   # Six if statements to check special cases which can cause multiple possibilities 
            if v2x>0:
                ang2=2*pi+pi
            elif v2x<0:
                ang2=2*pi
        
        if v1x==0 and v1y!=0:
            if v1y>0:
                ang1=3*pi/2+pi
            elif v1y<0:                                                                                                                             # Explanation: if any vector has 0, meaning the combined vector is only going vertical or horizontal 
                ang1=pi/2+pi                                                                                                                      # Since trignomitry is used, multiple answer can be abstracted vertical or horizontal angles
        if v2x== 0 and v2y!=0:                                                                                                                 # Therefore, each case must be studied separately
            if v2y>0:
                ang2=3*pi/2+pi
            elif v2y<0:
                ang2=pi/2+pi

        if v1y==0 and v1x==0:
            ang1=0
        if v2y==0 and v2x==0:
            ang2=0
         
        v1=sqrt(v1x**2+v1y**2)                                                                                                              # Find the combined vector 
        v2=sqrt(v2x**2+v2y**2)

        ratio=v1/v2                                                                                                                             # Find the ratio between the combined vectors
        d1=full_screen_radius*ratio                                                                                                       # A distance defined by using the corner of screen and the screen center, and the ratio of two velocities 
        d2=full_screen_radius
        d1x,d1y=d1*cos(ang1),d1*sin(ang1)                                                                                            # separate the component into x and y so it can be used in drawing functions 
        d2x,d2y=d2*cos(ang2),d2*sin(ang2)
        return d1x,d1y,d2x,d2y
        
    def legend(screen,variables):#------------------------------------------------------------------------------------# Function that print message on pygame screen
        myfont = pygame.font.SysFont('Arial', 19)
        font = pygame.font.SysFont('Arial', 23)
        m1_text = myfont.render('Mass 1: '+str(round(variables['mass1'],2))+'kg', False, WHITE)
        screen.blit(m1_text,(45, 10))
        v1_text = myfont.render('Velocity 1: '+str(round(variables['vel1'],2))+'m/s', False, WHITE)
        screen.blit(v1_text,(45, 30))
        m2_text = myfont.render('Mass 2: '+str(round(variables['mass2'],2))+'kg', False, WHITE)
        screen.blit(m2_text,(45, 50))
        v2_text = myfont.render('Velocity 2: '+str(round(variables['vel2'],2))+'m/s', False, WHITE)
        screen.blit(v2_text,(45, 70))
        if int(variables['collision_type'])==1 or int(variables['collision_type'])==2:
            v1f_text = myfont.render('Velocity 1 prime: '+str(round(variables['vel1f'],2))+'m/s', False, WHITE) # WIth different type of collision, different message will be printed 
            screen.blit(v1f_text,(45, 90))
            v2f_text = myfont.render('Velocity 2 prime: '+str(round(variables['vel2f'],2))+'m/s', False, WHITE)
            screen.blit(v2f_text,(45, 110))
        else:
            vf_text = myfont.render('Velocity prime: '+str(round(variables['velf'],2))+'m/s', False, WHITE)
            screen.blit(vf_text,(45, 90))
                                                                                        # If a velocity value is much more than the others, message will be shown 
        if abs(variables['vel1'])>abs(10*variables['vel2']) or abs(variables['vel2'])>abs(10*variables['vel1']):
            print(variables['vel1'],variables['vel2'])
            DIfference_txt = font.render('Difference between veolcities are too big', False, RED)
            screen.blit(DIfference_txt,(300, 400))
                    
    def distance(x,y,x2,y2):#-------------------------------------------------------------------------------------------# Distance function 
        return (round(sqrt((x2-x)**2+(y2-y)**2)))
                

    #Momentum in one dimention
    def ask_for_input(lst,collision_type):#-----------------------------------------------------------------------------# Function that collect inputted data , rearrange data and return the data along with the variable to be solved 
        collision_type=collision_type
        vel1= lst[0]
        mass1 =  lst[1]                                                                                                                         # Values are abstracted from the imported list 
        vel2= lst[2]
        mass2 = lst[3]
        if int(collision_type) ==1 or int(collision_type) ==2:                                                                      # Different type of collision can lead to different final values 
            vel1f= lst[4]
            vel2f= lst[5]
            variables={'collision_type':collision_type,'mass1':mass1,'vel1':vel1,'mass2':mass2,'vel2':vel2,'vel1f':vel1f,'vel2f':vel2f}
        if int(collision_type)==3:
            velf = lst[4]
            variables={'collision_type':collision_type,'mass1':mass1,'vel1':vel1,'mass2':mass2,'vel2':vel2,'velf':velf}# All the values are arranged into a dictionary 
        count_of_empty=0
        for i in variables:
            if len(variables.get(i))==0:                                                                                                    # If any value of dictionary keys is empty string, then it will become the one to be solved 
                solve=i
                count_of_empty+=1
            else:                                                                                                                                   # At the same time, all string values are change into float to allow calculations 
                variables[i]=float(variables.get(i))
        if count_of_empty>1 and collision_type!=1:
            return 'ERROR: Too many empty variables'
        if collision_type==1 and count_of_empty>2:                                                                                  # If there are too many missing variables or none, then a message will be returned
            return 'ERROR: Too many empty variables'
        if count_of_empty==0:
            return 'EXCEPT: All variables found'
        return variables,solve
        
    def find_missing_momentum1D(variables,solve):#--------------------------------------------------------------# Function that take the values and what is to be solved, to calculate the missing value 
        conservation_violated=False
        negative_mass=False                                                                                                                # Two unrealistic cases: negative mass and unconserved energy, two boolean values to be modified 
        collision_type=variables['collision_type']
        if collision_type==1:  # elastic and unelastic                                                                              Elastic collision, where kinetic energy and momentum are all conserved
            mass1,vel1,mass2,vel2,vel1f,vel2f= variables['mass1'],variables['vel1'],variables['mass2'],variables['vel2'],variables['vel1f'],variables['vel2f']
            if solve == 'mass1':
                variables['mass1']=round((mass2*(vel1f+vel1)-2*mass2*vel2)/(vel1-vel1f),2)
                mass1=variables['mass1']
                variables['vel2f']=round(vel2+(mass1*(vel1-vel1f)/mass2),2)
            if solve == 'vel1':
                variables['vel1']=( round((vel1f*(mass1+mass2)-2*mass2*vel2)/(mass1-mass2),2))  #needed to be modified
                vel1=variables['vel1']
                variables['vel2f']=round(vel2+(mass1*(vel1-vel1f)/mass2),2)
            if solve =='mass2':
                variables['mass2']=( round(mass1*(vel1f-vel1)/(2*vel2-vel1f-vel1),2))
                mass2=variables['mass2']
                variables['vel2f']=round(vel2+(mass1*(vel1-vel1f)/mass2),2)
            if solve == 'vel2':
                variables['vel2']=( round((mass1*(vel1f-vel1)+mass2*(vel1f+vel1))/2*mass2,2))                                                                                                                # Equation rearranged in all cases
                vel2=variables['vel2']
                variables['vel2f']=round(vel2+(mass1*(vel1-vel1f)/mass2),2)
            if solve == 'vel1f':
                variables['vel1f']=( round(vel1*(mass1-mass2)/(mass1+mass2)+vel2*2*mass2/(mass1+mass2),2))
                vel1f=variables['vel1f']
                variables['vel2f']=round(vel2+(mass1*(vel1-vel1f)/mass2),2)
            if solve == 'vel2f':
                variables['vel2f']=( round(vel2*(mass2-mass1)/(mass1+mass2)+vel1*2*mass1/(mass1+mass2),2))
                vel2f=variables['vel2f']
                variables['vel1f']=round(vel1+(mass2*(vel2-vel2f)/mass1),2)
            mass1,vel1,mass2,vel2,vel1f,vel2f= variables['mass1'],variables['vel1'],variables['mass2'],variables['vel2'],variables['vel1f'],variables['vel2f']

        if collision_type==2:  #                                                                                                                 Inelastic, kinetic energy not conserved, momentum conserved 
            mass1,vel1,mass2,vel2,vel1f,vel2f= variables['mass1'],variables['vel1'],variables['mass2'],variables['vel2'],variables['vel1f'],variables['vel2f']
            if solve == 'mass1':
                variables['mass1']=round(mass2*(vel2f-vel2)/(vel1-vel1f),2)
            if solve == 'vel1':
                variables['vel1']=round(vel1f+(mass2*(vel2f-vel2)/mass1),2)
            if solve =='mass2':
                variables['mass2']=round(mass1*(vel1-vel1f)/(vel2f-vel2),2)
            if solve == 'vel2':
                variables['vel2']=round(vel2f+(mass1*(vel1f-vel1)/mass2),2)
            if solve == 'vel1f':
                variables['vel1f']=round(vel1+(mass2*(vel2-vel2f)/mass1),2)
            if solve == 'vel2f':
                variables['vel2f']=round(vel2+(mass1*(vel1-vel1f)/mass2),2)
            mass1,vel1,mass2,vel2,vel1f,vel2f= variables['mass1'],variables['vel1'],variables['mass2'],variables['vel2'],variables['vel1f'],variables['vel2f']
            if (1/2*((mass1*vel1**2+mass2*vel2**2)-(mass1*vel1f**2+mass2*vel2f**2)))<0 and 'component_cal' not in variables:
                conservation_violated=True
                
        if collision_type== 3: # completely unelastic                                                                                   Inelastic, kinetic energy not conserved, momentum conserved 
            mass1,vel1,mass2,vel2,velf= variables['mass1'],variables['vel1'],variables['mass2'],variables['vel2'],variables['velf']
            if solve == 'mass1':
                variables['mass1']=( round((mass2*(velf-vel2))/(vel1-velf),2))
            if solve == 'vel1':
                variables['vel1']=( round((mass2*(velf-vel2))/mass1+velf,2))
            if solve == 'mass2':
                variables['mass2']=( round((mass1*(vel1-velf))/(velf-vel2),2))
            if solve == 'vel2':
                variables['vel2']=( round((velf-mass1*(vel1-velf))/mass2,2))
            if solve == 'velf':
                variables['velf']=(round((mass1*vel1+mass2*vel2)/(mass1+mass2),2))
        if variables['mass1']<0 or variables['mass2']<0:
            negative_mass=True
        if conservation_violated==True or negative_mass==True:
            if conservation_violated==True:                                                                                                 # When law of physics is violated, no true value will be returned, instead it will be None
                variables=None
                print("Re-enter values, total kinetic energy is not conserved")
            else:
                print("Re-enter values, unrealistic mass occurred")
                variables=None

        return (variables)
    def redraw_1d(variables):#--------------------------------------------------------------------------------------------# Function to draw animation 
        pygame.init()
        screen=pygame.display.set_mode((WIDTH, HEIGHT))
        if len(variables)==7:                                                                                                                       # Check the number of keys in a dictionary, to determine how many variables are needed to be defined
            m1,m2,v1,v2,v1f,v2f= variables['mass1'],variables['mass2'],variables['vel1'],variables['vel2'],variables['vel1f'],variables['vel2f']
        else:
            m1,m2,v1,v2,v1f,v2f= variables['mass1'],variables['mass2'],variables['vel1'],variables['vel2'],variables['velf'],variables['velf']
        lst_values=[v1,v2,v1f,v2f]
        display=True
        post_col=False                                                                                                                              # A boolean variable that determine when the collision happen
        press=0
        if v1>=0:
            ang1=0                                                                                                                                      # SInce it is 1d, no angles are inputted by user, but the negative/positive sign determine the direction of the velocity
        else:
            ang1=pi
        if v2>=0:
            ang2=0                                                                                                                                      # When velocity is bigger than 0, direction becomes 0 degree; when it is smaller than 0, direction becomes 180 degree

        else:
            ang2=pi
        d1x,d1y,d2x,d2y=initial_pos(v1,0,v2,0,ang1,ang2)                                                                            # initial_pos() is called to determine the initial position of of two ball so that they collide at the very center
        x1=WIDTH/2+d1x
        x2=WIDTH/2+d2x                                                                                                                          # Values returned by the function is added to the center coordinate and initial position determined 
        y=HEIGHT/2
        lst=ratio_conversion(lst_values)                                                                                                     # ratio_conversion() is called to recalculate relative velocity 
        v1,v2,v1f,v2f=lst[0],lst[1],lst[2],lst[3]
        
        

        while display:                                                                                                                              # While loop called to display and redraw the animation 
            screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                                                                                              # When space is pressed, slow down the animation 
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        press+=3
                    if event.key == pygame.K_r:                                                                                             # When r is pressed, the program returns to the value selection
                        fade(WIDTH,HEIGHT)
                        main()
            
            if distance(x1,y,x2,y)<20:                                                                                               # If the object did not touch, they will have the initial velocities                                                                                            
                post_col=True
            if post_col==True:                                                                                                                  # When they collide, the pre-set boolean variable becomes False
             
                act_vel1=v1f
                act_vel2=v2f
            else:
                act_vel1=v1
                act_vel2=v2
        
            x1+=act_vel1                                                                                                                    
            x2+=act_vel2
            indication(x1,y,WHITE)
            indication(x2,y,GREY)
            if m1>m2:
                pygame.draw.circle(screen,WHITE, (int(x1),int(y)), int(12),0)
                pygame.draw.circle(screen,GREY, (int(x2),int(y)), int(8),0)
            if m1<m2:
                pygame.draw.circle(screen,WHITE, (int(x1),int(y)), int(8),0)
                pygame.draw.circle(screen,GREY, (int(x2),int(y)), int(12),0)
            legend(screen,variables)                                                                                                        # Legend function is called to update the velocity and mass
            pygame.display.update()
            pygame.time.delay(press)
        


    print('-'*30)

    def find_missing_momentum2D(lst,collision_type):#-----------------------------------------------------------------# The main function that collects data and calculates the variables for 2d collisions
        collision_type= collision_type
        print("All angles are mandatory to be input")
        vel1= lst[0]
        angle1= lst[1]
        mass1 = lst[2]
        vel2= lst[3]                                                                                                                                    # Variables inside of the function is defined using the imported list of values 
        angle2=lst[4]
        mass2 = lst[5]
        if collision_type =='1' or  collision_type =='2':
            vel1f= lst[6]
            angle1f=lst[7]                                                                                                                              # Separate the cases of elastic, inelastic and completely inelastic
            vel2f= lst[8]
            angle2f=lst[9]
            variables={'collision_type':collision_type,'mass1':mass1,'vel1':vel1,'angle1':angle1,'mass2':mass2,'vel2':vel2,'angle2':angle2,'vel1f':vel1f,'angle1f':angle1f,'vel2f':vel2f,'angle2f':angle2f}
        if collision_type=='3':
            velf =lst[6]
            anglef=lst[7]
            variables={'collision_type':collision_type,'mass1':mass1,'vel1':vel1,'angle1':angle1,'mass2':mass2,'vel2':vel2,'angle2':angle2,'velf':velf,'anglef':anglef}

        count_of_empty=0
        vel_variables={}
        ang=[]
        for i in variables:
            if len(variables.get(i))==0:                                                                                                            # Run through the similar procedure to check the unknown variable
                solve=i                                                                                                                                   # if the value is empty string then it becomes the unknown to be solved
                count_of_empty+=1
            else:                                                                                                                                           # Otherwise it will be convert into float
                variables[i]=float(variables[i])
            
            if 'v' in i :                                                                                                                                   # Make copies of all velocity variables of the dictionary that consist of only velocities
                vel_variables[i]=variables.get(i) 
            if 'g' in i :
                ang.append(variables.get(i))                                                                                                    # Makes copies of all angles variables of the dictionary that consist of only velocities 
        for i in vel_variables:
            for p in reversed(ang):
                vel_variables[i]=(variables.get(i),p)                                                                                           # Create a dictionary that consists of tuples containing velocities and their corresponding angles 
            ang.remove(p)
        if count_of_empty>2:
            return 'ERROR: Too many empty variables'
        if count_of_empty==0:                                                                                                                       # If too much missing values or none, print message 
            return 'EXCEPT: All variables found'

        
        velx_variables={}
        vely_variables={}                                                                                                                               # Create two empty dictionary reserved for velocities of different axis 
        xy_axis=(velx_variables,vely_variables,variables)
        for i in vel_variables:
            if i!=solve:

                velx_variables[i]=round((vel_variables[i][0])*cos(vel_variables[i][1]*pi/180),2)                                # Velocities of each axis is being calculated using the angle assigned and being added into the two dictionary 
                vely_variables[i]=round((vel_variables[i][0])*sin(vel_variables[i][1]*pi/180),2)
            else:
                velx_variables[i]=''
                vely_variables[i]=''                                                                                                                    # If the any variable is solve, a empty string is assgned as the value of the corresponding key
        for i in xy_axis:
            i['collision_type']=variables['collision_type']                                                                                     # Two new keys assigned to indicate that it is calculate a component 
            i['component_cal']=True
        for i in xy_axis:
            for p in variables:
                if 'mass' in p:
                    i[p]=variables[p]
        if find_missing_momentum1D(vely_variables,solve)!=None or find_missing_momentum1D(velx_variables,solve)!= None:# If mass variable becomes negative or conservation of energy is false as calculated previously
            vely_variables[solve]=find_missing_momentum1D(vely_variables,solve)[solve]
            velx_variables[solve]=find_missing_momentum1D(velx_variables,solve)[solve]                                                      # No real values is returned if one of the two conditions is met
            if 'mass' not in solve:
                variables[solve]=sqrt(vely_variables[solve]**2+velx_variables[solve]**2)
            if 'mass' in solve:
                variables[solve]=vely_variables[solve]                                                                                                          # None s will be returned to re-ask the user to input values
            return(xy_axis)
        else:
            xy_axis=(None,None,None)
            return xy_axis
        
        

                


    def ratio_conversion2d(lstx,lsty):#------------------------------------------------------------------------------------------------------# Ratio conversion of 2d version , takes two parameter instead of one
        v_max=max([abs(i) for i in lstx+lsty if i!=0])
        v_min=min([abs(i) for i in lstx+lsty if i!=0])
        if v_max>1.3:
            ratio=1.3/v_max
            for i in range(len(lstx)):
                lstx[i]= lstx[i]*ratio
                lsty[i]= lsty[i]*ratio                                                                                                                                      # Go through the same procedure as the 1d ratio conversion, see previous code to relate 
        elif v_min<0.1:
            ratio=0.1/v_min
            for i in range(len(lstx)):
                lstx[i]= lstx[i]*ratio
                lsty[i]= lsty[i]*ratio
        return (lstx,lsty)
                
        
    def redraw_2d(variable_x,variable_y,variables):                                                                                                     # The function that update screen and show animation 
        if None in (variable_x,variable_y,variables):
            pass
        else:
            xy=[variable_x,variable_y]
            pygame.init()
            screen=pygame.display.set_mode((WIDTH, HEIGHT))
            display=True                                                                                                                                                # The boolean value to set the while loop to keep the game going 
            post_col=False                                                                                                                                              # Boolean value that check if it's before or after the collision
            press=0
            m1,m2=variable_x['mass1'],variable_x['mass2']
            if len(variable_x)==8:
                v1x,v2x,v1fx,v2fx= variable_x['vel1'],variable_x['vel2'],variable_x['vel1f'],variable_x['vel2f']
            else:
                v1x,v2x,v1fx,v2fx= variable_x['vel1'],variable_x['vel2'],variable_x['velf'],variable_x['velf']                              # Variables will be different if the type of collision is different 
            if len(variable_y)==8:
                v1y,v2y,v1fy,v2fy= variable_y['vel1'],variable_y['vel2'],variable_y['vel1f'],variable_y['vel2f']
            else:
                v1y,v2y,v1fy,v2fy= variable_y['vel1'],variable_y['vel2'],variable_y['velf'],variable_y['velf']
            d1x,d1y,d2x,d2y=initial_pos(v1x,v1y,v2x,v2y,variables['angle1'],variables['angle2'])                                            # Use initial_pos function to determine the location to start so they can meet at the center
            print(d1x,d1y,d2x,d2y)
            x1=WIDTH/2+d1x
            y1=HEIGHT/2-d1y
            x2=WIDTH/2+d2x                                                                                                                                          # the distance is applied to the initial x, y values of the balls 
            y2=HEIGHT/2-d2y
            print('x1:',x1,'y1',y1,'x2',x2,'y2',y2)
            lstx=[v1x,v2x,v1fx,v2fx]
            lsty=[v1y,v2y,v1fy,v2fy]
            ratio_conversion2d(lstx,lsty)                                                                                                                       # Velocity ratio conversion function is applied so that the balls travels at the observable speed
            nlx,nly=ratio_conversion2d(lstx,lsty)
            v1x,v2x,v1fx,v2fx=nlx[0],nlx[1],nlx[2],nlx[3]
            v1y,v2y,v1fy,v2fy=nly[0],nly[1],nly[2],nly[3]
            
            
            while display:
                screen.fill(BLACK)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:       
                        pygame.quit()                                                                                                                               # If quit hit, quit the screen
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            press+=3                                                                                                                                    # If space pressed, the display time becomes slower
                        if event.key == pygame.K_r:
                            fade(WIDTH,HEIGHT)                                                                                                                  # If r pressed, use returns to the variables input screen
                            main()
                
                if distance(x1,y1,x2,y2)<20:
                    post_col=True
                if post_col==True:
                    velx1,vely1,velx2,vely2=v1fx,v1fy,v2fx,v2fy                                                                                         # Before or after collision is detected so new velocities can be assigned
              
                else:
                    velx1,vely1,velx2,vely2=v1x,v1y,v2x,v2y
        ##        print( velx1,vely1,velx2,vely2)
                x1+=velx1
                x2+=velx2
                y1-=vely1
                y2-=vely2
                indication(x1,y1,WHITE)
                indication(x2,y2,GREY)                                                                                                                          # Indicator are called here 
                if m1>m2:
                    pygame.draw.circle(screen,WHITE, (int(x1),int(y1)), int(12),0)
                    pygame.draw.circle(screen,GREY, (int(x2),int(y2)), int(8),0)
                if m1<m2:
                    pygame.draw.circle(screen,WHITE, (int(x1),int(y1)), int(8),0)
                    pygame.draw.circle(screen,GREY, (int(x2),int(y2)), int(12),0)
                pygame.draw.circle(screen,RED, center, 4,0)
                legend(screen,variables)
                pygame.display.update()                                                                                                                         # 
                pygame.time.delay(press)



    def indication(x,y,color):
        if x>WIDTH:
            ratio=abs(WIDTH/x)
            ind=right
            indicator=ind.get_rect(center=(WIDTH-18,int(y)))                                                                                        # Indicator function helps to indicate the position of the ball when they are outside of the screen
            pygame.draw.circle(screen,color, (WIDTH-48,int(y)), int(7*ratio),0)
            screen.blit(ind,indicator)
        if x<0:
            ratio=(WIDTH/(WIDTH+abs(x)))                                                                                                                # General concept: When the x or y of ball is bigger or smaller than the limit of the screen, a triangle indicator will be shown ,and a ball will be shown with a changing size that depends on the how far away the ball is from the screen
            ind=left
            indicator=ind.get_rect(center=(18,int(y)))
            pygame.draw.circle(screen,color, (48,int(y)), int(7*ratio),0)
            screen.blit(ind,indicator)
        if y>HEIGHT:
            ratio=abs(HEIGHT/y)
            ind=down
            indicator=ind.get_rect(center=(int(x),(HEIGHT-18)))
            pygame.draw.circle(screen,color, (int(x),HEIGHT-48), int(7*ratio),0)
            screen.blit(ind,indicator)
        if y<0:
            ratio=(HEIGHT/(HEIGHT+abs(Y)))
            ind=up
            indicator=ind.get_rect(center=(int(x),(18)))
            pygame.draw.circle(screen,color, (int(x),48), int(7*ratio),0)
            screen.blit(ind,indicator)
            
            
            
    def choose_component():#-----------------------------------------------------------------------------------------------------------# A function that sets the screen for the user to be abl eto choose which dimension of animation is to be shown 
        
        while True:
            event = pygame.event.poll()
            mousex, mousey = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            twoD_width=233                                                                                                                                      # Dimension of each button is defined here
            twoD_x=239
            oneD_width=233
            oneD_x=497                                                                                                                                                                                                  
            h=351
            y=137
            if oneD_x <= mousex <= oneD_x+oneD_width and y <= mousey <= y+h and event.type == pygame.MOUSEBUTTONDOWN:# If the mouse is clicked with a certain location, the type of visualization will be shown 
                return '1d'
            elif twoD_x <= mousex <= twoD_x+twoD_width and y <= mousey < y+h and event.type == pygame.MOUSEBUTTONDOWN:
                return '2d'
            
            screen.blit(choose_image,(0,0))
            if oneD_x <= mousex <= oneD_x+oneD_width and y <= mousey <= y+h :                                                           # In order to make the visual effect better, when mouse is positioned over a certain area, it will increase the visual attribute of the product
                screen.blit(oneD_click,(0,0))
            elif twoD_x <= mousex <= twoD_x+twoD_width and y <= mousey < y+h:
                screen.blit(twoD_click,(0,0))

            pygame.display.update()
    def choose_collision():
        myfont = pygame.font.SysFont('Arial', 36)
        ELASTIC_txt = myfont.render('ELASTIC', False, WHITE)
        
        INELASTIC_txt = myfont.render('INELASTIC', False, ORANGE)                                                                                           # Indication to be shown on each section of the screen
        
        CE_txt = myfont.render('COMPLETELY', False, BLACK)
        CE_txt2=myfont.render('INELASTIC', False, BLACK)
        while True:
            event = pygame.event.poll()
            mousex, mousey = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elastic_width=WIDTH/3
            elastic_x=0
            inelatic_width=WIDTH/3                                                                                                                                      # The three sections of the screen on which if clicked, will lead to different type of collision
            inelastic_x=WIDTH/3
            CE_width=WIDTH/3
            CE_x=2*WIDTH/3
            h=HEIGHT
            y=0
            if elastic_x <= mousex <=elastic_width and y <= mousey <= y+h and event.type == pygame.MOUSEBUTTONDOWN:
                return '1'
            elif inelastic_x <= mousex <= inelastic_x+inelatic_width and y <= mousey < y+h and event.type == pygame.MOUSEBUTTONDOWN:# If mouse is clicked  within a certain area, the type of collision will be chosen 
                return '2'
            elif CE_x <= mousex <= CE_x+CE_width and y <= mousey < y+h and event.type == pygame.MOUSEBUTTONDOWN:
                return '3'
            
            screen.fill(BLACK)
            if elastic_x <= mousex <=elastic_width and y <= mousey <= y+h:
                pygame.draw.rect(screen, ORANGE, (elastic_x,y,elastic_width,HEIGHT), 0)
                screen.blit(ELASTIC_txt,(WIDTH/6-75, h/2))
            elif inelastic_x <= mousex <= inelastic_x+inelatic_width and y <= mousey < y+h:
                pygame.draw.rect(screen, GREY, (inelastic_x,y,inelatic_width,HEIGHT), 0)                                                                        # Visual attributes of the button, when mouse is positioned on a certain are, color will be changed
                screen.blit(INELASTIC_txt,(3*WIDTH/6-75, h/2))
            elif CE_x <= mousex <= CE_x+CE_width and y <= mousey < y+h:
                pygame.draw.rect(screen, WHITE, (CE_x,y,CE_width,HEIGHT), 0)
                screen.blit(CE_txt,(5*WIDTH/6-75, h/2))
                screen.blit(CE_txt2,(5*WIDTH/6-75, h/2+50))

            pygame.display.update()
    def fade(width,height):                                                                                                     # Function that will make the screen to fade into a certain color
        fade=pygame.Surface((width,height))
        fade.fill(BLACK)
        for alpha in range(0,300):
            fade.set_alpha(alpha)
            screen.blit(fade,(0,0))
            pygame.display.update()
            pygame.time.delay(3)
            
    def Rfade(width,height):                                                                                                     # Function that will make the screen to inversely fade into a certain color

        fade=pygame.Surface((width,height))
        fade.fill(WHITE)
        for alpha in reversed(range(0,300)):
            fade.set_alpha(alpha)
            screen.blit(fade,(0,0))
            pygame.display.update()
            pygame.time.delay(3)
            
    def main(case='2d',collision='1'):                                                                                      # Main function that contained all the little functions 
        case=choose_component()
        collision_type=choose_collision()
        a,b=slider_set(case,collision_type)
        fade(WIDTH,HEIGHT)                                                                                                  ### Firstly, the choose cases functions are called to determine the dimension and the type of the collision
        if case=='1d':                                                                                                              ### Determine the type values b using sliders 
            a,b=ask_for_input(a,b)
            print(a)                                                                                                                ### The sliders value are inputted into functions to rearrange and calculate the missing data to finalize the visualization 
            print(find_missing_momentum1D(a,b))
            while None == find_missing_momentum1D(a,b):
                a,b=slider_set(case,collision_type)
                print(a)                                                                                                            ### If special cases are met, re ask the using input more valid values, and run through the process again
                a,b=ask_for_input(a,b)
                find_missing_momentum1D(a,b)
            
                

        if case=='2d':
            a,b,c=find_missing_momentum2D(a,b)
            print(a,b,c)
            while None in find_missing_momentum1D(a,b):                                                         # Same scenario applies for 2d collision 
                print('fuck meeee')
                a,b=slider_set(case,collision_type)
                a,b,c=find_missing_momentum1D(a,b)

        if case=='1d':
            
            print(redraw_1d(find_missing_momentum1D(a,b)))                                                  # Draw the 1d scenario
        if case=='2d':
            redraw_2d(a,b,c)                                                                                                # Draw the 2d scenario
    main()
    unit=''                                                                                                       # Main functions calling 
