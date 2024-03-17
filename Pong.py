import pygame
import sys
from pygame.locals import *
import random 
from random import randint
from pygame import mixer
import time
pygame.init()
mixer.init()
mixer.music.load('E:\For_Pygame\Entities\Font\Sounds\y2mate.com - Eric Skiff  Underclocked  NO COPYRIGHT 8bit Music  Background.mp3')


mixer.music.set_volume(0.2)
mixer.music.play()
score = 0
score_2 = 0
WHITE = (255, 255, 255)
WIDTH = 1366
HEIGHT = 768
COOL = (190,255,255)
game_over = False
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
score_text_font = pygame.font.SysFont('E:\For_Pygame\Entities\Font\Ballistone.ttf',32)
Score_text = score_text_font.render('Score: ' + str(score) , True, WHITE)
Score_text_rect = Score_text.get_rect()

lose_text_font = pygame.font.SysFont('E:\For_Pygame\Entities\Font\Ballistone.ttf',64)
lose_text = lose_text_font.render('Player 1 loses! ', True, COOL)
lose2_text_font = pygame.font.SysFont('E:\For_Pygame\Entities\Font\Ballistone.ttf',64)
lose2_text = lose2_text_font.render('Player 2 loses! ', True, COOL)

restart_text_font = pygame.font.SysFont('E:\For_Pygame\Entities\Font\Ballistone.ttf',64)
restart_text = restart_text_font.render('Press r to restart', True, COOL)

winner1_text_font = pygame.font.SysFont('E:\For_Pygame\Entities\Font\Ballistone.ttf',64)
winner1_text = winner1_text_font.render('The winner is player 1', True, COOL)

winner2_text_font = pygame.font.SysFont('E:\For_Pygame\Entities\Font\Ballistone.ttf',64)
winner2_text = winner1_text_font.render('The winner is player 2', True, COOL)


score2_text_font = pygame.font.SysFont('E:\For_Pygame\Entities\Font\Ballistone.ttf',32)
Score2_text = score2_text_font.render('Score: ' + str(score) , True, WHITE)
Score2_text_rect = Score_text.get_rect()


lost2_text_font = pygame.font.SysFont('E:\For_Pygame\Entities\Font\Ballistone.ttf',64)
lost2_text = lost2_text_font.render('Player 2 Lost !', True, WHITE)


Player1 = pygame.Rect(6, 30, 15, 250)
Player2 = pygame.Rect(1300, 30, 15, 250)


ball = pygame.Rect(633, 334, 20, 30)


Player1_Forward = False
Player1_Downward = False
Player2_Forward = False
Player2_Downward = False
ball_Forward = False
ball_Downward = False

clock = pygame.time.Clock()

ball_velocity_x = -5
ball_velocity_y = 0

while True:
        screen.fill((0, 0, 0))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    Player1_Forward = True
                elif event.key == K_s:
                    Player1_Downward = True
                elif event.key == K_UP:
                    Player2_Forward = True
                elif event.key == K_DOWN:
                    Player2_Downward = True
            if event.type == pygame.KEYUP:
                if event.key == K_w:
                    Player1_Forward = False
                elif event.key == K_s:
                    Player1_Downward = False
                elif event.key == K_UP:
                    Player2_Forward = False
                elif event.key == K_DOWN:
                    Player2_Downward = False
                elif event.key == pygame.K_r:
                        ball.x = 633 
                        ball.y = 334
                        Player1.x = 6
                        Player1.y = 30
                        Player2.x = 1300
                        Player2.y = 30
                        score = 0
                        score_2 = 0
        
        if Player1_Forward:
            Player1.y -= 5
        if Player1_Downward:
            Player1.y += 5
        if Player2_Forward:
            Player2.y -= 5
        if Player2_Downward:
            Player2.y += 5

        ball.x += ball_velocity_x
        ball.y += ball_velocity_y

        if Player1.y <= 0 :
            Player1.y = 1
        elif Player1.bottom >= HEIGHT:
            Player1.bottom = HEIGHT -1
            
        if Player2.y <= 0 :
            Player2.y = 1
        elif Player2.bottom >= HEIGHT:
            Player2.bottom = HEIGHT -1
            
        if Player1.colliderect(ball):
            ball_velocity_x = random.randint(3, 5)
            ball_velocity_y = random.randint(-3, 3)
            score += 1
            Score_text = score_text_font.render('Score: ' + str(score) , True,(WHITE))
           
           
        if Player2.colliderect(ball):
            ball_velocity_x = random.randint(-5, -3)
            ball_velocity_y = random.randint(-3, 3)
            score_2 += 1
            Score2_text = score2_text_font.render('Score: ' + str(score) , True, WHITE)
        
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_velocity_y = -ball_velocity_y

        if ball.right < -10 :
           screen.blit(winner2_text, (183, 383))
           screen.blit(lose_text,(183,283))
           screen.blit(restart_text,(183,483))
           score = 0
           score_2 = 0
           Score_text = score_text_font.render('Score: ' + str(score) , True,(WHITE))
           Score2_text = score2_text_font.render('Score: ' + str(score) , True,(WHITE))
        
        
                    
        
        if ball.left > 1366 :
           screen.blit(winner1_text, (783, 383))
           screen.blit(lose2_text,(783,283))
           screen.blit(restart_text,(783,483))
           score = 0
           score_2 = 0
           Score2_text = score2_text_font.render('Score: ' + str(score) , True,(WHITE))
           Score_text = score_text_font.render('Score: ' + str(score) , True,(WHITE))


        screen.blit(Score_text,(310,0 ))
        screen.blit(Score2_text,(930,0))
        pygame.draw.rect(screen, WHITE, Player1)
        pygame.draw.rect(screen, WHITE, Player2)
        pygame.draw.circle(screen, (150,255,255), ball.center, ball.width // 2)
        pygame.draw.line(screen,WHITE, (683,50),(683,150),1)
        pygame.draw.line(screen,WHITE, (683,250),(683,350),1)
        pygame.draw.line(screen,WHITE, (683,450),(683,550),1)
        pygame.draw.line(screen,WHITE, (683,650),(683,750),1)

        
        pygame.draw.line(screen,WHITE,(100,350), (200,450))
        pygame.draw.line(screen,WHITE,(300,550), (400,650))
        pygame.draw.line(screen,WHITE,(500,750), (600,850))

        pygame.draw.line(screen,WHITE,(100,550), (200,650))
        
        pygame.draw.line(screen,WHITE,(300,750), (400,850))
        

        
        pygame.draw.line(screen,WHITE,(100,100), (200,200))
        pygame.draw.line(screen,WHITE,(300,300), (400,400))
        pygame.draw.line(screen,WHITE,(500,500), (600,600))
        pygame.draw.line(screen,WHITE,(700,700), (800,800))

        pygame.draw.line(screen,WHITE,(300,100), (400,200))
        pygame.draw.line(screen,WHITE,(500,300), (600,400))
        pygame.draw.line(screen,WHITE,(700,500), (800,600))
        pygame.draw.line(screen,WHITE,(900,700), (1000,800))

        pygame.draw.line(screen,WHITE,(500,100), (600,200))
        pygame.draw.line(screen,WHITE,(700,300), (800,400))
        pygame.draw.line(screen,WHITE,(900,500), (1000,600))
        pygame.draw.line(screen,WHITE,(1100,700), (1200,800))
    
        pygame.draw.line(screen,WHITE,(700,100), (800,200))
        pygame.draw.line(screen,WHITE,(900,300), (1000,400))
        pygame.draw.line(screen,WHITE,(1100,500), (1200,600))
        pygame.draw.line(screen,WHITE,(1300,700), (1400,800))
    
        pygame.draw.line(screen,WHITE,(900,100), (1000,200))
        pygame.draw.line(screen,WHITE,(1100,300), (1200,400))
        pygame.draw.line(screen,WHITE,(1300,500), (1400,600))
        pygame.draw.line(screen,WHITE,(1500,700), (1600,800))
    
        pygame.draw.line(screen,WHITE,(1100,100), (1200,200))
        pygame.draw.line(screen,WHITE,(1300,300), (1400,400))
        pygame.draw.line(screen,WHITE,(1500,500), (1600,600))
        pygame.draw.line(screen,WHITE,(1700,700), (1800,800))
    
    
        pygame.display.update()

        
        clock.tick(60)
