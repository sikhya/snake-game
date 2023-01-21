import pygame
import random
import  sys
import os
pygame.init()

pygame.mixer.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
display_Width = 900
display_Height = 600
gameWindow = pygame.display.set_mode((display_Width, display_Height))
bgimg = pygame.image.load(".\Data\Back_img.jpg")
bgimg = pygame.transform.scale(bgimg, (display_Width,display_Height)).convert_alpha()
pygame.display.set_caption("Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 45)

def textScreen(text, color , x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plotSnake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def WelCome():
    game_exit = False
    while not game_exit:
        gameWindow.fill((255,255,255))
        textScreen("-----: Welcome To Snake Game :-----", black, 195, 240)
        textScreen("Press Space Bar To Play", black, 270, 300)
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_exit = True
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            pygame.mixer.music.load('.\Data\BG_Song.mp3')
                            pygame.mixer.music.play()
                            gameLoop()
        pygame.display.update()
        clock.tick(40)

def gameLoop():
    game_exit = False
    game_over = False
    fps = 30
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 20
    if(not os.path.exists(".\Data\HighScore.txt")):
        with open(".\Data\HighScore.txt", "w") as f:
            f.write("0")
    with open(".\Data\HighScore.txt", "r") as f:
        highScore = f.read()
    food_x = random.randint(45, display_Width-50)
    food_y = random.randint(45, display_Height-50)
    init_velocity = 2
    score = 0
    snk_list = []
    snk_length = 1
    while not game_exit:
        if game_over:
            with open(".\Data\HighScore.txt","w")as f:
                f.write(str(highScore))
            gameWindow.fill(white)
            bgim = pygame.image.load(".\Data\Over_img.jpg")
            bgim = pygame.transform.scale(bgim, (display_Width,display_Height)).convert_alpha()
            gameWindow.blit(bgim, (0, 0))
            orange = (255, 85, 0)
            textScreen("Game Over! Press Enter To Continue", white, 180, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        WelCome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y =0
                    
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y =0

                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y =-init_velocity

                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = init_velocity

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score += 10
                food_x = random.randint(25, display_Width-50)
                food_y = random.randint(25, display_Height-50)
                snk_length += 5
                #pygame.mixer.music.load('beep.mp3')
                #pygame.mixer.music.play()
                if score > int(highScore):
                    highScore = score
              


            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            textScreen("Score: "+ str(score) + "        " +"High Score: "+str(highScore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('.\Data\Over.mp3')
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > display_Width or snake_y < 0 or snake_y > display_Height:
                game_over = True
                pygame.mixer.music.load('.\Data\Over.mp3')
                pygame.mixer.music.play()

            plotSnake(gameWindow, white, snk_list, snake_size)
            #pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
WelCome()
sys.exit()