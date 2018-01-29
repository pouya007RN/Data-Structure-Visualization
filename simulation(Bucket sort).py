import pygame,time

Algorithm = input()
if Algorithm == 'bucket sort':
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800,600))
    screen.fill((255,255,255))
    

    L1=200
    W1=150

    class bubble_1:
        def __init__(self,radius):
            self.radius = 30
            pygame.draw.circle(screen,(125,125,125),(int(L1),int(W1)),self.radius,5)
            
            myfont = pygame.font.SysFont("Comic Sans MS", 20)
            label = myfont.render('12',True,(0,0,0)) 
            screen.blit(label, (L1-10,W1-15))


    L2=300
    W2=150

    class bubble_2:
        def __init__(self,radius):
            self.radius = 30            
            pygame.draw.circle(screen,(255,150,255),(int(L2),int(W2)),self.radius,5)
            
            myfont = pygame.font.SysFont("Comic Sans MS", 20)
            label = myfont.render('30',True,(0,0,0)) 
            screen.blit(label, (L2-10,W2-15))
    L3=400
    W3=150

    class bubble_3:
        def __init__(self,radius):
            self.radius = 30
            pygame.draw.circle(screen,(150,255,255),(int(L3),int(W3)),self.radius,5)
            
            myfont = pygame.font.SysFont("Comic Sans MS", 20)
            label = myfont.render('8',True,(0,0,0)) 
            screen.blit(label, (L3-6,W3-15))

    L4=500
    W4=150

    class bubble_4:
        def __init__(self,radius):
            self.radius = 30
            pygame.draw.circle(screen,(150,150,255),(int(L4),int(W4)),self.radius,5)
            
            myfont = pygame.font.SysFont("Comic Sans MS", 20)
            label = myfont.render('4',True,(0,0,0)) 
            screen.blit(label, (L4-6,W4-15))

    L5=600
    W5=150

    class bubble_5:
        def __init__(self,radius):
            self.radius = 30
            pygame.draw.circle(screen,(255,150,150),(int(L5),int(W5)),self.radius,5)

            myfont = pygame.font.SysFont("Comic Sans MS", 20)
            label = myfont.render('45',True,(0,0,0)) 
            screen.blit(label, (L5-10,W5-15))

    class Bucket:
        def __init__(self,L,W):
            self.L = L
            self.W = W
            pygame.draw.rect(screen,(0,0,0),(L,W,100,120),8)

    pygame.draw.circle(screen,(80,80,255),(390,250),175,5)
    pygame.draw.circle(screen,(255,150,150),(390,250),170,170)
    myfont = pygame.font.SysFont("Comic Sans MS", 50)
    label = myfont.render('Bucket Sort',True,(80,80,250)) 
    screen.blit(label, (250,200))
    pygame.display.update()

    time.sleep(5)

    screen.fill((255,255,255))


    bubble_1(30)
    
    bubble_2(30)
    
    bubble_3(30)
    
    bubble_4(30)
    
    bubble_5(30)
    
    myfont = pygame.font.SysFont("Comic Sans MS", 20)
    label = myfont.render('there are 5 bubbles on the screen with different numbers on them !!!',True,(0,0,0)) 
    screen.blit(label, (90,300))    
   
    pygame.display.update()

   
    time.sleep(4)

    screen.fill((255,255,255))
    
    bubble_1(30)    
    bubble_2(30)    
    bubble_3(30)    
    bubble_4(30)    
    bubble_5(30)

    
    myfont = pygame.font.SysFont("Comic Sans MS", 20)

    label = myfont.render('look at the 6 rectangles drawn below',True,(0,0,0)) 
    screen.blit(label, (230,50))

    Bucket(100,300)
    Bucket(200,300)
    Bucket(300,300)
    Bucket(400,300)
    Bucket(500,300)
    Bucket(600,300)
    
    pygame.display.update()
    time.sleep(4)
    
    label = myfont.render('each block has a range !!',True,(0,0,0)) 
    screen.blit(label, (300,500))
    pygame.display.update()
    
    time.sleep(3)

    
    myfont = pygame.font.SysFont("Comic Sans MS", 15)

    label = myfont.render('[0 , 10)',True,(0,0,0)) 
    screen.blit(label, (124,430))
    pygame.display.update()

    time.sleep(1)

    label = myfont.render('[10 , 20)',True,(0,0,0)) 
    screen.blit(label, (224,430))    
    pygame.display.update()

    time.sleep(1)

    label = myfont.render('[20 , 30)',True,(0,0,0)) 
    screen.blit(label, (324,430))
    pygame.display.update()

    time.sleep(1)
    
    label = myfont.render('[30 , 40)',True,(0,0,0)) 
    screen.blit(label, (424,430))
    pygame.display.update()

    time.sleep(1)

    label = myfont.render('[40 , 50)',True,(0,0,0)) 
    screen.blit(label, (528,430))
    pygame.display.update()

    time.sleep(1)
    
    label = myfont.render('[50 , 60)',True,(0,0,0)) 
    screen.blit(label, (628,430))
    pygame.display.update()

    time.sleep(3)

    
    pygame.draw.rect(screen,(255,255,255),(300,500,400,50),100)
    pygame.draw.rect(screen,(255,255,255),(100,50,500,10),100)

    time.sleep(1)
    
    myfont = pygame.font.SysFont("Comic Sans MS", 20)
    label = myfont.render('now the bubbles will be put in their own blocks',True,(0,0,0)) 
    screen.blit(label, (200,40))
    
    label = myfont.render('according to their amounts',True,(0,0,0))
 
    screen.blit(label, (270,70))
    
    pygame.display.update()

    time.sleep(4)
    pygame.draw.rect(screen,(255,255,255),(200,40,500,30),100)
    pygame.display.update()

    for i in range (130):
        screen.fill((255,255,255))
        bubble_1(30)    
        bubble_2(30)    
        bubble_3(30)    
        bubble_4(30)    
        bubble_5(30)
        
        Bucket(100,300)
        Bucket(200,300)
        Bucket(300,300)
        Bucket(400,300)
        Bucket(500,300)
        Bucket(600,300)
        
        myfont = pygame.font.SysFont("Comic Sans MS", 15)

        label = myfont.render('[0 , 10)',True,(0,0,0)) 
        screen.blit(label, (124,430))
   
        label = myfont.render('[10 , 20)',True,(0,0,0)) 
        screen.blit(label, (224,430))    
    
        label = myfont.render('[20 , 30)',True,(0,0,0)) 
        screen.blit(label, (324,430))
       
        label = myfont.render('[30 , 40)',True,(0,0,0)) 
        screen.blit(label, (424,430))
    
        label = myfont.render('[40 , 50)',True,(0,0,0)) 
        screen.blit(label, (528,430))    
    
        label = myfont.render('[50 , 60)',True,(0,0,0)) 
        screen.blit(label, (628,430))
        
        L1 += 0.45
        W1 += 1.55

        L2 += 1.2
        W2 += 1.55

        L3 -= 1.8
        W3 += 1.45

        L4 -= 2.8
        W4 += 1.8

        L5 -=0.3
        W5 +=1.55

        time.sleep(0.01)
        pygame.display.update()

    time.sleep(1)

    myfont = pygame.font.SysFont("Comic Sans MS", 30)

    label = myfont.render('each block will sort its bubbles :)',True,(0,0,0)) 
    screen.blit(label, (150,230))
    pygame.display.update()

    time.sleep(5)

    screen.fill((255,255,255))
        
    Bucket(100,300)
    Bucket(200,300)
    Bucket(300,300)
    Bucket(400,300)
    Bucket(500,300)
    Bucket(600,300)
        
    myfont = pygame.font.SysFont("Comic Sans MS", 15)

    label = myfont.render('[0 , 10)',True,(0,0,0)) 
    screen.blit(label, (124,430))
   
    label = myfont.render('[10 , 20)',True,(0,0,0)) 
    screen.blit(label, (224,430))    
    
    label = myfont.render('[20 , 30)',True,(0,0,0)) 
    screen.blit(label, (324,430))
       
    label = myfont.render('[30 , 40)',True,(0,0,0)) 
    screen.blit(label, (424,430))
    
    label = myfont.render('[40 , 50)',True,(0,0,0)) 
    screen.blit(label, (528,430))    
    
    label = myfont.render('[50 , 60)',True,(0,0,0)) 
    screen.blit(label, (628,430))
    

    myfont = pygame.font.SysFont("Comic Sans MS", 20)

    label = myfont.render('4 , 8',True,(0,0,0)) 
    screen.blit(label, (124,260))

    label = myfont.render('12',True,(0,0,0)) 
    screen.blit(label, (234,260))

    label = myfont.render('30',True,(0,0,0)) 
    screen.blit(label, (434,260))
    
    label = myfont.render('45',True,(0,0,0)) 
    screen.blit(label, (534,260))
    pygame.display.update()

    time.sleep(3)

    
    label = myfont.render('now the numbers will be linked ! ',True,(255,100,100)) 
    screen.blit(label, (250,200))
    pygame.display.update()
    
    time.sleep(4)

    
    myfont = pygame.font.SysFont("Comic Sans MS", 25)

    label = myfont.render('4 ',True,(255,100,100)) 
    screen.blit(label, (190,100))
    pygame.display.update()
    
    
    time.sleep(0.8)

    label = myfont.render('8 ',True,(255,100,255)) 
    screen.blit(label, (290,100))
    pygame.display.update()
    
    time.sleep(0.8)

    label = myfont.render('12',True,(100,255,100)) 
    screen.blit(label, (390,100))
    pygame.display.update()
    
    time.sleep(0.8)

    label = myfont.render('30',True,(50,255,255)) 
    screen.blit(label, (490,100))
    pygame.display.update()

    time.sleep(0.8)
    
    label = myfont.render('45',True,(100,150,200)) 
    screen.blit(label, (590,100))
    pygame.display.update()

    time.sleep(4)

    screen.fill((255,255,255))
        
    C2=560
    C3=760

    for i in range(100):
        
        pygame.draw.circle(screen,(0,0,0),(40,C2),5,5)
        pygame.draw.circle(screen,(0,0,0),(C3,40),5,5)

        C2 -= 8
        C3 -= 8

        time.sleep(0.05)

        pygame.display.update()

    time.sleep(1)

 
    R=255
    G=255
    B=255

    for i in range(255):
        
    
        myfont = pygame.font.SysFont("Comic Sans MS", 40)

        label = myfont.render('** Bucket Sort **',True,(R,G,B)) 
        screen.blit(label, (220,100))

        R -= 1
        G -= 1
        B -= 1

        time.sleep(0.03)
        
        pygame.display.update()

    time.sleep(1)

    R=255
    G=255
    B=255

    for i in range(120):
        

        myfont = pygame.font.SysFont("Comic Sans MS", 30)

        label = myfont.render('Hossein Rezanejad & Ali Sobhani',True,(R,G,B)) 
        screen.blit(label, (180,220))

        R -= 1
        G -= 1
        

        time.sleep(0.03)

        pygame.display.update()

    time.sleep(1)

    R=255
    G=255
    B=255

    for i in range(120):
        
        myfont = pygame.font.SysFont("Comic Sans MS", 40)

        label = myfont.render('Final Project :D',True,(R,G,B)) 
        screen.blit(label, (250,340))

        G -= 1
        B -= 1

        time.sleep(0.03)
        pygame.display.update()
    
    time.sleep(5)
