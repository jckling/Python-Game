# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
FPS = 60

# RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#游戏状态
MENU = 0
START = 1
HELP = 2
OPTION = 3
EXIT = 4
status = MENU

# 玩家状态
RUN = 0
JUMP = 1

# 类型
PLAYER = 0
ARMY = 1
MONEY = 2

class MySprite(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        self.target_surface = target
        self.image = None
        self.master_image = None
        self.rect = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0 
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.x = 0
        self.y = 0
        self.type = ARMY

    def load(self, filename, width, height, columns, type = ARMY):
        # 加载图片
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1
        self.type = type

    def update(self, current_time, rate = FPS):
        # 图片更新
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = ( frame_x, frame_y, self.frame_width, self.frame_height )
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

    def move(self, pos_x, pos_y):
        # 移动
    	self.rect.top += pos_y
    	self.rect.left += pos_x

    def setpos(self, pos_x, pos_y):
        # 设置位置
        self.rect = Rect(pos_x, pos_y, self.frame_width, self.frame_height)
        if self.x == 0 and self.y == 0:
            self.x = pos_x
            self.y = pos_y

    def recover(self):
        # 恢复初始位置
        self.rect = Rect(self.x, self.y, self.frame_width, self.frame_height) 

class Player(pygame.sprite.Sprite):
    def __init__(self, animate, target):
        self.status = RUN
        self.speed = 10
        self.action = animate

    def Action(self, current_time, screen, rate = FPS):
        # 图片绘制
        self.action[self.status].update(current_time, rate)
        screen.blit(self.action[self.status].image, self.action[self.status].rect)