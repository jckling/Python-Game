# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import math
from math import *
from four import *
import random

# 游戏初始化
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption("Split")
clock = pygame.time.Clock()
level = 6
running = True
Pass = False

# 字体
tFONT = pygame.font.Font('LCALLIG.ttf', 200)
bFONT = pygame.font.Font('MAIAN.ttf', 80)

# 音乐
menu_sound = pygame.mixer.Sound('olli.wav')
menu_sound.set_volume(0.4)
pygame.mixer.music.load('internet.mp3')
pygame.mixer.music.set_volume(0.5)

# 等级
level1_img = pygame.image.load('level1.png')
level2_img = pygame.image.load('level2.png')
level3_img = pygame.image.load('level3.png')
level4_img = pygame.image.load('level4.png')
level5_img = pygame.image.load('level5.png')
level6_img = pygame.image.load('level6.png')
LEVEL = [level1_img, level2_img, level3_img, level4_img, level5_img, level6_img]

# 玩家初始化
player_img = pygame.image.load('0.png')
player = Player(player_img)

# 方块初始化
enemy_img1 = pygame.image.load('1.png')
enemy_img2 = pygame.image.load('2.png')
enemy_img3 = pygame.image.load('3.png')
enemy_img4 = pygame.image.load('4.png')
enemy_img5 = pygame.image.load('5.png')
enemy_img = [enemy_img1, enemy_img2, enemy_img3, enemy_img4, enemy_img5]
heng = [-24, SCREEN_WIDTH]
zong = [-24, SCREEN_HEIGHT]
enemies = pygame.sprite.Group()
enemy_frequency = 0
enemy_num = 0
#NUMBER = [300, 350, 400, 450, 500, 800]
NUMBER = [20, 20, 20, 20, 20, 50]

# 开始菜单
def StartMenu():
    global status
    menu_sound.play(-1)
    enemy = Enemy(enemy_img5,(-24, 400), RIGHT, 1, EXBIG)

    while status != START:
        if status == MENU:
            while status == MENU:
                screen.fill(BLACK)

                titleSurf = tFONT.render('Split', True, WHITE)
                titleRect = titleSurf.get_rect()
                titleRect.centerx = screen.get_rect().centerx
                titleRect.centery = screen.get_rect().centery - 222
                screen.blit(titleSurf, titleRect)

                startSurf = bFONT.render('START', True, WHITE)
                startRect = startSurf.get_rect()
                startRect.left = 290
                startRect.top = screen.get_rect().centery + 40
                screen.blit(startSurf, startRect)

                exitSurf = bFONT.render('EXIT', True, WHITE)
                exitRect = exitSurf.get_rect()
                exitRect.left = 290
                exitRect.top = screen.get_rect().centery + 140
                screen.blit(exitSurf, exitRect)

                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if (x > startRect.left and x < startRect.right) and (y > startRect.top and y < startRect.bottom):
                            status = START
                        if (x > exitRect.left and x < exitRect.right) and (y > exitRect.top and y < exitRect.bottom):
                            status = EXIT
        elif status == EXIT:
            pygame.quit()
            exit()

# 方块产生频率
def CheckFrequency():
    global enemy_frequency
    enemy_frequency += 1
    if enemy_frequency >= 80:
        enemy_frequency = 0

# 产生方块
def ProduceEnemyLevel1():
    if enemy_frequency % 18 == 0:
        i = random.randint(0, 1)
        j = random.randint(0, 1)
        t = random.randint(0, 2)
        if i == 0:
            k = random.randint(0, SCREEN_WIDTH - 24)
            pos = heng[j], k
            if j == 0:
                enemy = Enemy(enemy_img[0], pos, RIGHT, 2, TYPE[0])
            else:
                enemy = Enemy(enemy_img[0], pos, LEFT, 2, TYPE[0])
        elif i == 1:
            k = random.randint(0, SCREEN_HEIGHT - 24)
            pos = k, zong[j]
            if j == 0:
                enemy = Enemy(enemy_img[0], pos, DOWN, 2, TYPE[0])
            else:
                enemy = Enemy(enemy_img[0], pos, UP, 2, TYPE[0])
        AddEnemy(enemy)
    CheckFrequency()
def ProduceEnemyLevel2():
    if enemy_frequency % 18 == 0:
        i = random.randint(0, 1)
        j = random.randint(0, 1)
        t = random.randint(0, 2)
        if i == 0:
            k = random.randint(0, SCREEN_WIDTH - 24)
            pos = heng[j], k
            if j == 0:
                enemy = Enemy(enemy_img[1], pos, RIGHT, 1, TYPE[1])
            else:
                enemy = Enemy(enemy_img[1], pos, LEFT, 1, TYPE[1])
        elif i == 1:
            k = random.randint(0, SCREEN_HEIGHT - 24)
            pos = k, zong[j]
            if j == 0:
                enemy = Enemy(enemy_img[1], pos, DOWN, 1, TYPE[1])
            else:
                enemy = Enemy(enemy_img[1], pos, UP, 1, TYPE[1])
        AddEnemy(enemy)
    CheckFrequency()
def ProduceEnemyLevel3():
    if enemy_frequency % 30 == 0:
        i = random.randint(0, 1)
        j = random.randint(0, 1)
        t = random.randint(0, 2)
        if i == 0:
            k = random.randint(0, SCREEN_WIDTH - 24)
            pos = heng[j], k
            if j == 0:
                enemy = Enemy(enemy_img[2], pos, RIGHT, 2, TYPE[1])
            else:
                enemy = Enemy(enemy_img[2], pos, LEFT, 2, TYPE[1])
        elif i == 1:
            k = random.randint(0, SCREEN_HEIGHT - 24)
            pos = k, zong[j]
            if j == 0:
                enemy = Enemy(enemy_img[2], pos, DOWN, 2, TYPE[1])
            else:
                enemy = Enemy(enemy_img[2], pos, UP, 2, TYPE[1])
        AddEnemy(enemy)
    CheckFrequency()
def ProduceEnemyLevel4():
    if enemy_frequency % 20 == 0:
        i = random.randint(0, 1)
        j = random.randint(0, 1)
        t = random.randint(0, 2)
        if i == 0:
            k = random.randint(0, SCREEN_WIDTH - 24)
            pos = heng[j], k
            if j == 0:
                enemy = Enemy(enemy_img[3], pos, RIGHT, 1, TYPE[2])
            else:
                enemy = Enemy(enemy_img[3], pos, LEFT, 1, TYPE[2])
        elif i == 1:
            k = random.randint(0, SCREEN_HEIGHT - 24)
            pos = k, zong[j]
            if j == 0:
                enemy = Enemy(enemy_img[3], pos, DOWN, 1, TYPE[2])
            else:
                enemy = Enemy(enemy_img[3], pos, UP, 1, TYPE[2])
        AddEnemy(enemy)
    CheckFrequency()
def ProduceEnemyLevel5():
    if enemy_frequency % 20 == 0:
        i = random.randint(0, 1)
        j = random.randint(0, 1)
        t = random.randint(0, 2)
        if i == 0:
            k = random.randint(0, SCREEN_WIDTH - 24)
            pos = heng[j], k
            if j == 0:
                enemy = Enemy(enemy_img[4], pos, RIGHT, 2, TYPE[2])
            else:
                enemy = Enemy(enemy_img[4], pos, LEFT, 2, TYPE[2])
        elif i == 1:
            k = random.randint(0, SCREEN_HEIGHT - 24)
            pos = k, zong[j]
            if j == 0:
                enemy = Enemy(enemy_img[4], pos, DOWN, 2, TYPE[2])
            else:
                enemy = Enemy(enemy_img[4], pos, UP, 2, TYPE[2])
        AddEnemy(enemy)
    CheckFrequency()
def ProduceEnemyLevel6():
    i = random.randint(1, 5)
    if i == 1:
        #ProduceEnemyLevel1()
        pass
    elif i == 2:
        #ProduceEnemyLevel2()
        pass
    elif i == 3:
        #ProduceEnemyLevel3()
        pass
    elif i == 4:
        ProduceEnemyLevel4()
    elif i == 5:
        ProduceEnemyLevel5()
def ProduceEnemy():
    if level == 1:
        ProduceEnemyLevel1()
    elif level == 2:
        ProduceEnemyLevel2()
    elif level == 3:
        ProduceEnemyLevel3()
    elif level == 4:
        ProduceEnemyLevel4()
    elif level == 5:
        ProduceEnemyLevel5()
    else:
        ProduceEnemyLevel6()

# 增加方块
def AddEnemy(enemy):
    global enemies, enemy_num
    enemies.add(enemy)
    enemy_num += 1

# 分裂
def Split():
    global enemies
    for enemy in enemies:
        if enemy.type == EXBIG:
            enemy1 = Enemy(enemy.image, enemy.rect.topleft, UP, enemy.speed, BIG)
            enemy2 = Enemy(enemy.image, enemy.rect.topleft, DOWN, enemy.speed, BIG)
            enemy3 = Enemy(enemy.image, enemy.rect.topleft, LEFT, enemy.speed, BIG)
            enemy4 = Enemy(enemy.image, enemy.rect.topleft, RIGHT, enemy.speed, BIG)
            if enemy.distance > SCREEN_WIDTH/4 + enemy_num%150:          
                if enemy.direction == LEFT:
                    enemies.add(enemy1, enemy2, enemy4)
                elif enemy.direction == RIGHT: 
                    enemies.add(enemy1, enemy2, enemy3)
                elif enemy.direction == UP:
                    enemies.add(enemy2, enemy3, enemy4)
                elif enemy.direction == DOWN:
                    enemies.add(enemy1, enemy3, enemy4)
                enemy.change()
        elif enemy.type == BIG:
            enemy1 = Enemy(enemy.image, enemy.rect.topleft, UP, enemy.speed)
            enemy2 = Enemy(enemy.image, enemy.rect.topleft, DOWN, enemy.speed)
            enemy3 = Enemy(enemy.image, enemy.rect.topleft, LEFT, enemy.speed)
            enemy4 = Enemy(enemy.image, enemy.rect.topleft, RIGHT, enemy.speed)  
            if enemy.distance > SCREEN_WIDTH/4 + enemy_num%150:                        
                if enemy.direction == LEFT:
                    enemies.add(enemy1, enemy2, enemy4)
                elif enemy.direction == RIGHT: 
                    enemies.add(enemy1, enemy2, enemy3)
                elif enemy.direction == UP:
                    enemies.add(enemy2, enemy3, enemy4)
                elif enemy.direction == DOWN:
                    enemies.add(enemy1, enemy3, enemy4)
                enemy.change()

# 移动方块
def MoveEnemy():
    global running, player, enemies
    for enemy in enemies:
        enemy.move()
        if pygame.sprite.collide_rect_ratio(0.98)(player, enemy):
            player.is_hit = True
            running = False
        if enemy.rect.left < -24 or enemy.rect.left > SCREEN_WIDTH or enemy.rect.top > SCREEN_HEIGHT or enemy.rect.top < -24:
            enemies.remove(enemy)

# 初始化
def Init():
    global level, player, enemies, enemy_num
    #level = 1
    player.is_hit = False
    enemies.empty()
    enemy_num = 0

# 游戏循环
def RunGame():
    global running, level, enemy_num, Pass
    menu_sound.stop()
    pygame.mixer.music.play(-1)
    Init()
    i = 0
    while running:
        # 控制游戏最大帧率为60
        clock.tick(FPS)
        
        # level up
        if level < 6:
            if enemy_num > NUMBER[level-1]:
                enemy_num = 0
                level += 1
                i = 0

        # produce enemy
        if level == 6 and enemy_num > NUMBER[level-1]:
            if len(enemies) == 0:
                running = False
                Pass = True
        else:
            ProduceEnemy()

        # move enemy
        MoveEnemy()
        Split()

        # draw
        screen.fill(0)
        # level
        if i < 180:
            screen.blit(LEVEL[level-1], (260, 340))
            i += 1
        # player
        screen.blit(player.image, player.rect)
        # enemies
        enemies.draw(screen)

        # update
        pygame.display.update()

        # 监听键盘事件
        key_pressed = pygame.key.get_pressed()
        # 若玩家被击中，则无效
        if not player.is_hit:
            if key_pressed[K_w] or key_pressed[K_UP]:
                player.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                player.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                player.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                player.moveRight()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() 

# 是否再来
def Again():
    global running

    levelSurf = bFONT.render('Level '+ str(level), True, WHITE)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (285, 240)
    screen.blit(levelSurf, levelRect)

    conSurf = bFONT.render('Continue?', True, WHITE)
    conRect = conSurf.get_rect()
    conRect.topleft = (57, 400)
    screen.blit(conSurf, conRect)

    yesSurf = bFONT.render('YES', True, WHITE)
    yesRect = yesSurf.get_rect()
    yesRect.topleft = (437, 400)
    screen.blit(yesSurf, yesRect)

    noSurf =bFONT.render('NO', True, WHITE)
    noRect = noSurf.get_rect()
    noRect.topleft = (607, 400)
    screen.blit(noSurf, noRect)

    # 更新屏幕
    pygame.display.update()

    while running == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (x > noRect.left and x < noRect.right) and (y > noRect.top and y < noRect.bottom):
                    pygame.quit()
                    exit()
                if (x > yesRect.left and x < yesRect.right) and (y > yesRect.top and y < yesRect.bottom):
                    running = True

# 通关
def PassGame():
    global running

    cSurf = bFONT.render('Congrtulations!', True, WHITE)
    cRect = cSurf.get_rect()
    cRect.topleft = (135, 240)
    screen.blit(cSurf, cRect)

    aSurf = bFONT.render('Play again?', True, WHITE)
    aRect = aSurf.get_rect()
    aRect.topleft = (45, 400)
    screen.blit(aSurf, aRect)

    yesSurf = bFONT.render('YES', True, WHITE)
    yesRect = yesSurf.get_rect()
    yesRect.topleft = (450, 400)
    screen.blit(yesSurf, yesRect)

    noSurf =bFONT.render('NO', True, WHITE)
    noRect = noSurf.get_rect()
    noRect.topleft = (630, 400)
    screen.blit(noSurf, noRect)

    # 更新屏幕
    pygame.display.update()

    while running == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (x > noRect.left and x < noRect.right) and (y > noRect.top and y < noRect.bottom):
                    pygame.quit()
                    exit()
                if (x > yesRect.left and x < yesRect.right) and (y > yesRect.top and y < yesRect.bottom):
                    running = True

# 游戏结束否
def Over():
    pygame.mixer.music.stop()
    clock.tick(FPS)
    if Pass:
        PassGame()
    else:
        Again()

# 主函数
def main():
    StartMenu()
    while running:
        RunGame()
        Over()

if __name__ == '__main__':  
    main() 