#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## d
## File description:
## d
##

# Import the pygame module
import pygame
from random import randint
import pygame.freetype 
from os import system

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)
# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super(Player1, self).__init__()
        self.surf = pygame.Surface((25, 100))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect()

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super(Player2, self).__init__()
        self.surf = pygame.Surface((25, 100))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()

class Cup(pygame.sprite.Sprite):
    def __init__(self):
        super(Cup, self).__init__()
        self.surf = pygame.image.load("cup.png").convert_alpha()
        self.rect = self.surf.get_rect()

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((169, 169, 169))
        self.rect = self.surf.get_rect()

class Line(pygame.sprite.Sprite):
    def __init__(self):
        super(Line, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


# Move the sprite based on user keypresses
def update(self, pressed_keys):
    if pressed_keys[K_UP]:
        self.rect.move_ip(0, -5)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5, 0)

def collision(rectA, rectB):
    if rectB.right < rectA.left:
        # rectB est à gauche
        return False
    if rectB.bottom < rectA.top:
        # rectB est au-dessus
        return False
    if rectB.left > rectA.right:
        # rectB est à droite
        return False
    if rectB.top > rectA.bottom:
        # rectB est en-dessous
        return False
    # Dans tous les autres cas il y a collision
    return True


def menu_loop():
    system("clear")
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    pygame.init()
    pygame.mixer.init()
    GAME_FONT = pygame.freetype.Font("arcade.ttf", 44)
    GAME_FONT2 = pygame.freetype.Font("arcade.ttf", 74)
    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('music.ogg'),999)
    #pygame.mixer.Channel(1).play(pygame.mixer.Sound('boom.ogg'))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = 100
    Y = SCREEN_HEIGHT/2

    clock = pygame.time.Clock()
    running = True

    # Main loop
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                quit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[ord('b')]:
            main_game_vs()
        if pressed_keys[ord('a')]:
            main_game_ia()
        if pressed_keys[ord('c')]:
            main_game_ia_vs_ia()
        screen.fill((0, 0, 0))
        
        GAME_FONT2.render_to(screen, (320, 30), "PONG", (255, 255, 255))
        GAME_FONT.render_to(screen, (120, 230), "PRESS A TO PLAY AGAINST IA", (255, 255, 255))
        GAME_FONT.render_to(screen, (120, 330), "PRESS B TO PLAY VS", (255, 255, 255))
        GAME_FONT.render_to(screen, (120, 430), "PRESS C TO SEE IA VS IA", (255, 255, 255))
        
        pygame.display.flip()
        clock.tick(30)

def end_loop(MOD):
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('win.ogg'))
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    pygame.init()
    pygame.mixer.init()
    GAME_FONT = pygame.freetype.Font("arcade.ttf", 44)
  
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = 100
    Y = SCREEN_HEIGHT/2

    clock = pygame.time.Clock()
    running = True
    cup = Cup()
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                quit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            menu_loop()
        
        screen.fill((0, 0, 0))
        screen.blit(cup.surf, (300,150))
        if MOD == 1:
            GAME_FONT.render_to(screen, (230, 30), "PLAYER1 YOU WON", (255, 255, 255))
        if MOD == 2:
            GAME_FONT.render_to(screen, (230, 30), "PLAYER2 YOU WON", (255, 255, 255))
        if MOD == 3:
            GAME_FONT.render_to(screen, (280, 30), "IA YOU WON", (255, 255, 255))
        if MOD == 4:
            GAME_FONT.render_to(screen, (235, 30), "IA BLUE YOU WON", (255, 255, 255))
        if MOD == 5:
            GAME_FONT.render_to(screen, (235, 30), "IA RED YOU WON", (255, 255, 255))
        GAME_FONT.render_to(screen, (120, 530), "PRESS SPACE TO GO TO THE MENU", (255, 255, 255))
      
        pygame.display.flip()
        clock.tick(30)

def main_game_vs():
    pygame.init()
    GAME_FONT = pygame.freetype.Font("arcade.ttf", 60)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    P1X = 10
    P1Y = SCREEN_HEIGHT/2
    P2X = 766
    P2Y = SCREEN_HEIGHT/2
    BALLX = 385
    BALLY = 300
    POINT1 = 0
    POINT2 = 0
    E_X = 10
    E_Y = randint(15,569)
    E_Y2 = randint(15,569)
    direction = randint(1,2)
    b = 0
    player1 = Player1()
    player2 = Player2()
    ball = Ball()
    line = Line()
    running = True
    SPEED = 0
    while running:
        SPEED = SPEED + 0.02
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[K_UP] and P2Y > 5:
            P2Y = P2Y - 10
        if pressed_keys[K_DOWN] and P2Y < 495:
            P2Y = P2Y + 10
        if pressed_keys[ord('z')] and P1Y > 5:
            P1Y = P1Y - 10
        if pressed_keys[ord('s')] and P1Y < 495:
            P1Y = P1Y + 10
        if direction == 1:
            BALLX = BALLX - 2.5 - SPEED
        if direction == 2:
            BALLX = BALLX + 2.5 + SPEED
        if direction == 3:
            BALLX = BALLX - 2.5 - SPEED
            BALLY = BALLY + 2.5 + SPEED
        if direction == 4:
            BALLX = BALLX + 2.5 + SPEED
            BALLY = BALLY - 2.5 - SPEED
        if direction == 5:
            BALLX = BALLX + 2.5 + SPEED
            BALLY = BALLY + 2.5 + SPEED
        if direction == 6:
            BALLX = BALLX - 2.5 - SPEED
            BALLY = BALLY - 2.5 - SPEED
        
        if BALLY < 7 and direction == 4:
            direction = 5
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('wall.ogg'))
        if BALLY < 7 and direction == 6:
            direction = 3
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('wall.ogg'))
        if BALLY > 570 and direction == 3:
            direction = 6
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('wall.ogg'))
        if BALLY > 570 and direction == 5:
            direction = 4
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('wall.ogg'))
        
        if BALLX < 36 and BALLY <= P1Y + 100 and BALLY >= P1Y + 58:
            direction = 5
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX > 740 and BALLY <= P2Y + 100 and BALLY >= P2Y + 58:
            direction = 3
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX < 36 and BALLY <= P1Y + 58 and BALLY >= P1Y - 16:
            direction = 2
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX > 740 and BALLY <= P2Y + 58 and BALLY >= P2Y - 16:
            direction = 1
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX < 36 and BALLY <= P1Y + 16 and BALLY >= P1Y - 25:
            direction = 4
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX > 740 and BALLY <= P2Y + 16 and BALLY >= P2Y - 25:
            direction = 6
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX < 5:
            BALLX = 385
            BALLY = 300
            POINT2 = POINT2 + 1
            direction = randint(1,2)
            SPEED = 0
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('score.ogg'))
        if BALLX > 766:
            BALLX = 385
            BALLY = 300
            POINT1 = POINT1 + 1
            direction = randint(1,2)
            SPEED = 0
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('score.ogg'))
        if POINT1 == 10:
            end_loop(1)
        if POINT2 == 1:
            end_loop(2)
        screen.fill((0, 0, 0))
        screen.blit(player1.surf, (P1X,P1Y))
        screen.blit(player2.surf, (P2X,P2Y))
        screen.blit(ball.surf, (BALLX,BALLY))
        screen.blit(line.surf, (385,0))
        screen.blit(line.surf, (385,115))
        screen.blit(line.surf, (385,230))
        screen.blit(line.surf, (385,345))
        screen.blit(line.surf, (385,460))
        screen.blit(line.surf, (385,575))
        
        
        GAME_FONT.render_to(screen, (170, 30), str(POINT1), (255, 255, 255))          
        GAME_FONT.render_to(screen, (580, 30), str(POINT2), (255, 255, 255))
        pygame.display.flip()
        clock.tick(30)
    
def main_game_ia():
    pygame.init()
    GAME_FONT = pygame.freetype.Font("arcade.ttf", 60)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    P1X = 10
    P1Y = SCREEN_HEIGHT/2
    P2X = 766
    P2Y = SCREEN_HEIGHT/2
    BALLX = 385
    BALLY = 300
    POINT1 = 0
    POINT2 = 0
    X = randint(1,2)
    E_X = 10
    E_Y = randint(15,569)
    E_Y2 = randint(15,569)
    direction = randint(1,2)
    b = 0
    player1 = Player1()
    player2 = Player2()
    ball = Ball()
    line = Line()
    rdm_level = randint(0,200)
    running = True
    SPEED = 0
    while running:
        SPEED = SPEED + 0.02
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[ord('z')] and P1Y > 5:
            P1Y = P1Y - 10
        if pressed_keys[ord('s')] and P1Y < 495:
            P1Y = P1Y + 10
        P2Y = BALLY - rdm_level
        if P2Y >= 495:
            P2Y = 490
        if P2Y <= 5:
            P2Y = 10
        if direction == 1:
            BALLX = BALLX - 2.5 - SPEED
        if direction == 2:
            BALLX = BALLX + 2.5 + SPEED
        if direction == 3:
            BALLX = BALLX - 2.5 - SPEED
            BALLY = BALLY + 2.5 + SPEED
        if direction == 4:
            BALLX = BALLX + 2.5 + SPEED
            BALLY = BALLY - 2.5 - SPEED
        if direction == 5:
            BALLX = BALLX + 2.5 + SPEED
            BALLY = BALLY + 2.5 + SPEED
        if direction == 6:
            BALLX = BALLX - 2.5 - SPEED
            BALLY = BALLY - 2.5 - SPEED
        
        if BALLY < 7 and direction == 4:
            direction = 5
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('wall.ogg'))
        if BALLY < 7 and direction == 6:
            direction = 3
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('wall.ogg'))
        if BALLY > 570 and direction == 3:
            direction = 6
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('wall.ogg'))
        if BALLY > 570 and direction == 5:
            direction = 4
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('wall.ogg'))
        
        if BALLX < 36 and BALLY <= P1Y + 100 and BALLY >= P1Y + 58:
            direction = 5
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX > 740 and BALLY <= P2Y + 100 and BALLY >= P2Y + 58:
            direction = 3
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX < 36 and BALLY <= P1Y + 58 and BALLY >= P1Y - 16:
            direction = 2
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX > 740 and BALLY <= P2Y + 58 and BALLY >= P2Y - 16:
            direction = 1
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX < 36 and BALLY <= P1Y + 16 and BALLY >= P1Y - 25:
            direction = 4
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX > 740 and BALLY <= P2Y + 16 and BALLY >= P2Y - 25:
            direction = 6
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX < 5:
            BALLX = 385
            BALLY = 300
            POINT2 = POINT2 + 1
            direction = randint(1,2)
            SPEED = 0
            X = randint(1,2)
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('score.ogg'))
            rdm_level = randint(0,200)
        if BALLX > 766:
            BALLX = 385
            BALLY = 300
            POINT1 = POINT1 + 1
            direction = randint(1,2)
            SPEED = 0
            X = randint(1,2)
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('score.ogg'))
            rdm_level = randint(0,200)
        if POINT1 == 10:
            end_loop(1)
        if POINT2 == 10:
            end_loop(3)
        screen.fill((0, 0, 0))
        screen.blit(player1.surf, (P1X,P1Y))
        screen.blit(player2.surf, (P2X,P2Y))
        screen.blit(ball.surf, (BALLX,BALLY))
        screen.blit(line.surf, (385,0))
        screen.blit(line.surf, (385,115))
        screen.blit(line.surf, (385,230))
        screen.blit(line.surf, (385,345))
        screen.blit(line.surf, (385,460))
        screen.blit(line.surf, (385,575))
        GAME_FONT.render_to(screen, (170, 30), str(POINT1), (255, 255, 255))          
        GAME_FONT.render_to(screen, (580, 30), str(POINT2), (255, 255, 255))
        pygame.display.flip()
        clock.tick(30)
def main_game_ia_vs_ia():
    pygame.init()
    GAME_FONT = pygame.freetype.Font("arcade.ttf", 60)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    P1X = 10
    P1Y = SCREEN_HEIGHT/2
    P2X = 766
    P2Y = SCREEN_HEIGHT/2
    BALLX = 385
    BALLY = 300
    POINT1 = 0
    POINT2 = 0
    X = randint(1,2)
    E_X = 10
    E_Y = randint(15,569)
    E_Y2 = randint(15,569)
    direction = randint(1,2)
    direction = 3
    b = 0
    player1 = Player1()
    player2 = Player2()
    ball = Ball()
    line = Line()
    running = True
    SPEED = 0
    rdm_level = randint(0,200)
    rdm_level2 = randint(0,200)
    while running:
        SPEED = SPEED + 0.02
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        pressed_keys = pygame.key.get_pressed()
        
        P2Y = BALLY - rdm_level
        P1Y = BALLY - rdm_level2
        if P2Y >= 495:
            P2Y = 490
        if P2Y <= 5:
            P2Y = 10
        if P1Y >= 495:
            P1Y = 490
        if P1Y <= 5:
            P1Y = 10
        if direction == 1:
            BALLX = BALLX - 2.5 - SPEED
            direction = 3
        if direction == 2:
            BALLX = BALLX + 2.5 + SPEED
            direction = 4
        if direction == 3:
            BALLX = BALLX - 2.5 - SPEED
            BALLY = BALLY + 2.5 + SPEED
        if direction == 4:
            BALLX = BALLX + 2.5 + SPEED
            BALLY = BALLY - 2.5 - SPEED
        if direction == 5:
            BALLX = BALLX + 2.5 + SPEED
            BALLY = BALLY + 2.5 + SPEED
        if direction == 6:
            BALLX = BALLX - 2.5 - SPEED
            BALLY = BALLY - 2.5 - SPEED
        
        if BALLY < 7 and direction == 4:
            direction = 5
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('wall.ogg'))
        if BALLY < 7 and direction == 6:
            direction = 3
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('wall.ogg'))
        if BALLY > 570 and direction == 3:
            direction = 6
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('wall.ogg'))
        if BALLY > 570 and direction == 5:
            direction = 4
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('wall.ogg'))
        
        if BALLX < 36 and BALLY <= P1Y + 100 and BALLY >= P1Y + 58:
            direction = 5
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX > 740 and BALLY <= P2Y + 100 and BALLY >= P2Y + 58:
            direction = 3
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX < 36 and BALLY <= P1Y + 58 and BALLY >= P1Y - 16:
            direction = 2
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX > 740 and BALLY <= P2Y + 58 and BALLY >= P2Y - 16:
            direction = 1
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX < 36 and BALLY <= P1Y + 16 and BALLY >= P1Y - 25:
            direction = 4
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX > 740 and BALLY <= P2Y + 16 and BALLY >= P2Y - 25:
            direction = 6
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('pad.ogg'))
        if BALLX < 5:
            BALLX = 385
            BALLY = 300
            POINT2 = POINT2 + 1
            direction = randint(1,2)
            SPEED = 0
            X = randint(1,2)
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('score.ogg'))
            rdm_level = randint(0,200)
            rdm_level2 = randint(0,200)
        if BALLX > 766:
            BALLX = 385
            BALLY = 300
            POINT1 = POINT1 + 1
            direction = randint(1,2)
            SPEED = 0
            X = randint(1,2)
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('score.ogg'))
            rdm_level = randint(0,200)
            rdm_level2 = randint(0,200)
        if POINT1 == 10:
            end_loop(4)
        if POINT2 == 10:
            end_loop(5)
        screen.fill((0, 0, 0))
        screen.blit(player1.surf, (P1X,P1Y))
        screen.blit(player2.surf, (P2X,P2Y))
        screen.blit(ball.surf, (BALLX,BALLY))
        screen.blit(line.surf, (385,0))
        screen.blit(line.surf, (385,115))
        screen.blit(line.surf, (385,230))
        screen.blit(line.surf, (385,345))
        screen.blit(line.surf, (385,460))
        screen.blit(line.surf, (385,575))
        
        
        GAME_FONT.render_to(screen, (170, 30), str(POINT1), (255, 255, 255))          
        GAME_FONT.render_to(screen, (580, 30), str(POINT2), (255, 255, 255))
        #print(BALLX,P1Y,P2Y)
        pygame.display.flip()
        clock.tick(30)
#main_game()
menu_loop()