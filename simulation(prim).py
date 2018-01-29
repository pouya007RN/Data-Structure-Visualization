import pygame,time

Algorithm = input()
if Algorithm == 'prim':
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800,600))
    screen.fill((255,255,255))

    pygame.draw.circle(screen,(0,0,0),(390,250),175,5)
    pygame.draw.circle(screen,(200,0,0),(390,250),170,170)
    
    myfont = pygame.font.SysFont("Comic Sans MS", 70)
    label = myfont.render('Prim',True,(0,0,0)) 
    screen.blit(label, (310,200))
    pygame.display.update()

    time.sleep(5)
    
    screen.fill((255,255,255))
    
    graph = pygame.image.load('graph.png')
    screen.blit(graph,(520,100))
    
    pygame.display.update()

    time.sleep(2)
    
    graph = pygame.image.load('qoute.png')
    screen.blit(graph,(100,350))
    
    myfont = pygame.font.SysFont("Comic Sans MS", 18)
    label = myfont.render('this is a graph',True,(0,0,0)) 
    screen.blit(label, (130,360))
    
    label = myfont.render('with numbers and',True,(0,0,0)) 
    screen.blit(label, (130,380))

    label = myfont.render('letters',True,(0,0,0)) 
    screen.blit(label, (130,400))

    pygame.display.update()

    time.sleep(3)
    
    pygame.draw.rect(screen,(255,255,255),(100,350,300,500),100)
    
    graph = pygame.image.load('qoute.png')
    screen.blit(graph,(100,350))

    time.sleep(1)

    label = myfont.render('we choose one of',True,(150,0,0)) 
    screen.blit(label, (130,360))

    label = myfont.render('the vertices',True,(150,0,0)) 
    screen.blit(label, (130,380))
    
    label = myfont.render('randomly',True,(150,0,0)) 
    screen.blit(label, (130,400))

    pygame.display.update()

    time.sleep(1)

    myfont = pygame.font.SysFont("Comic Sans MS", 30)
    label = myfont.render("for example 'f'",True,(0,0,0)) 
    screen.blit(label, (130,260))

    pygame.display.update()

    class text:
        def __init__(self,size,text,color,pos):
            self.size = size
            self.text = text
            self.color = color
            self.pos = pos
            
            myfont = pygame.font.SysFont("Comic Sans MS", size)
            label = myfont.render(text,True,color) 
            screen.blit(label, pos)

    class image:
        def __init__(self,name,pos):
            self.name = name
            self.pos = pos
           
            graph = pygame.image.load('qoute.png')
            screen.blit(graph,(100,350))


    pygame.draw.circle(screen,(0,255,0),(596,118),15,4)
    pygame.display.update()

    time.sleep(3)

    pygame.draw.rect(screen,(255,255,255),(50,300,400,500),100)

    image('qoute.png',(100,350))

    text(18,'now we have 3 choices',(0,0,0),(130,360))
    text(30,' d , e , a ',(0,0,0),(130,390))

    pygame.display.update()

    time.sleep(2)

    image('qoute.png',(130,350))
    time.sleep(1)
    text(18,'we should compare',(0,0,0),(130,360))
    text(18,'the length of',(0,0,0),(130,380))
    text(18,'each edge',(0,0,0),(130,400))

    pygame.display.update()

    time.sleep(2)

    pygame.draw.rect(screen,(255,255,255),(50,300,400,500),100)

    image('qoute.png',(100,350))
    text(18,'as you see',(0,0,0),(130,360))
    text(18,"'1' is the least!!",(0,0,0),(130,390))

    pygame.display.update()

    time.sleep(2)

    pygame.draw.line(screen,(0,255,0),(588,125),(537,215),5)
    pygame.draw.circle(screen,(0,150,100),(537,228),15,4)

    pygame.display.update()

    time.sleep(2)

    pygame.draw.rect(screen,(255,255,255),(50,300,400,500),100)

    image('qoute.png',(130,350))

    time.sleep(1)

    text(18,'we have 2 vertices !',(0,0,0),(130,360))
    text(18,'the least distance',(0,0,0),(130,380))
    text(18,'should be chosen',(0,0,0),(130,400))

    pygame.display.update()

    time.sleep(2)

    text(30,"'2' is the least !!!",(0,0,0),(130,200))

    pygame.display.update()

    time.sleep(2)

    pygame.draw.line(screen,(0,255,0),(603,126),(640,186),5)
    pygame.draw.circle(screen,(255,0,0),(650,196),15,4)

    pygame.display.update()

    pygame.draw.rect(screen,(255,255,255),(100,160,300,100),100)
    pygame.display.update()

    time.sleep(2)

    text(30,'now we keep this trend on :D',(0,0,0),(100,100))
    
    pygame.display.update()
    time.sleep(2)

    pygame.draw.rect(screen,(255,255,255),(80,80,450,40),50)
    pygame.draw.rect(screen,(255,255,255),(100,320,400,500),1000)
    pygame.display.update()

    time.sleep(1)

    text(60,'again 2 is the least !!',(0,0,0),(100,400))
    pygame.display.update()

    time.sleep(2)

    pygame.draw.rect(screen,(255,255,255),(50,350,650,100),120)
    pygame.display.update()

    time.sleep(1)

    pygame.draw.line(screen,(255,0,0),(660,186),(720,150),5)
    pygame.draw.circle(screen,(0,0,255),(735,150),15,4)
    pygame.display.update()

    time.sleep(1)

    text(60,' 5 is the least',(0,0,0),(100,400))
    pygame.display.update()

    time.sleep(2)

    pygame.draw.line(screen,(255,0,0),(650,211),(662,260),5)
    pygame.draw.circle(screen,(250,0,250),(665,274),15,4)
    pygame.display.update()

    time.sleep(1)

    pygame.draw.rect(screen,(255,255,255),(50,350,500,100),100)
    pygame.display.update()

    text(50,'just one vertice left',(0,0,0),(100,400))
    text(50,'and as you see 5 < 6 :D ',(0,0,0),(100,460))
    pygame.display.update()

    time.sleep(2)

    pygame.draw.rect(screen,(255,255,255),(50,350,600,150),200)
    
    pygame.display.update()

    time.sleep(1)

    pygame.draw.line(screen,(250,0,250),(676,275),(737,237),5)
    pygame.draw.circle(screen,(200,200,0),(748,228),15,4)
    pygame.display.update()

    time.sleep(1)

    text(50,'and it is finally done :)',(200,80,80),(100,400))
    pygame.display.update()

    time.sleep(3)

    screen.fill((255,255,255))

    time.sleep(1)
  
    W1 = 0    
    W2 = 600
    L3 = 800  
    L4 = 0
   
    for i in range(450):
        pygame.draw.circle(screen,(200,0,0),(200,W1),5,5)        
        pygame.draw.circle(screen,(0,0,0),(600,W2),5,5)

        W1 += 1
        W2 -= 1

        time.sleep(0.002)
        pygame.display.update()

    for i in range(650):
        pygame.draw.circle(screen,(200,0,0),(L3,200),5,5)
        pygame.draw.circle(screen,(0,0,0),(L4,400),5,5)

        L3 -= 1
        L4 += 1

        time.sleep(0.002)
        pygame.display.update()

    time.sleep(1)

    R = 255
    G = 255
    B = 255

    for i in range(255):
        text(30,'Hossein rezanejad',(R,G,B),(280,250))
        text(30,'Ali Sobhani',(R,G,B),(320,300))
        text(30,'Final Project :D',(R,G,B),(300,500))

        R -= 1
        G -= 1
        B -= 1

        time.sleep(0.002)
        pygame.display.update()
        

        
    
    
    

    

    
