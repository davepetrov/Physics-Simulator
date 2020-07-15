import pygame, math, sys
from time import sleep
pygame.init()

X = 900
Y = 650

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
ORANGE = (200, 100, 50)
RED = (255,0,0)
RED_2 = (237,41,57)
GREEN = (0,255,0)
TRANS = (1, 1, 1)

font = pygame.font.SysFont("Arial", 12)
font2 = pygame.font.SysFont("Arial BOLD", 24)
screen = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
pop = 7

background2 = pygame.image.load('background2_forces.jpg')
background3 = pygame.image.load('background3_forces.jpg')

horiz_plane = pygame.image.load("horiz_plane.png")
horiz_plane = pygame.transform.scale(horiz_plane,(60,60))


class Slider():
    def __init__(self, name, maxi, mini, pos, unit):
        self.val = (maxi+mini)/2  # start value
        self.maxi = maxi  # maximum at slider position right
        self.mini = mini  # minimum at slider position left
        self.xpos = X/2-40  # x-location on screen
        self.x_max = self.xpos+80
        self.ypos = pos
        self.surf = pygame.surface.Surface((165, 50))
        self.hit = False  # the hit attribute indicates slider movement due to mouse interaction
        self.unit = unit

        self.txt_surf = font.render(name, 1, BLACK)
        self.txt_rect = self.txt_surf.get_rect(center=(50, 15))

        # Static graphics - slider background #
        pygame.draw.rect(self.surf, GREY, [0, 0, 165, 50], 3)
        pygame.draw.rect(self.surf, ORANGE, [10, 10, 80, 10], 0)
        pygame.draw.rect(self.surf, WHITE, [10, 30, 80, 5], 0)
        
        self.surf.blit(self.txt_surf, self.txt_rect)  # this surface never changes

        # dynamic graphics - button surface #
        self.button_surf = pygame.surface.Surface((20, 20))
        self.button_surf.fill(TRANS)
        self.button_surf.set_colorkey(TRANS)
        pygame.draw.circle(self.button_surf, BLACK, (10, 10), 6, 0)
        pygame.draw.circle(self.button_surf, ORANGE, (10, 10), 4, 0)

    def draw(self):
        # static
        surf = self.surf.copy()
        # dynamic
        pos = (10+int((self.val-self.mini)/(self.maxi-self.mini)*80), 33)
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        self.button_rect.move_ip(self.xpos, self.ypos)
        # screen
        mouseX,mouseY=pygame.mouse.get_pos()            
        screen.blit(surf, (self.xpos, self.ypos))
        value = font.render("= "+str(round(self.val,2))+self.unit,False,WHITE)
        screen.blit(value,(self.xpos+100,self.ypos+15))
        
    def move(self):
        self.val = (pygame.mouse.get_pos()[0] - self.xpos - 10) / 80 * (self.maxi - self.mini) + self.mini
        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi
            
def start_button_display():
    mousex, mousey = pygame.mouse.get_pos()
    if 10 <= mousex <= 10+50 and  75 <= mousey <= 75+25 and pygame.mouse.get_pressed():
        pygame.draw.rect(screen, GREEN, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
        pygame.draw.rect(screen, WHITE, (10, 75, 50, 25))
        return True
    pygame.draw.rect(screen, GREEN, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
    return False

def plane_startup(planeY,count,component):
    if count == 0: #BASE CASE
        return planeY
    
    if count % 2 ==1:
        planeY-=5
    else:
        planeY+=5
    count-=1
    screen.blit(horiz_plane,(X/2,Y-100+planeY))
    pygame.display.update()
    if component == 'Vertical':
        screen.blit(background2,(0,0))
    elif component == 'Horizontal':
        screen.blit(background3,(0,0))
    sleep(.05)
    return plane_startup(planeY,count,component)

def call_sliders(slides,component):
    DisplayList=[]
    planeX=X/2
    planeY=plane_startup(0,20, component)
    while True:
        if component == 'Vertical':
            force_gravity = slides[0].val*9.8
            a=(force_gravity - slides[1].val)/slides[0].val
            if start_button_display() and a>0:
                return_list=[]
                for i in range(len(slides)):
                    return_list.append(slides[i].val)
                return return_list
            elif a<=0:
                pygame.draw.rect(screen, RED, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
                static_text = font2.render('Impossible Acceleration value ', False, WHITE)
                static_text2 = font.render('Adjust Air Resistance or Mass!', False, RED_2)
                screen.blit(static_text,(X/2-120+70-30, Y/2+140+30-5))
                screen.blit(static_text2,(X/2-120+50, Y/2+150+30))
                
        elif component == 'Horizontal':
            force_friction = slides[0].val*9.8*slides[2].val
            a=(slides[1].val - force_friction)/slides[0].val
            if start_button_display() and a>0:
                return_list=[]
                for i in range(len(slides)):
                    return_list.append(slides[i].val) 
                return return_list
            elif a<=0:
                pygame.draw.rect(screen, RED, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
                static_text = font2.render('Impossible Acceleration value ', False, WHITE)
                static_text2 = font.render('Adjust Mass, Coef or Applied Force!', False, RED_2)
                screen.blit(static_text,(X/2-120+70-30, Y/2+140+30-5))
                screen.blit(static_text2,(X/2-120+50, Y/2+150+30))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for s in slides:
                    if s.button_rect.collidepoint(pos):
                        s.hit =  True
            elif event.type == pygame.MOUSEBUTTONUP:
                for s in slides:
                    s.hit = False
         

        for s in slides:
            if s.hit:
                s.move()

        pygame.display.update()
        
        if component == 'Vertical':
            screen.blit(background2,(0,0))
        elif component == 'Horizontal':
            screen.blit(background3,(0,0))
        planeX+=1
        if planeX-120>X: planeX=0-120
        screen.blit(horiz_plane,(planeX,Y-100))
        for s in slides:
            s.draw()

