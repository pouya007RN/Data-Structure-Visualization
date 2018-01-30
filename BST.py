import pygame
import time
pygame.init()
flat = pygame.display.set_mode((800,600))
white=(255,255,255)
black=(0,0,0)
tree = pygame.image.load('treee.png')



class node:
    def __init__(self , img , x , y):
        self.img = img
        self.x = x
        self.y = y

 
#for showing txt
def txt ( txt , x , y , sec =0 , font =10 ,color =(255,255,255)):
    myfont = pygame.font.SysFont("Comic Sans MS", font)

    label = myfont.render('%s'%txt,True,color)

    flat.blit(label, ( x , y))

    pygame.display.update()

    time.sleep(sec)




# for moving noseds
def goto(node , x , y ,tx ='' ,node2=None ,node3=None,node4=None,node5=None,node6=None,node7=None):

    if node.x <= x and node.y >= y:
        while node.x <= x or node.y >= y:
            if node.x <= x :
                node.x +=1

            if node.y >= y :
                node.y -=1

            flat.fill(white)
        
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
        
            flat.blit(node2.img ,(node2.x , node2.y))
            flat.blit(node3.img ,(node3.x , node3.y))
            flat.blit(node4.img ,(node4.x , node4.y))
            flat.blit(node5.img ,(node5.x , node5.y))
            flat.blit(node6.img ,(node6.x , node6.y))
            flat.blit(node7.img ,(node7.x , node7.y))
            flat.blit(node.img ,(node.x , node.y))
            txt(tx ,20 ,80,font = 30 , color = black)
            pygame.display.update()
        











#starting page
flat.fill(white)
pygame.draw.circle(flat,(0,0,0),(390,250),170,170)
txt('BST' , 350 , 220 ,sec =2 ,font = 40  )
pygame.display.update()
time.sleep(2)




flat.fill(white)

txt('BST has 3 operations :' , 20 , 40 ,sec =3 ,font = 30 , color =black  )

txt('insert' , 20 , 80 ,sec =1 ,font = 30 ,color =black )

txt('search' , 20 , 120 ,sec =1 ,font = 30 ,color =black )

txt('delete' , 20 , 160 ,sec =1 ,font = 30 ,color =black )


flat.fill(white)
pygame.display.update()




#loading node pics
t15 = pygame.image.load('T15.png')
t9 = pygame.image.load('T9.png')
t17 = pygame.image.load('T17.png')
t14 = pygame.image.load('T14.png')
t5 = pygame.image.load('T5.png')
t4 = pygame.image.load('T4.png')
t10 = pygame.image.load('T10.png')

#making node objs
a = node(t10 , 0,-90 )
b = node (t9 , 0,-90)
c = node(t15 , 0,-90)
d = node(t14 , 0,-90)
e = node(t17 , 0,-90)
f = node(t5 , 0,-90)
g = node(t4 , 0,-90)



#insertion descriptions
flat.fill(white)
txt('for inserting we have 3 principles:' , 20 , 40 ,sec =1 ,font = 30 ,color =black )

txt('if tree in None we just insert!' , 20 , 80 ,sec =1 ,font = 30 ,color =black )

txt('if the item >= node ; make right!' , 20 , 120 ,sec =1 ,font = 30 ,color =black )

txt('else make left!' , 20 , 160 ,sec =4 ,font = 30 ,color =black )



flat.fill(white)



#showing node inserts

goto(a , 345,190 ,tx ='inserting 10 ' , node2=b , node3 =c, node4 = d, node5 = e, node6 = f, node7 = g)
time.sleep(1)

goto(f , 95,390 ,tx = 'inserting 5 , left', node2=b , node3 =c, node4 = d, node5 = a, node6 = e, node7 = g)
time.sleep(1)

goto(b , 150,490 ,tx ='inserting 9 ,left ,right', node2=e , node3 =c, node4 = d, node5 = a, node6 = f, node7 = g)
time.sleep(1)

goto(c , 595, 390 ,tx = 'inserting 15 ,right' , node2=b , node3 =g, node4 = d, node5 = e, node6 = f, node7 = a)
time.sleep(1)

goto(d , 540, 490 ,tx = 'inserting 14 ,right ,left ', node2=b , node3 =c, node4 = a, node5 = e, node6 = f, node7 = g)
time.sleep(1)

goto(g , 40, 490 ,tx = 'inserting 4 ,left ,left ', node2=b , node3 =c, node4 = d, node5 = e, node6 = f, node7 = a)
time.sleep(1)

goto(e , 650,490 ,tx = 'inserting 17 ,right ,right ', node2=b , node3 =c, node4 = d, node5 = a, node6 = f, node7 = g)
time.sleep(1)




flat.fill(white)#refreshing the page
goto(g , 40, 490, node2=b , node3 =c, node4 = d, node5 = e, node6 = f, node7 = a)
time.sleep(1)



#removing descriptions
txt('for removing nodes there is 3 posibilities :' , 20 , 40 ,sec =3 ,font = 30 , color =black  )

txt('node with no child : we just remove it !' , 20 , 80 ,sec =2 ,font = 30 ,color =black )


goto(e , 890,690 ,tx = 'removing 17', node2=b , node3 =c, node4 = d, node5 = a, node6 = f, node7 = g)
time.sleep(5)


flat.fill(white)#refreshing the page
goto(e , 890,690, node2=b , node3 =c, node4 = d, node5 = a, node6 = f, node7 = g)
time.sleep(5)



txt('node with 1 child : replace it with its child ! ' , 20 , 80 ,sec =1 ,font = 30 ,color =black )
goto(c , 890, 690 ,tx = 'removing 15' , node2=b , node3 =g, node4 = d, node5 = e, node6 = f, node7 = a)
time.sleep(1)
goto(d , 595, 390 ,tx = 'replacing the child ', node2=b , node3 =c, node4 = a, node5 = e, node6 = f, node7 = g)
time.sleep(1)


flat.fill(white)#refreshing the page
goto(e , 890,690, node2=b , node3 =c, node4 = d, node5 = a, node6 = f, node7 = g)
time.sleep(5)


txt('node with 2 childs : replace it with the largest left node !' , 20 , 160 ,sec =1 ,font = 30 ,color =black )
goto(f , 890,690 ,tx = 'removing 5', node2=b , node3 =c, node4 = d, node5 = a, node6 = e, node7 = g)
time.sleep(1)
goto(g , 95, 390 ,tx = 'replacing the largest left ', node2=b , node3 =c, node4 = d, node5 = e, node6 = f, node7 = a)
time.sleep(1)




flat.fill(white)#refreshing the page
goto(e , 890,690, node2=b , node3 =c, node4 = d, node5 = a, node6 = f, node7 = g)
time.sleep(5)




txt('thats it !' , 350 , 220 ,sec =1 ,font = 30 ,color =black )

pygame.quit()




    
