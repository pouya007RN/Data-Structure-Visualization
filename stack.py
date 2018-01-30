import pygame
import time
pygame.init()
flat = pygame.display.set_mode((800,600))

f = pygame.image.load('f.jpg')
p = pygame.image.load('p.png')

w=0
h=0
white=(255,255,255)




def txt ( txt , x , y , sec =0 , font =10 ,color =(255,255,255)):
    myfont = pygame.font.SysFont("Comic Sans MS", font)

    label = myfont.render('%s'%txt,True,(0,0,0))

    flat.blit(label, ( x , y))

    pygame.display.update()

    time.sleep(sec)


class brick:
    def __init__(self , num ,img=None):
        n = num + 1
        self.x = 0
        self.y = 510 - num *90
        self.img = pygame.image.load('%s.png'%n)
        
        
needle3 = brick(3)
needle3.x =350
needle2 = brick(2)
needle2.x =350
a = brick(0)
b = brick(1)
c = brick(2)
d = brick(3)

#def make_obj(flat , x , y , img):
    #flat.blit(img ,(x , y))
 


flat.fill(white)
pygame.draw.circle(flat,(0,0,0),(390,250),170,170)

myfont = pygame.font.SysFont("Comic Sans MS", 50)

label = myfont.render('Stack',True,(250,250,250))

flat.blit(label, (320, 225))
pygame.display.update()
time.sleep(6)
flat.fill(white)

txt('In computer science, a stack is an abstract data type ',20,30,sec=4,font=15)
txt('that serves as a collection of elements, with two principal operations :' ,20,70,sec=4 ,font=15)

flat.fill(white)
txt('PUSH',200,200,sec=1,font=40)
txt('which stacks obj over each other',20,250,sec=4,font=20)




for i in range (500):
        flat.fill(white)
        flat.blit(a.img ,(a.x , a.y))
        flat.blit(f ,(525 , a.y - 80))
        a.x+=1
        txt('PUSHING OBJ',200,200,font=40)
        pygame.display.update()



for i in range (500):
        flat.fill(white)
        flat.blit(a.img ,(a.x , a.y))
        flat.blit(b.img ,(b.x , b.y))
        flat.blit(f ,(525 , b.y - 80))
        b.x+=1
        txt('PUSHING OBJ',200,200,font=40)
        pygame.display.update()



for i in range (500):
        flat.fill(white)
        flat.blit(a.img ,(a.x , a.y))
        flat.blit(b.img ,(b.x , b.y))
        flat.blit(c.img ,(c.x , c.y))
        flat.blit(f ,(525 , c.y - 80))
        c.x+=1
        txt('PUSHING OBJ',200,200,font=40)
        pygame.display.update()


for i in range (500):
        flat.fill(white)
        flat.blit(a.img ,(a.x , a.y))
        flat.blit(b.img ,(b.x , b.y))
        flat.blit(c.img ,(c.x , c.y))
        flat.blit(d.img ,(d.x , d.y))
        flat.blit(f ,(525 , d.y - 80))
        d.x+=1
        txt('PUSHING OBJ',200,200,font=40)
        pygame.display.update()




flat.fill(white)
flat.blit(a.img ,(a.x , a.y))
flat.blit(b.img ,(b.x , b.y))
flat.blit(c.img ,(c.x , c.y))
flat.blit(d.img ,(d.x , d.y))

txt('and POP',200,200,sec=1,font=40)
txt('which removes the most recently added obj',20,250,sec=4,font=20)



for j in range (180):
        flat.fill(white)
        flat.blit(a.img ,(a.x , a.y))
        flat.blit(b.img ,(b.x , b.y))
        flat.blit(c.img ,(c.x , c.y))
        flat.blit(d.img ,(d.x , d.y))
        flat.blit(p ,(needle3.x - 70 , d.y ))
        needle3.x+=1
        txt('POPING OBJ',200,200,font=40)
        pygame.display.update()

    



#for i in range (100):
flat.fill(white)
flat.blit(a.img ,(a.x , a.y))
flat.blit(b.img ,(b.x , b.y))
flat.blit(c.img ,(c.x , c.y))
flat.blit(p ,(d.x - 70 , d.y ))
txt('POPING OBJ',200,200,font=40)
pygame.display.update()
time.sleep(3)





for i in range (180):
        flat.fill(white)
        flat.blit(a.img ,(a.x , a.y))
        flat.blit(b.img ,(b.x , b.y))
        flat.blit(c.img ,(c.x , c.y))
        flat.blit(p ,(needle2.x - 70 , c.y ))
        needle2.x+=1
        txt('POPING OBJ',200,200,font=40)
        pygame.display.update()


flat.fill(white)
flat.blit(a.img ,(a.x , a.y))
flat.blit(b.img ,(b.x , b.y))
flat.blit(p ,(needle2.x - 70 , c.y ))
txt('POPING OBJ',200,200,font=40)
pygame.display.update()

time.sleep(4)
pygame.quit()



















