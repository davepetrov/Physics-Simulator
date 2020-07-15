import pygame, sys
from time import sleep
from math import acos, asin, sin, cos, tan, pi, sqrt
from formulas import formula1
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
font2 = pygame.font.SysFont("Arial BOLD", 25)
screen = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
pop = 7
background = pygame.image.load("background_forces.jpg")
background = background.convert_alpha()
background = pygame.transform.scale(background,(X,Y))

car = pygame.image.load("car.png")
car = pygame.transform.scale(car,(60,20))
class Slider():
    def __init__(self, name, maxi, mini, pos, unit):
        self.val = (maxi+mini)/2  # start value
        self.maxi = maxi  # maximum at slider position right
        self.name=name
        self.mini = mini  # minimum at slider position left
        self.xpos = X/2-40  # x-location on screen
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
    if 10 <= mousex <= 10+50 and  75 <= mousey <= 75+25 and pygame.mouse.get_pressed():
        pygame.draw.rect(screen, GREEN, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
        pygame.draw.rect(screen, WHITE, (10, 75, 50, 25))
        return True
    pygame.draw.rect(screen, GREEN, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
    return False

def car_up(carY):
    sleep(.05)
    carY-=2
    screen.blit(car,(X/2,Y-100+carY))
    pygame.display.update()
    screen.blit(background,(0,0))
    return carY

def car_down(carY):
    sleep(.05)
    carY+=2
    screen.blit(car,(X/2,Y-100+carY))
    pygame.display.update()
    screen.blit(background,(0,0))
    return carY 

def call_sliders(slides):
    Missing_Amount=2
    carX=X/2
    carY=car_up(0)
    carY=car_down(carY)
    carY=car_up(carY)
    carY=car_down(carY)
    carY=car_up(carY)
    carY=car_down(carY)
    carY=car_up(carY)
    carY=car_down(carY)
    carY=car_up(carY)
    carY=car_down(carY)
    carY=car_up(carY)
    carY=car_down(carY)
    carY=car_up(carY)
    carY=car_down(carY)
    carY=car_up(carY)
    carY=car_down(carY)
    carY=car_up(carY)
    carY=car_down(carY)
    carY=car_up(carY)
    carY=car_down(carY)
    carY=car_up(carY)
    
    while True:
        DisplayList=[slides[0].display,slides[1].display,slides[2].display,slides[3].display,slides[4].display]
    
        counter=1
        slides[4].display=True
        slides[4].choose=True
        slides[4].boxCol=GREEN
        if slides[0].choose == True:
            a=slides[0].val
        elif slides[0].choose == False:
            a=formula1(slides[0].val, slides[4].val,slides[1].val,slides[2].val,slides[3].val,'a')

        if slides[1].choose == True:
            m=slides[1].val
        elif slides[1].choose == False:
            fake_fa=1
            m=formula1(slides[0].val, slides[4].val,slides[1].val,slides[2].val,fake_fa,'m')
            
        for i in DisplayList:
            if i == False or i=="Gucci":
                counter+=1
        if counter>Missing_Amount or counter<Missing_Amount:
            pygame.draw.rect(screen, RED, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
        if counter==Missing_Amount and m>0 and a>0 :
            pygame.draw.rect(screen, RED, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
            static_text = font2.render("You're gud ;* ", False, GREEN)
            screen.blit(static_text,(X/2-120+85, Y/2+140+30-5))
            
            if start_button_display():
                return_list=[]
                for i in range(len(slides)):
                    if slides[i].choose==False:
                        return_list.append(None)
                    else:
                        return_list.append(slides[i].val)
                return return_list
        elif counter>Missing_Amount:
            pygame.draw.rect(screen, RED, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
            static_text = font2.render('NOT ENOUGH VARIABLES ', False, WHITE)
            screen.blit(static_text,(X/2-120+70-30, Y/2+140+30-5))
            
        elif counter<Missing_Amount:
            pygame.draw.rect(screen, RED, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
            static_text = font2.render('TOO MANY VARIABLES ', False, WHITE)
            screen.blit(static_text,(X/2-120+70-30, Y/2+140+30-5))
            
        elif a<=0:
            pygame.draw.rect(screen, RED, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
            static_text = font2.render('Impossible Acceleration value ', False, WHITE)
            static_text2 = font.render('Adjust Mass, Coef, Applied Force or Angle!', False, RED_2)
            screen.blit(static_text,(X/2-120+70-30, Y/2+140+30-5))
            screen.blit(static_text2,(X/2-120, Y/2+150+30))
        elif m<=0:
            pygame.draw.rect(screen, RED, [10-pop/2, 75-pop/2, 50+pop, 25+pop])
            static_text = font2.render('Impossible Mass value. ', False, WHITE)
            static_text2 = font.render('Adjust Acceleration, Coef, Applied Force or Angle!', False, RED_2)
            screen.blit(static_text,(X/2-120+70-30, Y/2+140+30-5))
            screen.blit(static_text2,(X/2-120, Y/2+150+30))
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
        carX+=a/30
        if carX-120>X: carX=0-120
        screen.blit(car,(carX,Y-100))
        for s in slides:
            s.draw()

