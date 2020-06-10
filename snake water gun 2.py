import random
import time
import pygame
pygame.init()
#colors
blue = (255,62,150)
yellow = (255,185,15)
green = (69,139,116)
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
com=0
user=0
font = pygame.font.SysFont(None, 30)
water = pygame.image.load('E:/games photos/water.jpg')
#water= pygame.transform.scale(water,(screen_width/2.5,screen_height/2.5)).convert_alpha()
snake = pygame.image.load('E:/games photos/snake.jpg')
#snake = pygame.transform.scale(bg,(screen_width,screen_height)).convert_alpha()
gun = pygame.image.load('E:/games photos/gun.jpg')
#gun = pygame.transform.scale(bg,(screen_width,screen_height)).convert_alpha()
pygame.display.set_caption("Snake water gun game")
#pygame.display.update()
j = -1
clock = pygame.time.Clock()
screen_width = 800
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))
def won():
        ex = False
        fps = 30
        while not ex:
            gameWindow.fill(blue)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    pygame.quit()
                    quit()
                if  event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                     pygame.quit()
                     quit()

            if com<user:
                font_text("You won the game",green,200,300)
            elif user<com:
                font_text("You loss the game",green,200,300)

            else:
                font_text("It is a tie",green,200,300)
            pygame.display.update()
            clock.tick(fps)
        pygame.quit()
        quit()
def font_text(text,color,x,y):
      screen_text = font.render(text,True,color)
      gameWindow.blit(screen_text,[x,y])
def welcome():
    enter = False
    time.sleep(3)
    global j
    j += 1
    if j==11:
      won() 
    pygame.display.update()    
    while not enter:
            gameWindow.fill(red)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        gameloop()
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if j<1:        
               font_text("Welcome to the snake,water,gun game",black,120,300)
            else:
               font_text("Press enter to continue",black,120,300)            
            pygame.display.update()
            clock.tick(30) 
    while j<11:
           gameloop()                          
def gameloop():  
        list=["Snake","Water","Gun"]
        i=1
        fps = 40        
        userch = ""
        global user
        while i<11:
          entry = False  
          while not entry:  
            gameWindow.fill(blue)
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN and event.key==pygame.K_s:
                    userch = "s"
                    print("s")
                    entry = True
                if event.type==pygame.KEYDOWN and event.key==pygame.K_w:
                    userch = "w"
                    entry = True
                if event.type==pygame.KEYDOWN and event.key==pygame.K_g:
                    userch = "g"
                    entry = True
            font_text("Enter s for snake,w for water and g for gun=",black,12,3)
            font_text(userch,black,450,3)
            i +=1
            pygame.display.update()                 
            ch=random.choice(list)
            font_text("Vs",black,250,290)
            #
            if ch=="Snake" and userch=="w":
                global com 
                com=com+10
                gameWindow.blit(snake,(10,180))
                gameWindow.blit(water,(300,180))
                font_text(f"Computer choose {ch}",black,10,30)
                font_text(f"Your points {user} Computer's points {com}",green,10,560)
                #pygame.display.update()

            elif ch=="Water" and  userch=="g":
                com+=10
                gameWindow.blit(gun,(10,180))
                gameWindow.blit(water,(300,180))
                font_text(f"Computer choose {ch}",black,10,30)
                font_text(f"Your points {user} Computer's points {com}",green,10,560) 
            elif ch=="Gun" and  userch=="s":
                #global com  
                com=com+10
                gameWindow.blit(snake,(10,180))
                gameWindow.blit(gun,(300,180))
                font_text(f"Computer choose {ch}",black,10,30)
                font_text(f"Your points {user} Computer's points {com}",green,10,560)
            elif ch=="Water" and  userch=="s":
                user=user + 10
                gameWindow.blit(snake,(10,180))
                gameWindow.blit(water,(300,180))
                font_text(f"Computer choose {ch}",black,10,30)
                font_text(f"Your points {user} Computer's points {com}",green,10,560)
            elif ch=="Snake" and  userch=="g":
                user=user+10
                gameWindow.blit(gun,(10,180))
                gameWindow.blit(snake,(300,180))
                font_text(f"Computer choose {ch}",black,10,30)
                font_text(f"Your point {user} Computer's points {com}",green,10,560)
            elif ch=="Gun" and  userch=="w":
                user+=10
                gameWindow.blit(water,(10,180))
                gameWindow.blit(gun,(300,180))
                font_text(f"Computer choose {ch}",black,10,30)
                font_text(f"Your points {user} Computer's points {com}",green,10,560)
            elif ch=="Snake" and  userch=="s":
                user+=10
                com=com+10
                gameWindow.blit(snake,(10,180))
                gameWindow.blit(snake,(300,180))
                font_text(f"Computer choose {ch}",black,10,30)
                font_text(f"Your points {user} Computer's points {com}",green,10,560)
            elif ch=="Water" and  userch=="w":
                user=user+10
                com=com+10
                gameWindow.blit(water,(10,180))
                gameWindow.blit(water,(300,180))
                font_text(f"Computer choose {ch}",black,10,30)
                font_text(f"Your points {user} Computer's points {com}",green,10,560)
            elif ch=="Gun" and  userch=="g":
                user+=10
                com=com+10
                gameWindow.blit(gun,(10,180))
                gameWindow.blit(gun,(300,180))
                font_text(f"Computer choose {ch}",black,10,30)
                font_text(f"Your points {user} Computer's points {com}",green,10,560)
                pygame.display.update()
                clock.tick(fps)
            pygame.display.update()
            clock.tick(fps)
        welcome()    
        ex = False
    

welcome()
