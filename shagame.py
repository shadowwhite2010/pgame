import pygame  
import numpy as np
import random

pygame.init()  
win_len=500
win_bre=600
inc=500//9
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def getdata(self, i):
        if self.head is None:
            return 0
        itr =self.head
        while i!=0:
            itr = itr.next
            i=i-1
        return itr.data
        


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remall(self):
        flag=0
        itr = self.head
        while itr:
            self.head = self.head.next
            if self.head is None:
                break


    def remove(self, data):
        

        flag=0
        if self.head==None:
            print("linked list empty")
            return
        itr = self.head
        if itr.data==data:
            self.head = self.head.next
            return
        it = None
        while itr.data!=data:
            it = itr
            itr = itr.next
            if itr is None:
                flag=1
                break
        if flag==0:
            it.next=itr.next

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


screen = pygame.display.set_mode((win_len,win_bre)) 
pygame.display.set_caption('shadow white') 
icon=pygame.image.load('sico.png')
pygame.display.set_icon(icon)

font1 = pygame.font.SysFont('arial.ttf', 72)
menu=font1.render('MENU', True, (120, 0, 0))  
gora=font1.render('GAME OVER', True, (120, 0, 0))

font2 =pygame.font.SysFont('arialblack.ttf', 60)
hard=font2.render('HARD', True, (0, 0, 0))  
easy=font2.render('EASY', True, (0, 0, 0))  
intermidiate=font2.render('MEDIUM', True, (0, 0, 0))  
won=font2.render('YOU WON', True, (0, 255, 0))

font3 = pygame.font.SysFont('arialblack.ttf', 30)
textrect=menu.get_rect()

restart=font2.render('RESTART', True, (0, 0, 0)) 
qit=font2.render('QUIT', True, (0, 0, 0)) 

level=36

# clock = pygame.time.Clock() 

def intro():
    done = False
    global level
    while not done:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                 
                pygame.quit()
                quit()

            #mouse inputs
            if event.type == pygame.MOUSEBUTTONDOWN:
                if win_len//2 - 100 <= mouse[0] <= win_len//2 - 100+280 and (win_bre//4)+100 <= mouse[1] <= (win_bre//4)+100+60: 
                    print("easy")
                    level=36
                    done=True

                if win_len//2 - 100 <= mouse[0] <= win_len//2 - 100+280 and (win_bre//4)+200 <= mouse[1] <= (win_bre//4)+200+60:
                    print("medium")
                    level=33
                    done=True
                
                if win_len//2 - 100 <= mouse[0] <= win_len//2 - 100+280 and (win_bre//4)+300 <= mouse[1] <= (win_bre//4)+300+60:
                    print("hard")
                    level=27
                    done=True
        
        screen.fill((255, 255, 255))

        mouse = pygame.mouse.get_pos()

        textrect.center=(win_len//2, win_bre//4)
        screen.blit(menu, textrect)

        if win_len//2 - 100 <= mouse[0] <= win_len//2 - 100+280 and (win_bre//4)+100 <= mouse[1] <= (win_bre//4)+100+60:
            pygame.draw.rect(screen, (0, 200, 0), [win_len//2 - 100, (win_bre//4)+100, 280, 60])
        else:
            pygame.draw.rect(screen, (0, 230, 0), [win_len//2 - 100, (win_bre//4)+100, 280, 60])

        textrect.center=(win_len//2, (win_bre//4)+130)
        screen.blit(easy, textrect)

        if win_len//2 - 100 <= mouse[0] <= win_len//2 - 100+280 and (win_bre//4)+200 <= mouse[1] <= (win_bre//4)+200+60:
            pygame.draw.rect(screen, (0, 0, 200), [win_len//2 - 100, (win_bre//4)+200, 280, 60])
        else:
            pygame.draw.rect(screen, (0, 0, 230), [win_len//2 - 100, (win_bre//4)+200, 280, 60])


        textrect.center=(win_len//2, (win_bre//4)+230)
        screen.blit(intermidiate, textrect)

        if win_len//2 - 100 <= mouse[0] <= win_len//2 - 100+280 and (win_bre//4)+300 <= mouse[1] <= (win_bre//4)+300+60:
            pygame.draw.rect(screen, (200, 0, 0), [win_len//2 - 100, (win_bre//4)+300, 280, 60])
        else:
            pygame.draw.rect(screen, (230, 0, 0), [win_len//2 - 100, (win_bre//4)+300, 280, 60])

        textrect.center=(win_len//2, (win_bre//4)+330)
        screen.blit(hard, textrect)

        
        pygame.display.update()
        # clock.tick(6) 

def drabox():
    
    
    

     


    for i in range(9):
        for j in range(9):
            if arr[i, j]!=0 and arr[i, j]!=-1:
                pygame.draw.rect(screen, (0, 153, 153), (inc*i, inc*j, inc, inc)) 

                txt=font3.render(str(arr[i, j]), True, (0, 0, 0))
                screen.blit(txt, (10+inc*i, 10+inc*j))

            if arr[i, j]==-1:
                pygame.draw.rect(screen, (100, 100, 100), (inc*i, inc*j, inc, inc))
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, 9*inc), 2) 
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (9*inc, 0), 2) 
    # line(surface, color, start_pos, end_pos, width) -> Rect
    x=0
    y=0
    for i in range(1,10):
        x=inc*i
        pygame.draw.line(screen, (0, 0, 0), (inc*i, 0), (inc*i, 9*inc), 2)
    
    for i in range(1, 10):
        
        pygame.draw.line(screen, (0, 0, 0), (0, inc*i), (9*inc, inc*i), 2)



# def draval(val):
#     txt=font3.render(str(val), True, (0, 0, 0))
#     #incomplete

def lfill(ll):
    # to refill the linked list
    ll.remall()
    for i in range (9):
        ll.insert_at_begining(i+1)

def lifill(li, ll):
    #to refill the list
    li.clear()
    for i in range(ll.get_length()):
        li.append(ll.getdata(i))

# def rawch(arr, ll, li, i):
#     for j in range(9):
#         if arr[i, j]!=0:
#             ll.remove(arr[i, j])

# def colch(arr, ll, li, j):
#     for i in range(9):
#         if arr[i, j]!=0:
#             ll.remove(arr[i, j])

# def er(li, ll, i, j, arr):
#     x=i//3
#     x=x*3
#     y=j//3
#     y=y*3
#     lifill(li, ll)
    
#     for l in range(x, x+3):
#         fl=0
#         for m in range(y, y+3):
#             flag=0
#             for k in range(9):
#                 if arr[l, m]==arr[i, k]:
#                     flag=1
#                     break
            
#             if flag==0:
#                 for k in range(9):
#                     if arr[l, m]==arr[k, j]:
#                         flag=1
#                         break
#             print("haloo")
#             if flag==0:
#                 t=arr[l, m] 
#                 arr[l, m]=arr[i, j]
#                 arr[i, j]=t
#                 if arr[l, m]==0:
#                     fl=0
#                     boxch(arr, ll, li, l, m)
#                     if len(li)==0:
                        
#                         return er(li, ll, l, m, arr)
#                     else:
#                         a= random.choice(li)
#                         arr[l, m]=a
#                         ll.remove(a)
#                         return 
                

        

def boxch(arr, ll, li, i, j):
    lifill(li, ll)
    for l in range(9):
        if arr[i, l]!=0:
            for k in range(len(li)):
                if arr[i, l]==li[k]:
                    li[k]=0

    for l in range(9):
        if arr[l, j]!=0:
            for k in range(len(li)):
                if arr[l, j]==li[k]:
                    li[k]=0
    while 0 in li:
        li.remove(0)
    print(li)
    
def sgen():
    global arr, level
    li=[]
    #this function will generate the sudoku 
    #take one extra copy of array 
    a=0
    l=0
    ll = LinkedList()
    
    #for our diagonal boxes
    # for k in range(3):
    #     lfill(ll)
    #     lifill(li, ll)
    #     l=k*3 
    #     for i in range(l, l+3):
    #         for j in range(l, l+3):
    #             a=random.choice(li)
    #             arr[i, j]=a
    #             ll.remove(a)
    #             lifill(li, ll)

    print(arr)
    # for i in range(9):
    #     for j in range(9):
    #         if arr[i, j]==0:
    #             lfill(ll)
    #             lifill(li, ll)
    #             print(li)
    #             rawch(arr, ll, li, i)
    #             colch(arr, ll, li, j)
    #             lifill(li, ll)
    #             print(li)
    #             a=random.choice(li)
    #             arr[i, j] = a 

    for k in range (0, 3):
        l=k*3
        lfill(ll)

        for i in range(3):
            for j in range(l, l+3):
                if arr[i, j]==0:
                    boxch(arr, ll, li, i, j)
                    if len(li)==0:
                        arr[i, j]=0
                    else:
                        a=random.choice(li)
                        arr[i, j] = a
                        print(arr[i, j])
                        ll.remove(a)
            print(arr)
    
    for k in range (0, 3):
        lfill(ll)
        l=k*3
        for i in range(3, 6):
            for j in range (l, l+3):
                if arr[i, j]==0:
                    boxch(arr, ll, li, i, j)
                    if len(li)==0:
                        arr[i, j]=0
                    else:
                        a=random.choice(li)
                        arr[i, j] = a
                        ll.remove(a)
            print(arr)
        
        

    for k in range (3):
        l=k*3
        lfill(ll)

        for i in range(6, 9):
            for j in range(l, l+3):
                if arr[i, j]==0:
                    boxch(arr, ll, li, i, j)
                    if len(li)==0:
                        arr[i, j]=0
                    else:
                        a=random.choice(li)
                        arr[i, j] = a
                        ll.remove(a)
            print(arr)

    for i in range (9):
        for j in range(9):
            if arr[i, j]==0:
                arr[i, j]=-1
    print(arr)
    global sol
    sol=np.copy(arr)
    # n in used for no elements to delete
    
    rem=level % 9
    if rem==0:
        n = 9-(level//9)
        lfill(ll)
        lifill(li, ll)
        for i in range(9):
            
            
            la=random.sample(li, k=n)
            for j in la:
                if arr[i, j-1]!=-1:
                    arr[i, j-1]=0
    else: 
        random.shuffle(li)
        for i in range(3):
            la=random.sample((li), k=6)
            for j in la:
                if arr[li[i], j]!=-1:
                    arr[li[i], j]=0
        for i in range(3, 9):
            la=random.sample((li), k=5)
            for j in la:
                if arr[li[i], j]!=-1:
                    arr[li[i], j]=0


    print(arr)



def click(pos): 
    global x 
    x = (pos[0])//inc 
    print("x:", x)
    global y 
    y = (pos[1])//inc
    print("y:", y) 
    

def game():
    done = False
    global level, arr, sol, x, y, flag
    x=None
    y=None
    key=None
    mistak=0
    flag=0
    flag1=0
    
    print(key)
    while not done:  
        for event in pygame.event.get():
              
            if event.type == pygame.QUIT:  
                 
                pygame.quit()
                quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse clicked")
                flag=1
                pos = pygame.mouse.get_pos()
                click(pos)
                print(flag)
                print(pos)
                
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9       
                print(key)           
                  
            

        
        screen.fill((255, 255, 255))
        mouse = pygame.mouse.get_pos()
        drabox()
        if flag==1 and arr[x, y]==0:
            pygame.draw.rect(screen, (0, 250, 0), (inc*x, inc*y, inc, inc)) 
            flag1=1
        if flag1==1 and key!=None:
            if key==sol[x, y]:
                arr[x, y]=sol[x, y]
                flag=0
                key=None
            else:
                mistak=mistak+1
                pygame.draw.rect(screen, (0, 250, 0), (inc*x, inc*y, inc, inc))
                flag=0
                key=None
                print(mistak)

        if mistak==3:
            done=True
        flag3=0
        for i in range(9):
            for j in range(9):
                if arr[i, j]==0:
                    flag3=1
                    break
        if flag3==0:
            textrect.center=(win_len//2, 20+(9*inc//2))
            screen.blit(won, textrect)

        
        
        
        pygame.display.update()
        # clock.tick(6) 

def gor():
    done = False
    
    while not done:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                 
                pygame.quit()
                quit()

            #mouse inputs
            if event.type == pygame.MOUSEBUTTONDOWN:
                

                if win_len//2 - 100 <= mouse[0] <= win_len//2 - 100+280 and (win_bre//4)+200 <= mouse[1] <= (win_bre//4)+200+60:
                    print("quit")
                    
                    pygame.quit()
                    quit()
        screen.fill((255, 255, 255))

        mouse = pygame.mouse.get_pos()

        textrect.center=(win_len//2, win_bre//4)
        screen.blit(gora, textrect)

        

        if win_len//2 - 100 <= mouse[0] <= win_len//2 - 100+280 and (win_bre//4)+200 <= mouse[1] <= (win_bre//4)+200+60:
            pygame.draw.rect(screen, (0, 0, 200), [win_len//2 - 100, (win_bre//4)+200, 280, 60])
        else:
            pygame.draw.rect(screen, (0, 0, 230), [win_len//2 - 100, (win_bre//4)+200, 280, 60])


        textrect.center=(win_len//2, (win_bre//4)+230)
        screen.blit(qit, textrect)


        pygame.display.update()
        # clock.tick(6) 

intro()
arr=np.zeros((9, 9), dtype=int)
sgen()
game()
gor()



pygame.quit()
quit()