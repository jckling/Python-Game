# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from math import *
import random

# 游戏属性
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 700
FPS = 30

#游戏状态
MENU = 0
START = 1
ABOUT = 2
HELP = 3
EXIT = 4
status = MENU

 # 敌机参数
PRODUCE_WIDTH = 32
SQUARE = 2
SQUAREplus = 3
CIRCLE = 4

# 玩家属性
LIFE = 8
EASY = 0
NORMAL = 1
HARD = 2
EXHARD = 3
ENERGY = 120
ENERGY_WHITE = 12
ENERGY_GREEN = 8
ENERGY_YELLOW = 6

# 子弹类型
SLOW = 0
FAST = 1
STABLE = 2

# 爆炸方向
LEFTTOP = 0
LEFTDOWN = 1
RIGHTTOP = 2
RIGHTDOWN = 3

#RGB
WHITE = (255, 255, 255, 80)
YELLOW = (255, 252, 113, 80)
BLUE = (58, 241, 236, 80)
GREEN = (212, 249, 55, 80)
ORANGE = (252, 175, 67, 80)
PURPLE = (231, 133, 254, 0)
color = [WHITE, YELLOW, BLUE, GREEN, ORANGE, PURPLE]
BLACK = (0, 0, 0)
TEXTCOLOR = (255, 255, 255)

# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, bullet_type, init_pos, bullet_angle, bullet_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate(bullet_img, bullet_angle)
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        self.type = bullet_type
        self.speed = bullet_speed
        self.angle = bullet_angle
        self.explosion = pygame.sprite.Group() 
        self.explode_index = 0

    def move(self):
        if self.angle > 0:
            self.rect.left -= self.speed * sin(radians(self.angle))
        elif self.angle < 0:
            self.rect.left += self.speed * sin(radians(-self.angle))       
        self.rect.top -= self.speed * cos(radians(self.angle))

    def explodeReady(self, explode_img):
        # 在一块区域内随机生成色彩方块
        j = random.randint(-50, 50)
        k = random.randint(-50, 50)
        pos = [self.rect.left + j, self.rect.top + k]
        exp = Explode(explode_img, pos, [self.rect.x, self.rect.y])
        self.explosion.add(exp)
        pos = [self.rect.left - j, self.rect.top - k]
        exp = Explode(explode_img, pos, [self.rect.x, self.rect.y])
        self.explosion.add(exp)

    def explodeStart(self, DISPLAYSURF):
        # 移动色彩方块
        self.explosion.draw(DISPLAYSURF)
        for exp in self.explosion:
            exp.move()
        self.explode_index += 1

# 玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self, player_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = []
        i = 0                        
        while i < 3:
            self.image.append(player_img[i])
            i += 1
        self.rect = player_img[0].get_rect()
        self.rect.topleft = init_pos
        self.bullets = pygame.sprite.Group()
        self.life = LIFE
        self.status = EASY
        self.energy_white = 0
        self.energy_yellow = 0
        self.energy_green = 0
        self.speed = 6
        self.explosion = pygame.sprite.Group()  
        self.explode_index = 0

    def shoot(self, bullet_img, bullet_angle):
        # 发射子弹
        if self.status == EASY:
            bullet = Bullet(bullet_img, SLOW, self.rect.midtop, bullet_angle, self.speed)
            self.bullets.add(bullet)
        elif self.status == NORMAL:
            bullet = Bullet(bullet_img, FAST, self.rect.midtop, bullet_angle, int(1.5 * self.speed))
            self.bullets.add(bullet)
        elif self.status == HARD:
            bullet = Bullet(bullet_img, STABLE, self.rect.midtop, bullet_angle, self.speed)
            self.bullets.add(bullet)
        elif self.status == EXHARD:
            bullet1 = Bullet(bullet_img, SLOW, self.rect.midtop, bullet_angle, self.speed)
            bullet2 = Bullet(bullet_img, SLOW, self.rect.midtop, bullet_angle + 20, self.speed)
            bullet3 = Bullet(bullet_img, SLOW, self.rect.midtop, bullet_angle - 20, self.speed)
            self.bullets.add(bullet1)
            self.bullets.add(bullet2)
            self.bullets.add(bullet3)

    def energyUP(self):
        # 积攒能量
        if self.status == EASY:
            if self.energy_white + ENERGY_WHITE <= ENERGY:
                self.energy_white += ENERGY_WHITE
            else:
                self.energy_white = ENERGY
            if self.energy_yellow + ENERGY_YELLOW <= ENERGY:
                self.energy_yellow += ENERGY_YELLOW
            else:
                self.energy_yellow = ENERGY
            if self.energy_green + ENERGY_GREEN <= ENERGY:
                self.energy_green += ENERGY_GREEN
            else:
                self.energy_green = ENERGY
        elif self.status == NORMAL:
            if self.energy_yellow + ENERGY_YELLOW <= ENERGY:
                self.energy_yellow += ENERGY_YELLOW
            else:
                self.energy_yellow = ENERGY
            if self.energy_green + ENERGY_GREEN <= ENERGY:
                self.energy_green += ENERGY_GREEN
            else:
                self.energy_green = ENERGY
        elif self.status == HARD:
            if self.energy_white + ENERGY_WHITE <= ENERGY:
                self.energy_white += ENERGY_WHITE
            else:
                self.energy_white = ENERGY
            if self.energy_yellow + ENERGY_YELLOW <= ENERGY:
                self.energy_yellow += ENERGY_YELLOW
            else:
                self.energy_yellow = ENERGY
        elif self.status == EXHARD:
            if self.energy_white + ENERGY_WHITE <= ENERGY:
                self.energy_white += ENERGY_WHITE
            else:
                self.energy_white = ENERGY
            if self.energy_green + ENERGY_GREEN <= ENERGY:
                self.energy_green += ENERGY_GREEN
            else:
                self.energy_green = ENERGY

    def energyUse(self):
        # 消耗能量
        if self.status == NORMAL:
            self.energy_white -= 0.48
            if self.energy_white <= 0:
                self.energy_white = 0
                self.status = EASY
        elif self.status == HARD:
            self.energy_green -= 0.48
            if self.energy_green <= 0:
                self.energy_green = 0
                self.status = EASY
        elif self.status == EXHARD:
            self.energy_yellow -= 0.48
            if self.energy_yellow <= 0:
                self.energy_yellow = 0
                self.status = EASY

    def drawEnergyBar(self, DISPLAYSURF):
        # 绘制能量条
        pygame.draw.rect(DISPLAYSURF, WHITE, [30, SCREEN_HEIGHT - 38, 120, 20], 2)
        pygame.draw.rect(DISPLAYSURF, WHITE, [30, SCREEN_HEIGHT - 38, self.energy_white, 20], 0)
        pygame.draw.rect(DISPLAYSURF, GREEN, [30+120+30, SCREEN_HEIGHT - 38, 120, 20], 2)
        pygame.draw.rect(DISPLAYSURF, GREEN, [30+120+30, SCREEN_HEIGHT - 38, self.energy_green, 20], 0)
        pygame.draw.rect(DISPLAYSURF, YELLOW, [30+120+30+120+30, SCREEN_HEIGHT - 38, 120, 20], 2)
        pygame.draw.rect(DISPLAYSURF, YELLOW, [30+120+30+120+30, SCREEN_HEIGHT - 38, self.energy_yellow, 20], 0)

    def drawlife(self, DISPLAYSURF):
        # 绘制血条
        pygame.draw.rect(DISPLAYSURF, BLUE, [10, SCREEN_HEIGHT - 10, SCREEN_WIDTH - 20, 4], 1)
        pygame.draw.rect(DISPLAYSURF, BLUE, [10, SCREEN_HEIGHT - 10, (SCREEN_WIDTH - 20) * (self.life / LIFE), 4], 0)

    def speedUP(self):
        # 加速
        self.speed += 2

    def explodeReady(self, explode_img):
        # 在一块区域内随机生成色彩方块
        i = 0
        while i < 10:
            j = random.randint(-80, 80)
            k = random.randint(-80, 0)
            pos = [self.rect.left + j, self.rect.top + k]
            exp = Explode(explode_img[0], pos, [self.rect.x, self.rect.y])
            self.explosion.add(exp)
            i += 1

    def explodeStart(self, DISPLAYSURF):
         # 移动色彩方块
        self.explosion.draw(DISPLAYSURF)
        for exp in self.explosion:
            exp.move()
        self.explode_index += 1

# 敌人类
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_type, enemy_color, init_pos, enemy_speed = 1):
       pygame.sprite.Sprite.__init__(self)
       self.image = enemy_img
       self.rect = self.image.get_rect()
       self.rect.topleft = init_pos
       self.type = enemy_type
       self.color = enemy_color
       self.speed = enemy_speed
       self.life = enemy_type
       self.origion = enemy_type
       self.explosion = pygame.sprite.Group()   
       self.explode_index = 0

    def move(self):
        # 移动
        self.rect.top += self.speed
    
    def drawlife(self, DISPLAYSURF):
        # 绘制生命条
        pygame.draw.rect(DISPLAYSURF, self.color, [self.rect.left - 4, self.rect.top - 8, PRODUCE_WIDTH, 3], 1)
        pygame.draw.rect(DISPLAYSURF, self.color, [self.rect.left - 4, self.rect.top - 8, PRODUCE_WIDTH * (self.life / self.origion), 3], 0)

    def explodeReady(self, explode_img):
        # 在一块区域内随机生成色彩方块
        if self.color == WHITE:
            img = explode_img[0]
        elif self.color == YELLOW:
            img = explode_img[1]
        elif self.color == BLUE:
            img = explode_img[2]
        elif self.color == GREEN:
            img = explode_img[3]
        elif self.color == ORANGE:
            img = explode_img[4]
        elif self.color == PURPLE:
            img = explode_img[5]
        i = 0
        while i < 8:
            j = random.randint(-50, 50)
            k = random.randint(-50, 0)
            pos = [self.rect.left + j, self.rect.top + k]
            exp = Explode(img, pos, [self.rect.x, self.rect.y])
            self.explosion.add(exp)
            i += 1

    def explodeStart(self, DISPLAYSURF):
         # 移动色彩方块
        self.explosion.draw(DISPLAYSURF)
        for exp in self.explosion:
            exp.move()
        self.explode_index += 1
        
# 爆炸
class Explode(pygame.sprite.Sprite):
    def __init__(self, explode_img, init_pos, original_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = explode_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        if init_pos[0] >= original_pos[0]:
            if init_pos[1] <= original_pos[1]:
                self.type = RIGHTTOP
            else:
                self.type = RIGHTDOWN
        else:
            if init_pos[1] <= original_pos[1]:
                self.type = LEFTTOP
            else:
                self.type = LEFTDOWN

    def move(self):
         # 移动色彩方块
        if self.type == LEFTTOP:
            self.rect.x -= 1
            self.rect.y += 1
        elif self.type == LEFTDOWN:
            self.rect.x -= 1
            self.rect.y -= 1
        elif self.type == RIGHTTOP:
            self.rect.x += 1
            self.rect.y += 1
        elif self.type == RIGHTDOWN:
            self.rect.x += 1
            self.rect.y -= 1