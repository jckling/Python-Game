# -*- coding: utf-8 -*-

import pygame
from sys import exit
from pygame.locals import *
from shoot import *
from math import *
import random

# 初始化游戏
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('CHROMATIC')
clock = pygame.time.Clock()
running = True

# 载入字体
BASICFONT = pygame.font.Font('CHILLER.ttf', 55)
BASICFONT2 = pygame.font.Font('comic.ttf', 40)

# 载入游戏音乐
bullet_sound = pygame.mixer.Sound('bullet.wav')
game_over_sound = pygame.mixer.Sound('over.wav')
menu_sound = pygame.mixer.Sound('angry.wav')
bullet_sound.set_volume(0.15)
game_over_sound.set_volume(0.4)
menu_sound.set_volume(0.4)
pygame.mixer.music.load('Tokyo.mp3')
pygame.mixer.music.set_volume(0.4)

# 载入背景图
background = pygame.image.load('bk.png')
about_img = pygame.image.load('about.png')
help_img = pygame.image.load('help.png')
menu_img = pygame.image.load('menu.png')

# 定义玩家对象
a = pygame.image.load('A.png')
b = pygame.image.load('B.png')
c = pygame.image.load('C.png')
player_img = [a, b, c]
player_pos = [219, 600]
score = 0
level = 1

# 定义子弹对象
a1 = pygame.image.load('bulletA.png')
b1 = pygame.image.load('bulletB.png')
c1 = pygame.image.load('bulletC.png')
bullet_img = [a1, b1, c1]

# 定义敌机对象
d = pygame.image.load('00.png')
e = pygame.image.load('01.png')
f = pygame.image.load('02.png')
g = pygame.image.load('03.png')
h = pygame.image.load('04.png')
i = pygame.image.load('05.png')
d0 = pygame.image.load('0.png')
e0 = pygame.image.load('1.png')
f0 = pygame.image.load('2.png')
g0 = pygame.image.load('3.png')
h0 = pygame.image.load('4.png')
i0 = pygame.image.load('5.png')
d1 = pygame.image.load('10.png')
e1 = pygame.image.load('11.png')
f1 = pygame.image.load('12.png')
g1 = pygame.image.load('13.png')
h1 = pygame.image.load('14.png')
i1 = pygame.image.load('15.png')
d2 = pygame.image.load('20.png')
e2 = pygame.image.load('21.png')
f2 = pygame.image.load('22.png')
g2 = pygame.image.load('23.png')
h2 = pygame.image.load('24.png')
i2 = pygame.image.load('25.png')
d3 = pygame.image.load('30.png')
e3 = pygame.image.load('31.png')
f3 = pygame.image.load('32.png')
g3 = pygame.image.load('33.png')
h3 = pygame.image.load('34.png')
i3 = pygame.image.load('35.png')
producer_img = [d, e, f, g, h, i]
square_img = [d0, e0, f0, g0, h0, i0]
squareplus_img = [d1, e1, f1, g1, h1, i1]
circle_img = [d2, e2, f2, g2, h2, i2]
explode_img = [d3, e3, f3, g3, h3, i3]
# 敌机信息
enemies = pygame.sprite.Group()
enemy_frequency = 0
ENEMY_SPEED = 1
# 敌机产生范围
border = [20, 96, 172, 248, 324, 400]
step = 60 - 24

# 存储被击毁的敌机和触碰到敌机的子弹
enemies_down = pygame.sprite.Group()
bullets_down = pygame.sprite.Group()

# 开始菜单
def StartMenu():
    global status
    menu_sound.play(-1)
    while status != START:
        if status == MENU:
            while status == MENU:
                screen.fill(BLACK)
                #screen.blit(menu_img, (0,0))
                bFONT = pygame.font.Font('CHILLER.ttf', 88)
                titleSurf = bFONT.render('CHROMATIC', True, TEXTCOLOR)
                titleRect = titleSurf.get_rect()
                titleRect.topleft = (70, 80)
                screen.blit(titleSurf, titleRect)

                startSurf = BASICFONT.render('START GAME', True, TEXTCOLOR)
                startRect = startSurf.get_rect()
                startRect.topleft = (124, 245)
                screen.blit(startSurf, startRect)

                aboutSurf = BASICFONT.render('ABOUT', True, TEXTCOLOR)
                aboutRect = aboutSurf.get_rect()
                aboutRect.topleft = (124, 325)
                screen.blit(aboutSurf, aboutRect)

                helpSurf = BASICFONT.render('HELP', True, TEXTCOLOR)
                helpRect = helpSurf.get_rect()
                helpRect.topleft = (124, 405)
                screen.blit(helpSurf, helpRect)

                exitSurf = BASICFONT.render('EXIT', True, TEXTCOLOR)
                exitRect = exitSurf.get_rect()
                exitRect.topleft = (124, 485)
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
                        if (x > aboutRect.left and x < aboutRect.right) and (y > aboutRect.top and y < aboutRect.bottom):
                            status = ABOUT
                        if (x > helpRect.left and x < helpRect.right) and (y > helpRect.top and y < helpRect.bottom):
                            status = HELP
                        if (x > exitRect.left and x < exitRect.right) and (y > exitRect.top and y < exitRect.bottom):
                            status = EXIT
        elif status == ABOUT:
            while status == ABOUT:
                # 绘制背景
                screen.blit(about_img, (0,0))
                # 返回菜单
                backSurf = BASICFONT.render('BACK', True, TEXTCOLOR)
                backRect = startSurf.get_rect()
                backRect.topleft = (18, 635)
                screen.blit(backSurf, backRect)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if (x >= backRect.left and x <= backRect.right) and (y >= backRect.top and y <= backRect.bottom):
                            status = MENU 
        elif status == HELP:
            while status == HELP:
                # 绘制背景
                screen.blit(help_img, (0,0))
                # 返回菜单
                backSurf = BASICFONT.render('BACK', True, TEXTCOLOR)
                backRect = startSurf.get_rect()
                backRect.topleft = (18, 635)
                screen.blit(backSurf, backRect)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if (x >= backRect.left and x <= backRect.right) and (y >= backRect.top and y <= backRect.bottom):
                            status = MENU 
        elif status == EXIT:
            pygame.quit()
            exit()

# 初始化
def Init():
    global enemies, enemies_down, bullets_down
    global score, level, enemy_frequency, ENEMY_SPEED
    score = 0
    level = 1
    enemy_frequency = 0
    ENEMY_SPEED = 1
    enemies.empty()
    enemies_down.empty()
    bullets_down.empty()

# 绘制敌机Producer
def drawProducer(produce_img, DISPLAYSURF):
    DISPLAYSURF.blit(produce_img[0],(20, 40))
    DISPLAYSURF.blit(produce_img[1],(20+60+16, 40))
    DISPLAYSURF.blit(produce_img[2],(20+60+16+60+16, 40))
    DISPLAYSURF.blit(produce_img[3],(20+60+16+60+16+60+16, 40))
    DISPLAYSURF.blit(produce_img[4],(20+60+16+60+16+60+16+60+16, 40))
    DISPLAYSURF.blit(produce_img[5],(480-60-20, 40))

# 产生敌机
def ProdeceEnemy(enemy_pos_x):
    i = 0
    while i < 6:
        if enemy_pos_x >= border[i] and enemy_pos_x <= border[i] + step:
            if level <= 2:
                enemy = Enemy(square_img[i], SQUARE, color[i], [enemy_pos_x, 40], ENEMY_SPEED)
            elif level > 2 and level <= 4:
                if enemy_pos_x % 2 ==0:
                    enemy = Enemy(square_img[i], SQUARE, color[i], [enemy_pos_x, 40], ENEMY_SPEED)
                else:
                    enemy = Enemy(squareplus_img[i], SQUAREplus, color[i], [enemy_pos_x, 40], ENEMY_SPEED)
            else:
                if enemy_pos_x % 3 ==0:
                    enemy = Enemy(square_img[i], SQUARE, color[i], [enemy_pos_x, 40], ENEMY_SPEED)
                elif enemy_pos_x % 3 ==1:
                    enemy = Enemy(square_img[i], SQUARE, color[i], [enemy_pos_x, 40], ENEMY_SPEED)
                else:
                    enemy = Enemy(circle_img[i], CIRCLE, color[i], [enemy_pos_x, 40], ENEMY_SPEED)
            enemies.add(enemy)
        i += 1

# 绘制子弹和敌机
def DrawBulletsAndEnemy():
    #绘制子弹爆炸
    for bullet in bullets_down:
        if bullet.explode_index < 111:
            bullet.explodeStart(screen)
        else:
            bullets_down.remove(bullet)
            continue
            
    # 绘制击毁动画
    for enemy_down in enemies_down:
        if enemy_down.explode_index < 150:
            enemy_down.explodeStart(screen)
        else:
            enemies_down.remove(enemy_down)
            continue

    # 绘制子弹和敌机
    player.bullets.draw(screen)
    for enemy in enemies:
        enemy.drawlife(screen)
    enemies.draw(screen)

# 移动子弹
def MoveBullets():
    # 移动子弹，若超出窗口范围则删除
    for bullet in player.bullets:
        bullet.move()
        if bullet.rect.bottom < 0 and bullet.type != STABLE:
            player.bullets.remove(bullet)
        elif bullet.rect.bottom < 0 or bullet.rect.right < 0 or bullet.rect.left > SCREEN_WIDTH:
            player.bullets.remove(bullet)

# 游戏循环
def RunGame():
    global enemies, enemy_frequency, ENEMY_SPEED
    global score, level, player
    global running

    player = Player(player_img, player_pos)
    Init()

    pygame.mixer.music.play(-1, 0.0)
    while running:
        # 控制游戏帧率
        clock.tick(FPS)

        # 获取按键情况,发射子弹
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > 240 and y < player_pos[1]:
                    t = (player_pos[1] - y) / (x - 240)
                    angle = degrees(atan(t)) - 90
                elif x < 240 and y < player_pos[1]:
                    t = (player_pos[1] - y) / (240 - x)
                    angle = 90 - degrees(atan(t))
                elif x > 30 and x < 30+120 and y > SCREEN_HEIGHT - 38 and player.energy_white == ENERGY:
                    player.status = NORMAL
                elif x >30+120+30 and x<30+120+30+120 and y>SCREEN_HEIGHT - 38 and player.energy_green == ENERGY:
                    player.status = HARD
                elif x > 30+120+30+120+30 and x < 30+120+30+120+30+120 and y > SCREEN_HEIGHT - 38 and player.energy_yellow == ENERGY:
                    player.status = EXHARD
                bullet_sound.play()
                if player.status == EASY:
                    player.shoot(bullet_img[player.status], angle)
                else:
                    player.shoot(bullet_img[player.status - 1], angle)
    
        # 移动子弹，若超出窗口范围则删除
        MoveBullets()

        # 若玩家在技能状态，消耗能量
        player.energyUse()

        # 生成敌机   
        if enemy_frequency % 51 == 0:
            enemy_pos_x = random.randint(20, 460 - 24)
            ProdeceEnemy(enemy_pos_x)
        enemy_frequency += 1
        if enemy_frequency >= 60:
            enemy_frequency = 0

        # 移动敌机，若超出范围则删除
        for enemy in enemies:
            enemy.move()
            # 判断玩家是否被击中
            if pygame.sprite.collide_circle_ratio(0.8)(enemy, player):
                enemy.explodeReady(explode_img)
                enemies_down.add(enemy)
                enemies.remove(enemy)
                player.life -= 1
                if player.life <= 0:
                    game_over_sound.play()
                    running = False
            if enemy.rect.top > player.rect.top + 35:
                enemies.remove(enemy)
                player.life -= 1
                if player.life <= 0:
                    #game_over_sound.play()
                    player.explodeReady(explode_img)
                    running = False

        # 将被击中的敌机对象添加到击毁敌机组中，用来爆炸
        for enemy in enemies:
            for bullet in player.bullets:
                if pygame.sprite.collide_circle_ratio(0.8)(bullet, enemy):
                    if bullet.type != STABLE:
                        bullet.explodeReady(explode_img[0])
                        bullets_down.add(bullet)
                        player.bullets.remove(bullet)
                    enemy.life -= 1
                    if enemy.life <= 0:
                        if enemy.type == SQUARE:
                            score += 100
                        elif enemy.type == SQUAREplus:
                            score += 200
                        elif enemy.type == CIRCLE:
                            score += 300
                        #elif enemy.type == :                    
                        if score % 2400 == 0:
                            level += 1
                            if level % 2:
                                player.speedUP()
                            ENEMY_SPEED += 0.38
                        player.energyUP()
                        enemy.explodeReady(explode_img)
                        enemies.remove(enemy)
                        enemies_down.add(enemy)

        # 绘制背景
        screen.fill(0)
        screen.blit(background, (0, 0))

        # 绘制玩家
        if player.status == EASY:
            screen.blit(player.image[player.status], player.rect)
        else:
            screen.blit(player.image[player.status - 1], player.rect)
        player.drawlife(screen)

        # 绘制敌方Producer、玩家能量条
        drawProducer(producer_img, screen)
        player.drawEnergyBar(screen)

        # 绘制子弹和敌机
        DrawBulletsAndEnemy()

        # 绘制得分
        score_font = pygame.font.Font('comic.ttf', 15)
        score_text = score_font.render('Score: '+ str(score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = [20, 53]
        screen.blit(score_text, score_rect)

        # 绘制等级
        level_text = score_font.render('Level: '+ str(level), True, WHITE)
        level_rect = level_text.get_rect()
        level_rect.topleft = [20, 71]
        screen.blit(level_text, level_rect)

        # 更新屏幕
        pygame.display.update()

# 结束画面
def Over():
    global running
    pygame.mixer.music.stop()
    game_over_sound.play()

    # 分数
    text = BASICFONT2.render('Score: '+ str(score), True, WHITE)
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery - 120

    # 等级
    text1 = BASICFONT2.render('Level: '+ str(level), True, WHITE)
    text1_rect = text1.get_rect()
    text1_rect.centerx = screen.get_rect().centerx
    text1_rect.centery = screen.get_rect().centery - 55

    # 再来一次
    again = BASICFONT2.render('Try Again ?', True, WHITE)
    again_rect = again.get_rect()
    again_rect.centerx = screen.get_rect().centerx
    again_rect.centery = screen.get_rect().centery + 70

    # 确认
    yes = BASICFONT2.render('YES', True, WHITE)
    yes_rect = yes.get_rect()
    yes_rect.centerx = screen.get_rect().centerx - 65
    yes_rect.centery = screen.get_rect().centery + 130

    # 拒绝
    no = BASICFONT2.render('NO', True, WHITE)
    no_rect = no.get_rect()
    no_rect.centerx = screen.get_rect().centerx + 65
    no_rect.centery = screen.get_rect().centery + 130

    while running == False:
        # 继续移动
        clock.tick(FPS)

        # 移动子弹，若超出窗口范围则删除
        MoveBullets()

        # 移动敌机
        for enemy in enemies:
            enemy.move()
            if enemy.rect.top > SCREEN_HEIGHT:
                enemies.remove(enemy)

        # 绘制背景
        screen.fill(0)
        screen.blit(background, (0,0))

        # 玩家爆炸
        if player.explode_index < 111:
            player.explodeStart(screen)
    
        # 绘制子弹和敌机
        DrawBulletsAndEnemy()

        # 绘制分数和等级
        screen.blit(text, text_rect)
        screen.blit(text1, text1_rect)

        # 绘制选项
        screen.blit(again, again_rect)
        screen.blit(yes, yes_rect)
        screen.blit(no, no_rect)

        # 更新屏幕
        pygame.display.update()

        # 结束游戏
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (x > no_rect.left and x < no_rect.right) and (y > no_rect.top and y < no_rect.bottom):
                    pygame.quit()
                    exit()
                if (x > yes_rect.left and x < yes_rect.right) and (y > yes_rect.top and y < yes_rect.bottom):
                    running = True

# 主函数
def main():
    StartMenu()
    menu_sound.stop()
    
    while running:
        RunGame()
        Over()

if __name__ == '__main__':  
    main() 