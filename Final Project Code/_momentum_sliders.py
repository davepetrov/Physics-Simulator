import pygame, sys
from time import sleep
from math import acos, asin, sin, cos, tan, pi, sqrt
pygame.init()

X = 900
Y = 650
WIDTH, HEIGHT = 900, 650
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
ORANGE = (200, 100, 50)
RED = (255,0,0)
RED_2 = (237,41,57)
GREEN = (0,255,0)
TRANS = (1, 1, 1)

font = pygame.font.SysFont("Arial", 14)
font1 = pygame.font.SysFont("Arial", 18)
font2 = pygame.font.SysFont("Arial", 16)
screen = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
pop = 7
background = pygame.image.load("_momentum_2d_image.jpg")
background = background.convert_alpha()
background = pygame.transform.scale(background,(X,Y))

class Slider():
    def __init__(self, name, maxi, mini, pos, unit):
        self.val = (maxi+mini)/2  # start value
        self.maxi = maxi  # maximum at slider position right
        self.name=name
        self.mini = mini  # minimum at slider position left
        self.xpos = X-240  # x-location on screen
        self.x_max = self.xpos+80
        self.ypos = pos
        self.surf = pygame.surface.Surface((165, 50))
        self.surf2 = pygame.surface.Surface((50, 50))
        self.hit = False  # the hit attribute indicates slider movement due to mouse interaction
        self.display="Gucci"
        self.boxCol=GREY
        self.unit = unit
        self.choose=False

        self.txt_surf = font.render(self.name, 1, BLACK)
        self.txt_rect = self.txt_surf.get_rect(center=(50, 15))

        # Static graphics - slider background #
        pygame.draw.rect(self.surf, GREY, [0, 0, 165, 50], 3)
        pygame.draw.rect(self.surf, ORANGE, [10, 10, 80, 10], 0)
        pygame.draw.rect(self.surf, WHITE, [10, 30, 80, 5], 0)

        pygame.draw.rect(self.surf2, self.boxCol, [0, 0, 50, 50], 3)
        
        self.surf.blit(self.txt_surf, self.txt_rect)  # this surface never changes

        # dynamic graphics - button surface #
        self.button_surf = pygame.surface.Surface((20, 20))
        self.button_surf.fill(TRANS)
        self.button_surf.set_colorkey(TRANS)
        pygame.draw.circle(self.button_surf, BLACK, (10, 10), 6, 0)
        pygame.draw.circle(self.button_surf, ORANGE, (10, 10), 4, 0)

    def draw(self):
        # static
        #event=pygame.event.poll()
        surf = self.surf.copy()
        surf2= self.surf2.copy()
        # dynamic
        pos = (10+int((self.val-self.mini)/(self.maxi-self.mini)*80), 33)
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        self.button_rect.move_ip(self.xpos, self.ypos)  # move of button box to correct screen position

        # screen
        mouseX,mouseY=pygame.mouse.get_pos()
        if mouseX>self.xpos-50 and mouseX<self.xpos and mouseY>self.ypos and mouseY<self.ypos+50:
            event=pygame.event.poll()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.display==True:
                        self.display=False
                        self.choose=False
                        self.boxCol=RED
                    elif self.display==False or self.display=="Gucci":
                        self.display=True
                        self.choose=True
                        self.boxCol=GREEN
                pygame.time.delay(100)
        pygame.draw.rect(self.surf2, self.boxCol, [0, 0, 50, 50], 3)
        if self.display==True or self.display=="Gucci":              
            screen.blit(surf, (self.xpos, self.ypos))
            value = font.render("= "+str(round(self.val,2))+self.unit,False,WHITE)
            screen.blit(value,(self.xpos+100,self.ypos+15))
    
        screen.blit(surf2,(self.xpos-50,self.ypos))
        
    def move(self):

        self.val = (pygame.mouse.get_pos()[0] - self.xpos - 10) / 80 * (self.maxi - self.mini) + self.mini

        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi
            
def start_button_display():
    mousex, mousey = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if 10 <= mousex <= 10+50 and  75 <= mousey <= 75+25 and event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, GREEN, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
            pygame.draw.rect(screen, WHITE, (10, 75, 50, 25))
            return True
    pygame.draw.rect(screen, GREEN, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
    return False

def Notes(screen):
        
        Note = font1.render('-=NOTES=-',1,WHITE)
        
        Note_Message = font2.render('Velocity shown is not realistic speed ',1,WHITE)
        Note_Message2 = font2.render('Scaling is blown out of proportion to increase viewability',1,WHITE)
        
        Speed_Message1 = font2.render('Left click will diminish speed of the program by 10%',1,WHITE)
        
        Legend_Message = font2.render('Legend is displayed on top left corner',1,WHITE)
        Restart_Message = font2.render('Pressing "r" will restart the program',1,WHITE)
        Mandatory_Message = font2.render('ALL MASSES AND ANGLES ARE MANDATORY',1,WHITE)


        screen.blit(Note,Note.get_rect(center=(WIDTH/2-300, 150)))
        
        #screen.blit(Notes_Pic,(WIDTH/2-300,175))
        screen.blit(Note_Message,Note_Message.get_rect(center=(WIDTH/2-240, 180)))
        screen.blit(Note_Message2,Note_Message2.get_rect(center=(WIDTH/2-190, 210)))

        #screen.blit(Click,(WIDTH/2-200,250))
        screen.blit(Speed_Message1,Speed_Message1.get_rect(center=(WIDTH/2-200, 290)))
        screen.blit(Legend_Message,Legend_Message.get_rect(center=(WIDTH/2-240, 260)))
        screen.blit(Mandatory_Message,Mandatory_Message.get_rect(center=(WIDTH/2-220, 370)))
        #screen.blit(Scroll,(WIDTH/2-180,330))
        screen.blit(Restart_Message,Restart_Message.get_rect(center=(WIDTH/2-250, 340)))
  

        

def call_sliders(slides, component,coll_type):
    allow=False
    while True:
        Notes(screen)
        Missing_Amount=1
        DisplayList=[]
        if component == '2d' and coll_type!='3':
            DisplayList=[slides[0].display,slides[1].display,slides[2].display,slides[3].display,slides[4].display,slides[5].display,slides[6].display,slides[7].display,slides[8].display,slides[9].display] #10
        elif component == '2d' and coll_type=='3':
            DisplayList=[slides[0].display,slides[1].display,slides[2].display,slides[3].display,slides[4].display,slides[5].display,slides[6].display,slides[7].display] #8
        if component == '1d' and coll_type!='3' :
            DisplayList=[slides[0].display,slides[1].display,slides[2].display,slides[3].display,slides[4].display,slides[5].display] #6
        elif component == '1d' and coll_type=='3':
           DisplayList=[slides[0].display,slides[1].display,slides[2].display,slides[3].display,slides[4].display] #5 
        allow=True
        counter=0
        for s in slides:
            if 'angle' in s.name or 'mass' in s.name:
                s.display=True
                s.boxCol=GREEN
                s.choose=True
        for i in DisplayList:
            if i == False or i=="Gucci":
                counter+=1
        if counter>Missing_Amount or counter<=Missing_Amount:
            pygame.draw.rect(screen, RED, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
            allow=1
        
        
        if counter==Missing_Amount:
            if slides[1].val!=slides[4].val:    
                if start_button_display():
                    return_list=[]
                    for i in range(len(slides)):
                        if slides[i].choose==False:
                            return_list.append('')
                        else:
                            return_list.append(str(slides[i].val))
                    return return_list
            if slides[1].val==slides[4].val :
                message = font.render(" INITIAL ANGLES CAN NOT HAVE THE SAME VALUES",False,WHITE)
                screen.blit(message,(200,500))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for s in slides:
                    if s.button_rect.collidepoint(pos):
                        s.hit = True
                
            elif event.type == pygame.MOUSEBUTTONUP:
                for s in slides:
                    s.hit = False

        for s in slides:
            if s.hit:
                s.move()

        pygame.display.update()
        screen.blit(background,(0,0))
        for s in slides:
            s.draw()

def slider_set(case,collision_type):
    if case=='1d':
        v1 = Slider("velocity 1", 50, -50, 15, "m/s")
        m1 = Slider("mass 1", 80,1, 15+60, "kg")
        v2 = Slider("velocity 2", 50, -50, 15+60+60, "m/s")
        m2 = Slider("mass 2", 80,1, 15+60+60+60, "kg")
        if collision_type=='1' or collision_type=='2' :
            v1f = Slider("Final velocity 1", 50, -50, 15+60+60+60+60, "m/s")
            v2f = Slider("Final velocity 2", 50,-50, 15+60+60+60+60+60, "m/s")
            slides=[v1,m1,v2,m2,v1f,v2f]
            obtained=call_sliders(slides,case,collision_type)

        else:
            vf = Slider("Final velocity", 50,1, 15+60+60+60+60, "m/s")
            slides=[v1,m1,v2,m2,vf]
            obtained=call_sliders(slides,case,collision_type)
    if case=='2d':
        v1 = Slider("velocity 1", 50, 0, 15, "m/s")
        ang1 = Slider("angle 1", 360,0, 15+60+60, "°")
        m1 = Slider("mass 1", 80,1, 15+60, "kg")
        v2 = Slider("velocity 2", 50, 0, 15+60+60+60, "m/s")
        ang2 = Slider("angle 2", 360,0, 15+60+60+60+60, "°")
        m2 = Slider("mass 2", 89,1, 15+60+60+60+60+60, "kg")
        if collision_type=='1' or collision_type=='2' :
            v1f = Slider("Final velocity 1", 50, 0, 15+60+60+60+60+60+60, "m/s")
            ang1f = Slider("angle 1 prime", 360,0, 15+60+60+60+60+60+60+60, "°")
            v2f = Slider("Final velocity 2", 50,0, 15+60+60+60+60+60+60+60+60, "m/s")
            ang2f = Slider("angle 2 prime", 360,0, 15+60+60+60+60+60+60+60+60+60, "°")
            slides=[v1,ang1,m1,v2,ang2,m2,v1f,ang1f,v2f,ang2f]
            obtained =call_sliders(slides,case,collision_type)

        else:
            vf = Slider("Final velocity", 50,1, 15+60+60+60+60+60+60, "m/s")
            angf = Slider("angle prime", 360,0, 15+60+60+60+60+60+60+60, "°")
            slides=[v1,ang1,m1,v2,ang2,m2,vf,angf]
            obtained=call_sliders(slides,case,collision_type)
    return obtained,collision_type
