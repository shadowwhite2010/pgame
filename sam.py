import pygame  
  
pygame.init()  
win_len=600
win_bre=600
screen = pygame.display.set_mode((win_len,win_bre)) 
pygame.display.set_caption('shadow white') 
icon=pygame.image.load('sico.png')
pygame.display.set_icon(icon)
done = False  
clock = pygame.time.Clock() 

while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True 

    
    screen.fill((255, 25, 255))
    pygame.draw.circle(screen, (0, 222 , 222), (0, 250), 75) 
    pygame.display.update()
    clock.tick(6) 

pygame.quit()
quit()