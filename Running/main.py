# -*- coding: utf-8 -*-

import pygame
from sys import exit
from pygame.locals import *
from running import *
import random

# 游戏初始化
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption("Running Game")
clock = pygame.time.Clock()
running = True

# 字体
BASICFONT = pygame.font.Font('comic.ttf', 30)
SFONT = pygame.font.Font('comic.ttf', 50)
BIGFONT = pygame.font.Font('CURLZ.TTF', 70)

# 载入游戏音乐
menu_sound = pygame.mixer.Sound('menu.wav')
menu_sound.set_volume(0.4)
select_sound = pygame.mixer.Sound('button.wav')
select_sound.set_volume(0.35)
per_sound = pygame.mixer.Sound('per.wav')
per_sound.set_volume(0.6)
jump_sound = pygame.mixer.Sound('jump.wav')
jump_sound.set_volume(0.6)
money_sound = pygame.mixer.Sound('qb.wav')
money_sound.set_volume(0.45)
game_over_sound = pygame.mixer.Sound('com.wav')
pygame.mixer.music.load('circles.mp3')
pygame.mixer.music.set_volume(0.5)
sound = True

# 载入菜单
menu_img = pygame.image.load('menu.png')
menu_img = pygame.transform.scale(menu_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
help_img = pygame.image.load('help.png')
on_img = pygame.image.load('on.png')
off_img = pygame.image.load('off.png')

# 难度
NORMAL = 3
HARD = 2
difficulty = NORMAL

# 过渡画面
per = pygame.image.load('xian.jpg')
money_img = pygame.image.load('money.png')

# 滚动背景初始化
background = pygame.image.load('bk5.png')
background1 = pygame.image.load('bk6.png')
bk = background
bk1 = background
rect = bk.get_rect()
width = rect.right - rect.left
x1 = 0
x2 = width

# 结束画面
over = pygame.image.load('o1.png')
end = pygame.image.load('66.png')
end = pygame.transform.scale(end, (90, 100))

# 玩家动画
run = MySprite(screen)
run.load('AA.png',120, 150, 6, PLAYER)
run.setpos(150, 400)
jump = MySprite(screen)
jump.load('AA.png',120, 150, 6, PLAYER)
jump.setpos(150, 400)
animate = [run, jump]
# 玩家信息
player = Player(animate, screen)
level = 1
distance = 0
money = 0

# 金币信息
QB1 = MySprite(screen)
QB1.load('QB.png', 30, 43, 7, MONEY)
QB1.setpos(SCREEN_WIDTH, SCREEN_HEIGHT-50-43*3)
QB2 = MySprite(screen)
QB2.load('QB.png', 30, 43, 7, MONEY)
QB2.setpos(SCREEN_WIDTH-40, SCREEN_HEIGHT-50-43*3)
QB3 = MySprite(screen)
QB3.load('QB.png', 30, 43, 7, MONEY)
QB3.setpos(SCREEN_WIDTH-80, SCREEN_HEIGHT-50-43*3)
QB4 = MySprite(screen)
QB4.load('QB.png', 30, 43, 7, MONEY)
QB4.setpos(SCREEN_WIDTH-120, SCREEN_HEIGHT-50-43*3)

QB5 = MySprite(screen)
QB5.load('QB.png', 30, 43, 7, MONEY)
QB5.setpos(SCREEN_WIDTH, SCREEN_HEIGHT-50-43*5)
QB6 = MySprite(screen)
QB6.load('QB.png', 30, 43, 7, MONEY)
QB6.setpos(SCREEN_WIDTH-40, SCREEN_HEIGHT-50-43*5)
QB7 = MySprite(screen)
QB7.load('QB.png', 30, 43, 7, MONEY)
QB7.setpos(SCREEN_WIDTH-80, SCREEN_HEIGHT-50-43*5)
QB8 = MySprite(screen)
QB8.load('QB.png', 30, 43, 7, MONEY)
QB8.setpos(SCREEN_WIDTH-120, SCREEN_HEIGHT-50-43*5)

QB9 = MySprite(screen)
QB9.load('QB.png', 30, 43, 7, MONEY)
QB9.setpos(SCREEN_WIDTH, SCREEN_HEIGHT-50-43*7)
QB10 = MySprite(screen)
QB10.load('QB.png', 30, 43, 7, MONEY)
QB10.setpos(SCREEN_WIDTH-40, SCREEN_HEIGHT-50-43*7)
QB11 = MySprite(screen)
QB11.load('QB.png', 30, 43, 7, MONEY)
QB11.setpos(SCREEN_WIDTH-80, SCREEN_HEIGHT-50-43*7)
QB12 = MySprite(screen)
QB12.load('QB.png', 30, 43, 7, MONEY)
QB12.setpos(SCREEN_WIDTH-120, SCREEN_HEIGHT-50-43*7)

Qa = [QB1, QB2, QB3, QB4]
Qb = [QB5, QB6, QB7, QB8]
Qc = [QB9, QB10, QB11, QB12]
Qd = [QB1, QB2, QB3, QB4, QB5, QB6, QB7, QB8]
Qe = [QB5, QB6, QB7, QB8, QB9, QB10, QB11, QB12]
Qf = [QB1, QB2, QB3, QB4, QB5, QB6, QB7, QB8, QB9, QB10, QB11, QB12]
Qg = [QB1, QB2, QB3, QB5, QB6, QB7]
Qh = [QB5, QB6, QB7, QB9, QB10, QB11]

# 敌人信息
enemy1 = MySprite(screen)
enemy1.load('01.png', 90, 130, 4)
enemy1.setpos(SCREEN_WIDTH, SCREEN_HEIGHT-50-130)
enemy2 = MySprite(screen)
enemy2.load('02.png', 90, 125, 4)
enemy2.setpos(SCREEN_WIDTH, SCREEN_HEIGHT-50-125)
enemy3 = MySprite(screen)
enemy3.load('03.png', 85, 112, 4)
enemy3.setpos(SCREEN_WIDTH, SCREEN_HEIGHT-50-112)
enemy4 = MySprite(screen)
enemy4.load('04.png', 85, 116, 4)
enemy4.setpos(SCREEN_WIDTH, SCREEN_HEIGHT-50-116)
enemy5 = MySprite(screen)
enemy5.load('05.png', 80, 115, 6)
enemy5.setpos(SCREEN_WIDTH, SCREEN_HEIGHT-50-115)
enemy6 = MySprite(screen)
enemy6.load('06.png', 70, 105, 6)
enemy6.setpos(SCREEN_WIDTH, SCREEN_HEIGHT-50-105)
enemy7 = MySprite(screen)
enemy7.load('07.png', 80, 106, 6)
enemy7.setpos(SCREEN_WIDTH, SCREEN_HEIGHT-50-106)
enemy8 = MySprite(screen)
enemy8.load('08.png', 100, 100, 5)
enemy8.setpos(SCREEN_WIDTH, SCREEN_HEIGHT-50-100)
enem = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, QB1, QB5, QB9]
enemies = pygame.sprite.Group()


# 开始菜单
def StartScreen():
    global status, sound, difficulty
    menu_sound.play(-1)
    while status != START:
        if status == MENU:
            while status == MENU:
                screen.fill(0)
                screen.blit(menu_img, (0,0))
                startSurf = BIGFONT.render('START', True, WHITE)
                startRect = startSurf.get_rect()
                startRect.topleft = (500, 120)
                screen.blit(startSurf, startRect)

                helpSurf = BIGFONT.render('HELP', True, WHITE)
                helpRect = helpSurf.get_rect()
                helpRect.topleft = (500, 220)
                screen.blit(helpSurf, helpRect)

                optSurf = BIGFONT.render('OPTION', True, WHITE)
                optRect = optSurf.get_rect()
                optRect.topleft = (500, 320)
                screen.blit(optSurf, optRect)

                exitSurf = BIGFONT.render('EXIT', True, WHITE)
                exitRect = exitSurf.get_rect()
                exitRect.topleft = (500, 420)
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
                        if (x > optRect.left and x < optRect.right) and (y > optRect.top and y < optRect.bottom):
                            select_sound.play()
                            status = OPTION
                        if (x > helpRect.left and x < helpRect.right) and (y > helpRect.top and y < helpRect.bottom):
                            select_sound.play()
                            status = HELP
                        if (x > exitRect.left and x < exitRect.right) and (y > exitRect.top and y < exitRect.bottom):
                            select_sound.play()
                            status = EXIT
        elif status == HELP:
            while status == HELP:
                # 绘制背景
                screen.fill(WHITE)
                screen.blit(help_img, (222, 50))
                # 返回菜单
                backSurf = BIGFONT.render('BACK', True, BLACK)
                backRect = startSurf.get_rect()
                backRect.topleft = (45, 490)
                screen.blit(backSurf, backRect)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if (x >= backRect.left and x <= backRect.right) and (y >= backRect.top and y <= backRect.bottom):
                            select_sound.play()
                            status = MENU 
        elif status == OPTION:
            while status == OPTION:
                    screen.fill(WHITE)
        
                    # 返回菜单
                    backSurf = BIGFONT.render('BACK', True, BLACK)
                    backRect = startSurf.get_rect()
                    backRect.topleft = (45, 490)
                    screen.blit(backSurf, backRect)

                    # 声音
                    soundSurf = SFONT.render('JUMP SOUND: ', True, BLACK)
                    soundRect = soundSurf.get_rect()
                    soundRect.topleft = (50, 180)
                    screen.blit(soundSurf, soundRect)
            
                    if sound == True:
                        onSurf = SFONT.render('ON', True, BLACK)
                        onRect = onSurf.get_rect()
                        onRect.topleft = (425, 180)
                        screen.blit(onSurf, onRect)
                    else:
                        offSurf = SFONT.render('OFF', True, BLACK)
                        offRect = offSurf.get_rect()
                        offRect.topleft = (425, 180)
                        screen.blit(offSurf, offRect)

                    # 难度
                    difficultySurf = SFONT.render('DIFFICULTY: ', True, BLACK)
                    difficultyRect = soundSurf.get_rect()
                    difficultyRect.topleft = (50, 260)
                    screen.blit(difficultySurf, difficultyRect)

                    if difficulty == NORMAL:
                        screen.blit(off_img, (600, 50))
                        normalSurf = SFONT.render('NORMAL', True, BLACK)
                        normalRect = normalSurf.get_rect()
                        normalRect.topleft = (405, 260)
                        screen.blit(normalSurf, normalRect)
                    else:
                        screen.blit(on_img, (600, 50))
                        hardSurf = SFONT.render('HARD', True, BLACK)
                        hardRect = hardSurf.get_rect()
                        hardRect.topleft = (405, 260)
                        screen.blit(hardSurf, hardRect)

            
                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            x, y = event.pos
                            if sound == True and (x >= onRect.left and x <= onRect.right) and (y >= onRect.top and y <= onRect.bottom):
                                select_sound.play()
                                sound = False                      
                            elif sound == False and (x >= offRect.left and x <= offRect.right) and (y >= offRect.top and y <= offRect.bottom):
                                select_sound.play()
                                sound = True
                            elif difficulty == NORMAL and (x >= normalRect.left and x <= normalRect.right) and (y >= normalRect.top and y <= normalRect.bottom):
                                select_sound.play()
                                difficulty = HARD
                            elif difficulty == HARD and (x >= hardRect.left and x <= hardRect.right) and (y >= hardRect.top and y <= hardRect.bottom):
                                select_sound.play()
                                difficulty = NORMAL
                            elif (x >= backRect.left and x <= backRect.right) and (y >= backRect.top and y <= backRect.bottom):
                                select_sound.play()
                                status = MENU
        elif status == EXIT:
            pygame.quit()
            exit()

# 过渡画面
def Transition():
    menu_sound.stop()
    per_sound.play()
    screen.fill(WHITE)
    screen.blit(per,(381, 90))
    pygame.display.update()
    # 持续时间（笨办法）
    sp = 0
    while sp < 11000000:
        sp += 1

# 跳跃音效
def PlaySound():
    if sound == True:
        jump_sound.play()

# 绘制背景
def DrawBK():
    screen.blit(bk, (x1, 0))
    screen.blit(bk1, (x2, 0))

# 绘制信息
def DrawInfo():
    # 等级
    levelSurf = BASICFONT.render('Level '+ str(level//8 + 1), True, BLACK)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (40, 26)
    screen.blit(levelSurf, levelRect)
    
    # 距离
    disSurf = BASICFONT.render(' Distance: '+ str(distance), True, BLACK)
    disRect = disSurf.get_rect()
    disRect.topleft = (40+levelRect.right - levelRect.left+10, 26)
    screen.blit(disSurf, disRect)
    
    mSurf = BASICFONT.render('m', True, BLACK)
    mRect = mSurf.get_rect()
    mRect.topleft = (40+levelRect.right - levelRect.left+disRect.right - disRect.left+15, 26)
    screen.blit(mSurf, mRect)

    # 金币
    screen.blit(money_img,(40, 70))
    qbSurf = BASICFONT.render(str(money), True, BLACK)
    qbRect = levelSurf.get_rect()
    qbRect.topleft = (80, 70)
    screen.blit(qbSurf, qbRect)

# 初始化
def Init():
    global player, enemies
    global level, distance, money
    global bk, bk1, rect, width, x1, x2

    player.status = RUN

    for enemy in enemies:
        enemy.recover()
        enemies.remove(enemy)

    level = 1
    distance = 0
    money = 0

    bk = background
    bk1 = background
    rect = bk.get_rect()
    width = rect.right - rect.left
    x1 = 0
    x2 = width

# 游戏循环
def Game():
    global running, player, enemies
    global level, distance, money
    global bk, bk1, rect, width, x1, x2

    # 初始化
    Init()

    # 背景循环信息    
    loop = 0

    # 玩家信息
    flag = False
    flag2 = False
    flip = 0
    move_y = 0

    per_sound.stop()
    pygame.mixer.music.play(-1, 0.0)
    i = random.randint(0, 7)
    enem[i].setpos(SCREEN_WIDTH+800, SCREEN_HEIGHT-50-130)
    enemies.add(enem[i])

    while running:
        clock.tick(FPS)
        ticks = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    if flag == False:
                        PlaySound()
                        player.status = JUMP
                        move_y = -20
                        flag = True
                        flip = 0 
         # 距离增加
        distance += 1
        if distance % 100 == 0:
            level += 1

        # 滚动背景
        x1 -= (4 + level/difficulty)
        x2 -= (4 + level/difficulty)
        if x1 <= -width:
            x1 = width
            loop += 1
            if loop > 15:
                bk = background1
                rect = bk.get_rect()
                width = rect.right - rect.left
        if x2 <= -width:
            x2 = width
            loop += 1
            if loop > 15:
                bk1 = background1
                rect = bk.get_rect()
                width = rect.right - rect.left

        # 玩家跳跃
        if flag == True:
            flip += 1
            if flip > 12:
                move_y = 0
                flag2 = True
        player.action[player.status].move(0, move_y)
        if flag2:
            player.action[player.status].move(0, 10+level/difficulty)
            if player.action[player.status].rect.bottom >= 550:
                flag2 = False
                flag = False
                player.status = RUN

        # 是否有敌人
        flag_enemy = False
        for enemy in enemies:
            flag_enemy = True
        if flag_enemy == False:
            i = random.randint(0, 10)       
            if enem[i].type == MONEY:
                j = random.randint(1, 3)
                if j == 1:
                    if enem[i] == QB1:
                        enemies.add(QB1, QB2, QB3, QB4)
                    elif enem[i] == QB5:
                        enemies.add(QB5, QB6, QB7, QB8)
                    elif enem[i] == QB9:
                        enemies.add(QB9, QB10, QB11, QB12)
                elif j == 2:
                    if enem[i] == QB1 or enem[i] == QB5:
                        enemies.add(QB1, QB2, QB3, QB4, QB5, QB6, QB7, QB8)
                    elif enem[i] == QB9:
                        enemies.add(QB9, QB10, QB11, QB12, QB5, QB6, QB7, QB8)
                elif j == 3:
                        enemies.add(QB1, QB2, QB3, QB4, QB5, QB6, QB7, QB8, QB9, QB10, QB11, QB12)
            else:
                enemies.add(enem[i])

        # 敌人移动
        for enemy in enemies:
            if enemy.rect.right < 0:
                enemy.recover()
                enemies.remove(enemy)
            else:
                enemy.move(-(7.5+level/difficulty), 0)

        # 跳过敌人
        for enemy in enemies:
            if enemy.type == MONEY:
                if pygame.sprite.collide_rect_ratio(0.86)(enemy, player.action[player.status]):
                    money_sound.play()
                    money += 1
                    enemy.recover()
                    enemies.remove(enemy)
            else:
                if player.status == RUN:
                    if pygame.sprite.collide_rect_ratio(0.84)(enemy, player.action[RUN]):
                        running = False
                elif player.status == JUMP:
                    if pygame.sprite.collide_rect_ratio(0.67)(enemy, player.action[JUMP]):
                        running = False

        # 绘制背景
        DrawBK()
             
        # 绘制敌人
        for enemy in enemies:
            enemy.update(ticks)
        enemies.draw(screen)

        # 绘制玩家
        player.Action(ticks, screen)
    
        # 绘制信息
        DrawInfo()

        # 更新屏幕
        pygame.display.update()

# 结束选项
def Again():
    global running
    screen.blit(over, (400, 120))

    sSurf = BASICFONT.render('YES', True, BLACK)
    sRect = sSurf.get_rect()
    sRect.topleft = (435, 233)
    screen.blit(sSurf, sRect)

    yesSurf = BASICFONT.render('OK', True, BLACK)
    yesRect = yesSurf.get_rect()
    yesRect.topleft = (545, 233)
    screen.blit(yesSurf, yesRect)

    # 更新屏幕
    pygame.display.update()

    while running == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (x > sRect.left and x < sRect.right) and (y > sRect.top and y < sRect.bottom):
                    running = True
                if (x > yesRect.left and x < yesRect.right) and (y > yesRect.top and y < yesRect.bottom):
                    running = True

# 结束画面
def Over():
    pygame.mixer.music.stop()
    game_over_sound.play()
    clock.tick(FPS)

    # 绘制背景
    DrawBK()

    # 绘制敌人
    enemies.draw(screen)
    
    # 绘制玩家
    screen.blit(player.action[player.status].image, player.action[player.status].rect)
    screen.blit(end, (player.action[player.status].rect.left+20,player.action[player.status].rect.top))

    # 绘制信息
    DrawInfo()

    # 更新屏幕
    pygame.display.update()

    # 是否再来
    Again()

# 主函数
def main():
    global screen, status
    StartScreen()
    while running:
        Transition()
        Game()
        Over()

if __name__ == '__main__':  
    main() 