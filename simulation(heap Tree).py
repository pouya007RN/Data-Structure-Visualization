import pygame,time

Algorithm = input()
if Algorithm == 'heap tree':
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800,600))
    screen.fill((255,255,255))

    pygame.draw.circle(screen,(200,100,0),(390,250),175,5)
    pygame.draw.circle(screen,(100,200,0),(390,250),170,170)
    myfont = pygame.font.SysFont("Comic Sans MS", 50)
    label = myfont.render('heap tree',True,(150,100,0)) 
    screen.blit(label, (270,210))

    Tree = pygame.image.load('Tree 2.png')
    screen.blit(Tree,(550,350))
    screen.blit(Tree,(20,350))
    pygame.display.update()
   
    time.sleep(5)

    screen.fill((255,255,255))

    
    Tree = pygame.image.load('Tree.png')
    screen.blit(Tree,(300,50))
    pygame.display.update()

    time.sleep(1)

    
    myfont = pygame.font.SysFont("Comic Sans MS", 25)

    label = myfont.render('here you see a tree',True,(0,0,0))
    screen.blit(label, (30, 400))
    label = myfont.render('and the Algorithm will be shown on it !',True,(0,0,0),10)
    screen.blit(label, (30, 450))
    pygame.display.update()

    time.sleep(3)
    screen.fill((255,255,255))
    
    Tree = pygame.image.load('Tree.png')
    screen.blit(Tree,(300,50))
    pygame.display.update()

    time.sleep(1)

    myfont = pygame.font.SysFont("Comic Sans MS", 20)

    label = myfont.render('for example, number 10 ==>',True,(0,0,0))
    screen.blit(label, (30, 20))
    pygame.display.update()

    L1=320
    W1=35

    class circle_1:
        def __init__(self,R):
            self.R = R
            pygame.draw.circle(screen,(0,0,0),(int(L1),int(W1)),R,5)

    l1 = 310
    w1 = 20
            
    class num_1:
        def __init__(self,size):
            self.size = size
            
            myfont = pygame.font.SysFont("Comic Sans MS", size)

            label = myfont.render('10',True,(120,0,120))
            screen.blit(label, (l1, w1))

    time.sleep(1)

    circle_1(25)
    num_1(20)

    pygame.display.update()

    time.sleep(2)

    
    myfont = pygame.font.SysFont("Comic Sans MS", 25)

    label = myfont.render('it will be sent to the top :)',True,(200,50,50))
    screen.blit(label, (30, 120))
    pygame.display.update()

    time.sleep(3)

    for i in range(100):
         screen.fill((255,255,255))
         Tree = pygame.image.load('Tree.png')
         screen.blit(Tree,(300,50))
         circle_1(25)
         num_1(20)
         
         L1 += 2.05
         W1 -= 0.02
         l1 += 2.05
         w1 -= 0.02
         
         time.sleep(0.005)    
         pygame.display.update()

    time.sleep(1)

    myfont = pygame.font.SysFont("Comic Sans MS", 25)

    label = myfont.render('the next number will be 12 ==>',True,(0,0,0))
    screen.blit(label, (30, 450))
    pygame.display.update()

    L2=425
    W2=470
    
    class circle_2:
        def __init__(self,R):
            self.R = R
            pygame.draw.circle(screen,(0,0,0),(int(L2),int(W2)),R,5)

    l2 = 415
    w2 = 455

    class num_2:
        def __init__(self,size):
            self.size = size
                        
            myfont = pygame.font.SysFont("Comic Sans MS", size)            
            label = myfont.render('12',True,(0,100,150))
            screen.blit(label, (l2, w2))


    time.sleep(1)

    circle_2(25)
    num_2(20)

    time.sleep(1)

    R=0
    G=0
    B=0

    for i in range(255):
        myfont = pygame.font.SysFont("Comic Sans MS", 25)
         
        label = myfont.render('Tip:',True,(255,G,B))
        screen.blit(label, (30,20))
        
        label = myfont.render('numbers are random !!!',True,(R,G,B))
        screen.blit(label, (80, 20))
        
        R += 1
        G += 1
        B += 1
        time.sleep(0.02)
        pygame.display.update()

    pygame.draw.rect(screen,(255,255,255),(30,20,280,20),100)
    pygame.display.update()

    time.sleep(1)

    myfont = pygame.font.SysFont("Comic Sans MS", 20)
         
    label = myfont.render('it will be sent to the second branch',True,(0,100,150))
    screen.blit(label, (20,280))

    pygame.display.update()

    time.sleep(3)

    for i in range(100):
        screen.fill((255,255,255))
        
        Tree = pygame.image.load('Tree.png')
        screen.blit(Tree,(300,50))
        
        circle_1(25)
        circle_2(25)
        num_1(20)
        num_2(20)
        
        W2 -= 3.2
        w2 -= 3.2
        
        time.sleep(0.005)
        
        pygame.display.update()

    time.sleep(1)

    myfont = pygame.font.SysFont("Comic Sans MS", 20)
         
    label = myfont.render('now we should compare the numbers ',True,(0,0,0))
    screen.blit(label, (30,430))
    
    label = myfont.render("since 10 is less than 12 we'll make no change !!",True,(0,0,0))
    screen.blit(label, (30,470))

    pygame.display.update()

    time.sleep(1)

        
    time.sleep(1)
    pygame.draw.rect(screen,(255,255,255),(30,470,400,80),100)
    pygame.display.update()

    time.sleep(1)

    
    label = myfont.render('number 5',True,(0,0,0))
    screen.blit(label, (30,420))
    
    label = myfont.render('which is less than two other numbers !',True,(0,0,0))
    screen.blit(label, (30,460))

    pygame.display.update()

    time.sleep(1)

    label = myfont.render('it will be sent to the right',True,(0,0,0))
    screen.blit(label, (550,490))
    
    pygame.display.update()

    L3=680
    W3=460

    class circle_3:
        def __init__(self,R):
            self.R = R

            pygame.draw.circle(screen,(0,0,0),(int(L3),int(W3)),R,5)

    l3 = 674
    w3 = 445

    class num_3:
        def __init__(self,size):
            self.size = size
                       
            myfont = pygame.font.SysFont("Comic Sans MS", size)         
            label = myfont.render('5',True,(200,50,50))
            screen.blit(label, (l3,w3))

    time.sleep(2)
    
    circle_3(25)
    num_3(20)
    
    time.sleep(3)

    for i in range(100):
        screen.fill((255,255,255))

        Tree = pygame.image.load('Tree.png')
        screen.blit(Tree,(300,50))

        circle_1(25)
        circle_2(25)
        circle_3(25)
        num_1(20)
        num_2(20)
        num_3(20)

        L3 -= 0.4
        W3 -= 3.1
        l3 -= 0.4
        w3 -= 3.1

        time.sleep(0.005)            
        pygame.display.update()

        
    time.sleep(1)

    myfont = pygame.font.SysFont("Comic Sans MS", 25)         
    label = myfont.render('since 5 is less than 10',True,(0,0,0))
    screen.blit(label, (30,400))        
    label = myfont.render('they will exchange',True,(0,0,0))
    screen.blit(label, (30,450))
    pygame.display.update()

    time.sleep(3)

    for i in range(100):
        screen.fill((255,255,255))
        
        Tree = pygame.image.load('Tree.png')
        screen.blit(Tree,(300,50))
        
        circle_1(25)
        circle_2(25)
        circle_3(25)
        num_1(20)
        num_2(20)
        num_3(20)

        l3 -= 1.15
        w3 -= 1.2
        l1 += 1.152
        w1 += 1.18

        time.sleep(0.005)
        pygame.display.update()
    
    time.sleep(2)
    
    myfont = pygame.font.SysFont("Comic Sans MS", 20)         
    label = myfont.render('* you see the least number is at the top *',True,(200,0,0))
    screen.blit(label, (30,450))
    pygame.display.update()

    time.sleep(2)

    pygame.draw.rect(screen,(255,255,255),(20,450,400,20),50)
            
    myfont = pygame.font.SysFont("Comic Sans MS", 25)         
    label = myfont.render('there are some other numbers !!',True,(0,0,0))
    screen.blit(label, (30,420))

    pygame.display.update()

    time.sleep(1)
    
    label = myfont.render('you will see the rest of the animation',True,(0,0,0))
    screen.blit(label, (30,460))

    time.sleep(2)

    L4 = 50
    W4 = 100

    class circle_4:
        def __init__(self,R):
            self.R = R
            pygame.draw.circle(screen,(0,0,0),(int(L4),int(W4)),R,5)

    l4 = 44
    w4 = 85

    class num_4:
        def __init__(self,size):
            self.size = size
            
            myfont = pygame.font.SysFont("Comic Sans MS", size)         
            label = myfont.render('2',True,(60,70,80))
            screen.blit(label, (l4,w4))

    L5 = 50
    W5 = 180

    class circle_5:
        def __init__(self,R):
            self.R = R
            pygame.draw.circle(screen,(0,0,0),(int(L5),int(W5)),R,5)

    l5 = 40
    w5 = 165

    class num_5:
        def __init__(self,size):
            self.size = size
            
            myfont = pygame.font.SysFont("Comic Sans MS", size)         
            label = myfont.render('15',True,(100,0,200))
            screen.blit(label, (l5,w5))

    L6 = 50
    W6 = 260

    class circle_6:
        def __init__(self,R):
            self.R = R
            pygame.draw.circle(screen,(0,0,0),(int(L6),int(W6)),R,5)

    l6 = 40
    w6 = 245

    class num_6:
        def __init__(self,size):
            self.size = size
            
            myfont = pygame.font.SysFont("Comic Sans MS", size)         
            label = myfont.render('20',True,(90,100,150))
            screen.blit(label, (l6,w6))

    L7 = 50
    W7 = 340

    class circle_7:
        def __init__(self,R):
            self.R = R
            pygame.draw.circle(screen,(0,0,0),(int(L7),int(W7)),R,5)

    l7 = 44
    w7 = 322

    class num_7:
        def __init__(self,size):
            self.size = size

            
            myfont = pygame.font.SysFont("Comic Sans MS", 25)         
            label = myfont.render('8',True,(0,50,200))
            screen.blit(label, (l7,w7))

    circle_4(25)
    num_4(20)
    pygame.display.update()

    time.sleep(0.8)

    circle_5(25)
    num_5(20)
    pygame.display.update()

    time.sleep(0.8)

    circle_6(25)
    num_6(20)
    pygame.display.update()
    
    time.sleep(0.8)

    circle_7(25)
    num_7(20)

    pygame.display.update()

    time.sleep(2)
    
    for i in range(100):
        screen.fill((255,255,255))
        
        Tree = pygame.image.load('Tree.png')
        screen.blit(Tree,(300,50))

        circle_1(25)
        num_1(20)
        circle_2(25)
        num_2(20)
        circle_3(25)
        num_3(20)
        circle_4(25)
        num_4(20)
        circle_5(25)
        num_5(20)
        circle_6(25)
        num_6(20)
        circle_7(25)
        num_7(20)

        L4 += 3
        l4 += 3
        W4 += 1.3
        w4 += 1.3

        time.sleep(0.005)
        pygame.display.update()

    
    time.sleep(1)
            
    for i in range(100):
        screen.fill((255,255,255))
        
        Tree = pygame.image.load('Tree.png')
        screen.blit(Tree,(300,50))

        circle_1(25)
        num_1(20)
        circle_2(25)
        num_2(20)
        circle_3(25)
        num_3(20)
        circle_4(25)
        num_4(20)
        circle_5(25)
        num_5(20)
        circle_6(25)
        num_6(20)
        circle_7(25)
        num_7(20)
    
        l4 += 0.75
        w4 -= 0.8
        l2 -= 0.75
        w2 += 0.8

        time.sleep(0.005)
        pygame.display.update()

    time.sleep(1)

    
    for i in range(100):
        screen.fill((255,255,255))
        
        Tree = pygame.image.load('Tree.png')
        screen.blit(Tree,(300,50))

        circle_1(25)
        num_1(20)
        circle_2(25)
        num_2(20)
        circle_3(25)
        num_3(20)
        circle_4(25)
        num_4(20)
        circle_5(25)
        num_5(20)
        circle_6(25)
        num_6(20)
        circle_7(25)
        num_7(20)

        l4 += 1
        w4 -= 1.2
        l3 -= 1
        w3 += 1.2        

        time.sleep(0.005)
        pygame.display.update()

    time.sleep(1)

        
    for i in range(100):
        screen.fill((255,255,255))
        
        Tree = pygame.image.load('Tree.png')
        screen.blit(Tree,(300,50))

        circle_1(25)
        num_1(20)
        circle_2(25)
        num_2(20)
        circle_3(25)
        num_3(20)
        circle_4(25)
        num_4(20)
        circle_5(25)
        num_5(20)
        circle_6(25)
        num_6(20)
        circle_7(25)
        num_7(20)

        L5 += 4.1
        l5 += 4.1
        W5 += 0.6
        w5 += 0.6

        time.sleep(0.005)
        pygame.display.update()

    time.sleep(1)
    
    for i in range(100):
        screen.fill((255,255,255))
        
        Tree = pygame.image.load('Tree.png')
        screen.blit(Tree,(300,50))

        circle_1(25)
        num_1(20)
        circle_2(25)
        num_2(20)
        circle_3(25)
        num_3(20)
        circle_4(25)
        num_4(20)
        circle_5(25)
        num_5(20)
        circle_6(25)
        num_6(20)
        circle_7(25)
        num_7(20)

        L6 += 5.6
        l6 += 5.6
        W6 -= 0.45
        w6 -= 0.45
        
        time.sleep(0.005)
        pygame.display.update()
   

    time.sleep(1)

    
    for i in range(100):
        screen.fill((255,255,255))
        
        Tree = pygame.image.load('Tree.png')
        screen.blit(Tree,(300,50))

        circle_1(25)
        num_1(20)
        circle_2(25)
        num_2(20)
        circle_3(25)
        num_3(20)
        circle_4(25)
        num_4(20)
        circle_5(25)
        num_5(20)
        circle_6(25)
        num_6(20)
        circle_7(25)
        num_7(20)

        L7 += 6.4
        l7 += 6.4
        W7 -= 1.35
        w7 -= 1.35
        
        time.sleep(0.005)
        pygame.display.update()

    time.sleep(1)
    
    for i in range(100):
        screen.fill((255,255,255))
        
        Tree = pygame.image.load('Tree.png')
        screen.blit(Tree,(300,50))

        circle_1(25)
        num_1(20)
        circle_2(25)
        num_2(20)
        circle_3(25)
        num_3(20)
        circle_4(25)
        num_4(20)
        circle_5(25)
        num_5(20)
        circle_6(25)
        num_6(20)
        circle_7(25)
        num_7(20)
        
        l1 += 0.5
        w1 += 0.55
        l7 -= 0.5
        w7 -= 0.55
               
        time.sleep(0.005)
        pygame.display.update()

    time.sleep(2)

    myfont = pygame.font.SysFont("Comic Sans MS", 30)

    label = myfont.render('our heap is built properly :D',True,(0,0,0))

    screen.blit(label, (30, 420))
    pygame.display.update()

    time.sleep(3)
    screen.fill((255,255,255))

    R = 255
    G = 255
    B = 255
    
    for i in range(255):
        screen.fill((255,255,255))

        pygame.draw.circle(screen,(R,G,B),(400,300),250,10)

        R -= 1
        G -= 1
        B -= 1

        time.sleep(0.02)
        
        Tree = pygame.image.load('star.png')
        screen.blit(Tree,(380,20))
        
        pygame.display.update()

    time.sleep(1)

    R = 255
    G = 255
    B = 255

    for i in range(255):
        screen.fill((255,255,255))
                
        pygame.draw.circle(screen,(0,0,0),(400,300),250,10)

        label = myfont.render('Hossein Rezanejad',True,(R,G,B))
        screen.blit(label, (270, 200))

        label = myfont.render('Ali Sobhani',True,(R,G,B),10)
        screen.blit(label, (320, 250))
         
        label = myfont.render('Final Project :D',True,(R,G,B))
        screen.blit(label, (300, 450))

        R -=1
        B -= 1
        G -= 1
        
        Tree = pygame.image.load('star.png')
        screen.blit(Tree,(380,20))
        
        time.sleep(0.01)                    
        pygame.display.update()

    time.sleep(5) 

    

