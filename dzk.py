#!/usr/bin/env python
# -*- coding:utf-8 -*-

from zk import *
from funcs import *
import pygame
from pygame.locals import *
import sys
import random

SCREEN_WIDTH = 960
SCREEN_HIGHT = 600
ZK_WIDTH = 80
ZK_HIGHT = 26
background_image = 'image/bg.jpg'
stick_image = 'image/brownStick.png'
ball_image = 'image/ball.png'
bluezk_image = 'image/blueZK.png'
pinkzk_image = 'image/pinkZK.png'
yellowzk_image = 'image/yellowZK.png'
bullet_image = 'image/bullet.png'

# 初始化pygame，为使用硬件做准备
pygame.init()
# 创建了一个窗口
bg_size = (SCREEN_WIDTH,SCREEN_HIGHT)
screen = pygame.display.set_mode(bg_size, 0, 32)
# 设置窗口标题
pygame.display.set_caption("Happy 7c")

# 刷新频率
fpsClock = pygame.time.Clock()
FPS = 60
# shot event
SHOOTING_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SHOOTING_EVENT, 500)

# 加载并转换图像
background = pygame.image.load(background_image).convert()

# Creat objects
ball_speed = [0,0]
ball = Ball(ball_image,(SCREEN_WIDTH/2,SCREEN_HIGHT-40-30),bg_size)
stick = Stick(4,stick_image,(SCREEN_WIDTH/2,SCREEN_HIGHT-40),bg_size)

# 很多砖
zkGroup = pygame.sprite.Group()
# zkGroup = ZKGroup()
j = 0
for i in range(0,24):
    zkColor = random.randint(1,3)
    j = i//(SCREEN_WIDTH//ZK_WIDTH)
    i = i%(SCREEN_WIDTH//ZK_WIDTH)
    # print('j=',j)
    # print('i=',i)
    if 1 == zkColor:
        bluezk = ZK(bluezk_image,(i*ZK_WIDTH,j*ZK_HIGHT),bg_size)
        zkGroup.add(bluezk)
    elif 2 == zkColor:
        pinkzk = ZK(pinkzk_image,(i*ZK_WIDTH,j*ZK_HIGHT),bg_size)
        zkGroup.add(pinkzk)
    elif 3 == zkColor:
        yellowzk = ZK(yellowzk_image,(i*ZK_WIDTH,j*ZK_HIGHT),bg_size)
        zkGroup.add(yellowzk)


# 方向
direct_x = (0,0)
Colide_direct = 1
keyPressed = False
ballShooted = False
ballPaused = False
bulletShot = False
canShot = False

# 杆
stickType = 0
# Groups
pill_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:  # 接收到退出事件后退出程序
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            keyPressed = True

            if(event.key == K_LEFT or event.key == K_a):
                direct_x = (-1,0)
            if(event.key == K_RIGHT or event.key == K_d):
                direct_x = (1,0)
            if(event.key == K_SPACE) and (ballShooted == False or ballPaused == True):
                ballShooted = True
                ballPaused = False
                ball_speed = [random.randint(-3,3),-3]
                
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == KEYUP:
            keyPressed = False
            direct_x = (0,0)
        if event.type == SHOOTING_EVENT:
            canShot = True

        if pygame.key.get_pressed()[K_j]:
            bulletShot = True



    # Draw background
    screen.blit(background, (0, 0))

    # 杆加速
    if keyPressed == True:
        if direct_x[0] > 0:
            direct_x = (direct_x[0]+1,0)
        elif direct_x[0] < 0:
            direct_x = (direct_x[0]-1,0)

    if bulletShot == True and stick.getStickType() == 0 and canShot == True:
        bulletShot = False
        canShot = False
        bullet = Bullet(bullet_image, (stick.getLeftTop()[0]+50, stick.getLeftTop()[1]), bg_size)
        bullet_group.add(bullet)
        
    if bullet_group.sprites():
        for each in bullet_group:
            each.move()
            if each.getLeftTop()[1] < 0:
                bullet_group.remove(each)

            else:
                pygame.sprite.spritecollide(each, zkGroup, True)
                screen.blit(each.getImage(), each.getLeftTop())


    # 球设定
    Colide_direct = 0

    # 碰撞检测
    # 碰砖
    for each in zkGroup:
        if pygame.sprite.collide_mask(ball, each):
            # print("peng zhao le!!!")
            Colide_direct = collideDirectionJudge(ball, each)
            zkGroup.remove(each)

            # airbornSupply
            supplyType = random.randint(0,6)
            # supplyType = 2
            if supplyType == 0:
                pill_image = 'image/redPill.png'
            elif supplyType == 1:
                pill_image = 'image/bluePill.png'
            elif supplyType == 2:
                pill_image = 'image/greenPill.png'
            else:
                pass
            # print('supplyType= ',supplyType)
            if supplyType <=2:
                DropPill = Pills(supplyType, pill_image, each.getLeftTop(), bg_size)
                pill_group.add(DropPill)

    # pill move and hit stick
    for each in pill_group:
        each.move()
        if each.getLeftTop()[1] >= SCREEN_HIGHT:
            pill_group.remove(each)
        # pill hit stick
        if pygame.sprite.collide_mask(each, stick):
            if each.getPillType() == 0:
                stick_image = 'image/redStick.png'
            elif each.getPillType() == 1:
                stick_image = 'image/blueStick.png'
            elif each.getPillType() == 2:
                stick_image = 'image/greenStick.png'
            else:
                pass
            # stick.setImage(stick_image)
            # stick.setStickType(each.getPillType())
            stick = Stick(each.getPillType(),stick_image,stick.getLeftTop(),bg_size)
            pill_group.remove(each)
            
    # 杆移动
    direct_x = stick.move(direct_x)
    if ballShooted == False:
        ball_speed = direct_x

    # 球碰杆
    if ballPaused == False: 
        if pygame.sprite.collide_mask(ball, stick):
            Colide_direct = collideDirectionJudge(ball, stick)
            # 用杆加速
            # print("ball_speed", ball_speed)
            # print("direct_x", direct_x)
            if (ball_speed[0] + direct_x[0]) > 10:
                ball_speed = (10,ball_speed[1])
            elif (ball_speed[0] + direct_x[0]) < -10:
                ball_speed = (-10,ball_speed[1])
            else:
                ball_speed = (ball_speed[0] + direct_x[0],ball_speed[1])
            # green stick can hold the ball
            if stick.getStickType() == 2 and ballShooted == True and ballPaused == False:
                ballPaused = True  
    else:
        ball_speed = direct_x

    ball_speed = ball.move(ball_speed, Colide_direct)

    # End Game
    if zkGroup.sprites():
        if (ball.getPosition()[0] > SCREEN_HIGHT):
            # ball.setLeftTop((stick.getLeftTop()[0], stick.getLeftTop()[1]-30))
            # ballShooted = False
            # ball_speed = direct_x

            # Game over
            myFont = pygame.font.SysFont('simhei',116)
            textSurface = myFont.render('哈哈哈！', True, (0,0,0))
            screen.blit(textSurface, (SCREEN_WIDTH/2-116*2, SCREEN_HIGHT/2-116))
            # 刷新画面
            pygame.display.update()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()
    else:
        # win the game
        myFont = pygame.font.SysFont('simhei',116)
        textSurface = myFont.render('爱你呦！', True, (0,0,0))
        screen.blit(textSurface, (SCREEN_WIDTH/2-116*1.5, SCREEN_HIGHT/2))

    # Draw
    screen.blit(stick.getImage(), stick.getLeftTop())
    screen.blit(ball.getImage(), ball.getLeftTop())
    for each in pill_group:
        screen.blit(each.getImage(), each.getLeftTop())
    for each in zkGroup:
        screen.blit(each.getImage(), each.getLeftTop())

    # 刷新画面
    pygame.display.update()

    fpsClock.tick(FPS)


