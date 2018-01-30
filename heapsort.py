import pygame
import time
pygame.init()
flat = pygame.display.set_mode((800,600))
white=(255,255,255)
black = (0,0,0)

tree = pygame.image.load('tree.jpg')


def txt ( txt , x , y , sec =0 , font =10 ,color =(255,255,255)):
    myfont = pygame.font.SysFont("Comic Sans MS", font)

    label = myfont.render('%s'%txt,True,(0,0,0))

    flat.blit(label, ( x , y))

    pygame.display.update()

    time.sleep(sec)


flat.fill(white)

pygame.draw.circle(flat,(0,0,0),(390,250),170,170)

myfont = pygame.font.SysFont("Comic Sans MS", 50)

label = myfont.render('HeapSort',True,(250,250,250))

flat.blit(label, (300, 235))
pygame.display.update()
time.sleep(1)
flat.fill(white)



h7 = pygame.image.load('h7.png')
h91 = pygame.image.load('h91.png')
h23 = pygame.image.load('h23.png')
h12 = pygame.image.load('h12.png')
h5 = pygame.image.load('h5.png')
h40 = pygame.image.load('h40.png')
h1 = pygame.image.load('h1.png')





class node:
    def __init__(self , img , x , y):
        self.img = img
        self.x = x
        self.y = y




a = node(h7 , 375 ,200)
b = node(h91 , 375 ,200)
c = node(h23 , 375 ,200)
d = node(h12 , 375 ,200)
e = node(h5 , 375 ,200)
f = node(h40 , 375 ,200)
g = node(h1 , 375 ,200)



#animates the movements of nodes
def goto(node , x , y ,tx ='' ,node2=None ,node3=None,node4=None,node5=None,node6=None,node7=None):

    if node.x <= x and node.y >= y:
        while node.x <= x or node.y >= y:
            if node.x <= x :
                node.x +=1

            if node.y >= y :
                node.y -=1

            flat.fill(white)
            flat.blit(tree ,(100 ,-80))
            flat.blit(node2.img ,(node2.x , node2.y))
            flat.blit(node3.img ,(node3.x , node3.y))
            flat.blit(node4.img ,(node4.x , node4.y))
            flat.blit(node5.img ,(node5.x , node5.y))
            flat.blit(node6.img ,(node6.x , node6.y))
            flat.blit(node7.img ,(node7.x , node7.y))
            flat.blit(node.img ,(node.x , node.y))
            txt(tx ,20 ,80,font = 30 , color = black)
            pygame.display.update()
        
    
    elif node.x <= x and node.y <= y:
        while node.x <= x or node.y <= y:
            if node.x <= x :
                node.x +=1

            if node.y <= y :
                node.y +=1

            flat.fill(white)
            flat.blit(tree ,(100 ,-80))
            flat.blit(node2.img ,(node2.x , node2.y))
            flat.blit(node3.img ,(node3.x , node3.y))
            flat.blit(node4.img ,(node4.x , node4.y))
            flat.blit(node5.img ,(node5.x , node5.y))
            flat.blit(node6.img ,(node6.x , node6.y))
            flat.blit(node7.img ,(node7.x , node7.y))
            flat.blit(node.img ,(node.x , node.y))
            txt(tx ,20 ,80,font = 30 , color = black)
            pygame.display.update()

    elif node.x >= x and node.y >= y:
        while node.x >= x or node.y >= y:
            if node.x >= x :
                node.x -=1

            if node.y >= y :
                node.y -=1

            flat.fill(white)
            flat.blit(tree ,(100 ,-80))
            flat.blit(node2.img ,(node2.x , node2.y))
            flat.blit(node3.img ,(node3.x , node3.y))
            flat.blit(node4.img ,(node4.x , node4.y))
            flat.blit(node5.img ,(node5.x , node5.y))
            flat.blit(node6.img ,(node6.x , node6.y))
            flat.blit(node7.img ,(node7.x , node7.y))
            flat.blit(node.img ,(node.x , node.y))
            txt(tx ,20 ,80,font = 30 , color = black)
            pygame.display.update()


    elif node.x >= x and node.y <= y:
        while node.x >= x or node.y <= y:
            if node.x >= x :
                node.x -=1

            if node.y <= y :
                node.y +=1

            flat.fill(white)
            flat.blit(tree ,(100 ,-80))
            flat.blit(node2.img ,(node2.x , node2.y))
            flat.blit(node3.img ,(node3.x , node3.y))
            flat.blit(node4.img ,(node4.x , node4.y))
            flat.blit(node5.img ,(node5.x , node5.y))
            flat.blit(node6.img ,(node6.x , node6.y))
            flat.blit(node7.img ,(node7.x , node7.y))
            flat.blit(node.img ,(node.x , node.y))
            txt(tx ,20 ,80,font = 30 , color = black)
            pygame.display.update()





txt('In computer science, HeapSort is a comparison-based ',20,30,sec=2,font=20)
txt('sorting algorithm ,it extracts the largest element ' ,20,70,sec=2 ,font=20)
txt('based on heap data structure instead of linear-time search',20,110,sec=4 ,font=20)

flat.fill(white)

flat.blit(tree ,(100 ,-80))
txt('if we consider this as our Heap tree ,' ,20,30,sec=2,font=20)
txt( 'for sorting a list first we need to heapify it !',410,30,sec=4,font=20)



goto(a , 375,150 ,tx ='Heapify [7,91,23,12,5,40,1] ' , node2=b , node3 =c, node4 = d, node5 = e, node6 = f, node7 = g)
#time.sleep(1)

goto(b , 300,260 ,tx ='Heapify [7,91,23,12,5,40,1] ' , node2=a , node3 =c, node4 = d, node5 = e, node6 = f, node7 = g)
#time.sleep(1)

goto(c , 450,260 ,tx ='Heapify [7,91,23,12,5,40,1] ' , node2=b , node3 =a, node4 = d, node5 = e, node6 = f, node7 = g)
#time.sleep(1)

goto(d , 200,335 ,tx ='Heapify [7,91,23,12,5,40,1] ' , node2=b , node3 =c, node4 = a, node5 = e, node6 = f, node7 = g)
#time.sleep(1)

goto(e , 300,380 ,tx ='Heapify [7,91,23,12,5,40,1] ' , node2=b , node3 =c, node4 = d, node5 = a, node6 = f, node7 = g)
#time.sleep(1)

goto(f , 450,380 ,tx ='Heapify [7,91,23,12,5,40,1] ' , node2=b , node3 =c, node4 = d, node5 = e, node6 = a, node7 = g)
#time.sleep(1)

goto(g , 550,335 ,tx ='Heapify [7,91,23,12,5,40,1] ' , node2=b , node3 =c, node4 = d, node5 = e, node6 = f, node7 = a)
time.sleep(1)


pygame.display.update()


flat.fill(white)
goto(g , 550,335 ,tx ='' , node2=b , node3 =c, node4 = d, node5 = e, node6 = f, node7 = a)



txt( 'for finding the largest we replace',40,30,sec=2,font=20)
txt( 'larger child with its parent from bottom',410,30,sec=4,font=20)


goto(f , 450,260 , node2=b , node3 =c, node4 = d, node5 = e, node6 = a, node7 = g)

flat.fill(white)
goto(c , 450,380 , node2=b , node3 =a, node4 = d, node5 = e, node6 = f, node7 = g)


txt( 'if there was no move, we ',40,30,sec=2,font=20)
txt( 'switch to there parent untill the root',410,30,sec=4,font=20)

flat.fill(white)
goto(b , 375,150 , node2=a , node3 =c, node4 = d, node5 = e, node6 = f, node7 = g)
goto(a , 300,260 , node2=b , node3 =c, node4 = d, node5 = e, node6 = f, node7 = g)

txt( 'at the end we switch the top with right corner',40,30,sec=2,font=20)
txt( 'and remove it from the tree',40,70,sec=4,font=20)


flat.fill(white)
goto(g , 375,150 , node2=b , node3 =c, node4 = d, node5 = e, node6 = f, node7 = a)
goto(b , 675,500 , node2=a , node3 =c, node4 = d, node5 = e, node6 = f, node7 = g)

txt( 'repet this to end up the tree',40,30,sec=3,font=20)
flat.fill(white)

goto(d , 300,260 , node2=b , node3 =c, node4 = a, node5 = e, node6 = f, node7 = g)
goto(a , 200,335 , node2=b , node3 =c, node4 = d, node5 = e, node6 = f, node7 = g)

goto(f , 375,150 , node2=b , node3 =c, node4 = d, node5 = e, node6 = a, node7 = g)
goto(g , 450,260 , node2=b , node3 =c, node4 = d, node5 = e, node6 = f, node7 = a)

goto(c , 375,150 , node2=b , node3 =e, node4 = d, node5 = a, node6 = f, node7 = g)
goto(f , 575,500 , node2=b , node3 =c, node4 = d, node5 = e, node6 = a, node7 = g)

goto(e , 375,150 , node2=b , node3 =c, node4 = d, node5 = a, node6 = f, node7 = g)
goto(c , 475,500 , node2=b , node3 =e, node4 = d, node5 = a, node6 = f, node7 = g)

goto(d , 375,150 , node2=b , node3 =c, node4 = a, node5 = e, node6 = f, node7 = g)
goto(e , 300,260 , node2=b , node3 =c, node4 = d, node5 = a, node6 = f, node7 = g)

goto(a , 375,150 , node2=b , node3 =c, node4 = d, node5 = e, node6 = f, node7 = g)
goto(d , 375,500 , node2=b , node3 =c, node4 = a, node5 = e, node6 = f, node7 = g)

goto(a , 275,500 , node2=b , node3 =c, node4 = d, node5 = e, node6 = f, node7 = g)
goto(e , 175,500 , node2=b , node3 =c, node4 = d, node5 = a, node6 = f, node7 = g)
goto(g , 75,500 , node2=b , node3 =c, node4 = d, node5 = e, node6 = f, node7 = a)

txt( 'TADAAAAAA !',40,30,sec=1,font=20)


pygame.quit()






