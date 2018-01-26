import pygame,random,time
Algorithm=input()
if Algorithm == 'merge sort':
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800,600))
    screen.fill((255,255,255))

    L1=445
    W1=495

    H=50
    

    class square_1:
        def __init__(self,side):

            self.side= 50
            pygame.draw.rect(screen,(200,200,200),(L1,W1,H,H))

    L2=345
    W2=495
        
    class square_2:
        def __init__(self,side):
            self.side= 50
            pygame.draw.rect(screen,(150,150,150),(L2,W2,H,H))


    L3=395
    W3=495


    class square_3:
        def __init__(self,side):
            self.side= 50
            pygame.draw.rect(screen,(100,100,100),(L3,W3,H,H))

    L4=295
    W4=495

    class square_4:
        def __init__(self,side):
            self.side= 50
            pygame.draw.rect(screen,(50,50,50),(L4,W4,H,H))



    

    pygame.draw.circle(screen,(0,0,0),(390,250),170,170)

    myfont = pygame.font.SysFont("Comic Sans MS", 50)

    label = myfont.render('Merge Sort',True,(250,250,250))

    screen.blit(label, (250, 200))
    pygame.display.update()
    time.sleep(4)

    screen.fill((255,255,255))
    
    square_1(10)
    square_2(10)
    square_3(10)
    square_4(10)


    myfont = pygame.font.SysFont("Comic Sans MS", 30)

    label = myfont.render('you see four squares on the screen',True,(0,0,0))

    screen.blit(label, (160, 400))
    pygame.display.update()


    time.sleep(5)
        
        

    for i in range(100):       
        screen.fill((255,255,255))
        square_1(10)
        square_2(10)
        square_3(10)
        square_4(10)
        L2 -= 0.5
        W2 -= 0.5
        L4 -= 0.5
        W4 -= 0.5
        L1 += 0.5
        W1 -= 0.5
        L3 += 0.5
        W3 -= 0.5
        time.sleep(0.05)
        pygame.display.update()
        
        myfont = pygame.font.SysFont("Comic Sans MS", 30)

        label = myfont.render('now the four squares are devided into two couples',True,(0,0,0))

        screen.blit(label, (50, 250))
        pygame.display.update()

       
    time.sleep(5)       

    for i in range(100):
        screen.fill((255,255,255))
        square_1(1)
        square_3(2)
        square_4(1)
        square_2(2)
        L4 -= 0.1
        W4 -= 0.1
        L2 += 0.1
        W2 -= 0.1
        L1 += 0.1
        W1 -= 0.1
        L3 -= 0.1
        W3 -= 0.1
    
        time.sleep(0.01)
        pygame.display.update()




        myfont = pygame.font.SysFont("Comic Sans MS", 30)

        label = myfont.render('we will devide the two couples one by one',True,(0,0,0))

        screen.blit(label, (120, 200))
        pygame.display.update()



        

    time.sleep(4)

    for i in range(100):
        screen.fill((255,255,255))
        square_1(1)
        square_2(2)
        square_3(3)
        square_4(4)
        L2 -= 0.6
        W2 -= 0.6
        L4 += 0.6
        W4 -= 0.6
        L1 -= 0.6
        W1 -= 0.6
        L3 += 0.6
        W3 -= 0.6
        time.sleep(0.01)
        pygame.display.update()




        myfont = pygame.font.SysFont("Comic Sans MS", 30)

        label = myfont.render('each side should be sorted separately',True,(0,0,0))

        screen.blit(label, (150, 300))
        pygame.display.update()


        

    time.sleep(4)

    for i in range(100):
        screen.fill((255,255,255))
        square_1(1)
        square_2(2)
        square_3(3)
        square_4(4)
        L1 -= 2.5
        W1 -= 0.8
        time.sleep(0.05)
        pygame.display.update()
        
        
    time.sleep(2)

    for i in range(100):
        
        screen.fill((255,255,255))
        square_1(1)
        square_2(2)
        square_3(3)
        square_4(4)
        L2 -= 0.001
        W2 -= 0.805
        time.sleep(0.05)
        pygame.display.update()
        
        
    time.sleep(2)

    for i in range(100):
        screen.fill((255,255,255))
        square_1(1)
        square_2(2)
        square_3(3)
        square_4(4)
        L3 -= 2.03
        W3 -= 0.805
        time.sleep(0.05)
        pygame.display.update()
        

    time.sleep(2)

    for i in range(100):
        screen.fill((255,255,255))
        square_1(1)
        square_2(2)
        square_3(3)
        square_4(4)
        L4 += 0.48
        W4 -= 0.81
        time.sleep(0.05)
        pygame.display.update()


    myfont = pygame.font.SysFont("Comic Sans MS", 30)

    label = myfont.render('you see the squares are sorted as for the RGB',True,(0,0,0))

    screen.blit(label, (100, 200))

    

    myfont = pygame.font.SysFont("Comic Sans MS", 20)

    label = myfont.render('(Hossein Rezanejad & Ali Sobhani)',True,(0,0,0))

    screen.blit(label, (420, 300))


    
    myfont = pygame.font.SysFont("Comic Sans MS", 60)

    label = myfont.render('** Merge Sort **',True,(0,0,0))

    screen.blit(label, (150, 50))

    

    myfont = pygame.font.SysFont("Comic Sans MS", 30)

    label = myfont.render('Final Project :D',True,(0,0,0))

    screen.blit(label, (300, 500))
        
        
            
    
    pygame.display.update()
        

    time.sleep(5)
