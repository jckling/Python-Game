# -*- coding: utf-8 -*-

import pygame
from math import *

# 游戏属性
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60

# RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#游戏状态
MENU = 0
START = 1
EXIT = 2
status = MENU

# 方向
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
#LEFTUP = 4
#RIGHTUP = 5
#LEFTDOWN = 6
#RIGHTDOWN = 7

# 类型
SMALL = 0
BIG = 1
EXBIG = 2
TYPE = [SMALL, BIG, EXBIG]

class Player(pygame.sprite.Sprite):
    def __init__(self, init_img):
        self.image = init_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (400, 400)
        self.speed = 5
        self.is_hit = False     

    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, init_pos, init_dir, init_speed = 1, init_type = SMALL):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = init_speed
        self.direction = init_dir
        self.type = init_type
        self.distance = 0

    def move(self):
        # 移动
        self.distance += self.speed
        if self.direction == UP:
            self.rect.top -= self.speed
        elif self.direction == DOWN:
            self.rect.top += self.speed
        elif self.direction == LEFT:
            self.rect.left -= self.speed
        elif self.direction == RIGHT:
            self.rect.left += self.speed

    def change(self):
        # 类型转换
        if self.type == EXBIG:
            self.type = BIG
            self.distance = 0
        elif self.type == BIG:
            self.type = SMALL