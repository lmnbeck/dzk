#!/usr/bin/env python
# -*- coding:utf-8 -*-

from zk import *
from funcs import *
import pygame
from pygame.locals import *
import sys
import random

SCREEN_WIDTH = 480
SCREEN_HIGHT = 600
ZK_WIDTH = 80
ZK_HIGHT = 26
background_image = 'image/bg.jpg'
stick_image = 'image/head.jpg'
ball_image = 'image/ball.png'
bluezk_image = 'image/blueZK.png'
pinkzk_image = 'image/pinkZK.png'
yellowzk_image = 'image/yellowZK.png'

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

# 加载并转换图像
background = pygame.image.load(background_image).convert()

# 球和杆
ball_speed = [0,0]
ball = Ball(ball_image,(140,360),bg_size)
stick = Stick(stick_image,(140,400),bg_size)
# 很多砖
zkGroup = pygame.sprite.Group()
j = 0
for i in range(0,12):
    zkColor = random.randint(1,3)
    j = i//(SCREEN_WIDTH//ZK_WIDTH)
    i = i%(SCREEN_WIDTH//ZK_WIDTH)
    print('j=',j)
    print('i=',i)
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

# 杆坐标
stick_x = screen.get_rect().centerx - stick.getImage().get_rect().width/2
stick_y = screen.get_rect().bottom - stick.getImage().get_rect().height
print(stick_x,stick_y)
stick_width = stick.getImage().get_rect().width

while True:
    for event in pygame.event.get():
        if event.type == QUIT:  # 接收到退出事件后退出程序
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            keyPressed = True
            # if(event.key == K_UP or event.key == K_w):
            #     direct_y = -1
            # if(event.key == K_DOWN or event.key == K_s):
            #     direct_y = 1
            if(event.key == K_LEFT or event.key == K_a):
                direct_x = (-1,0)
            if(event.key == K_RIGHT or event.key == K_d):
                direct_x = (1,0)
            if(event.key == K_SPACE) and (ball_speed[0] == 0):
                ball_speed = [random.randint(-3,3),-3]
                
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == KEYUP:
            keyPressed = False
            direct_x = (0,0)
    # 杆加速
    if keyPressed == True:
        if direct_x[0] > 0:
            direct_x = (direct_x[0]+1,0)
        elif direct_x[0] < 0:
            direct_x = (direct_x[0]-1,0)

    # 杆移动
    direct_x = stick.move(direct_x)

    # 球设定
    Colide_direct = 0

    # 碰撞检测
    # 碰砖
    for each in zkGroup:
        if pygame.sprite.collide_mask(ball, each):
            print("peng zhao le!!!")
            Colide_direct = collideDirectionJudge(ball, each)
            zkGroup.remove(each)

    # 碰杆
    if pygame.sprite.collide_mask(ball, stick):
        Colide_direct = collideDirectionJudge(ball, stick)
        # 用杆加速
        print("ball_speed", ball_speed)
        print("direct_x", direct_x)
        if (ball_speed[0] + direct_x[0]) > 10:
            ball_speed = (10,ball_speed[1])
        elif (ball_speed[0] + direct_x[0]) < -10:
            ball_speed = (-10,ball_speed[1])
        else:
            ball_speed = (ball_speed[0] + direct_x[0],ball_speed[1])
        print("after ball_speed", ball_speed)
        print("after direct_x", direct_x)

    ball_speed = ball.move(ball_speed,Colide_direct)

    # Game over
    if zkGroup.sprites():
        pass
    else:
        # win the game
        pass


    # Draw
    screen.blit(background, (0, 0))
    screen.blit(stick.getImage(), stick.getLeftTop())
    screen.blit(ball.getImage(), ball.getLeftTop())
    for each in zkGroup:
        screen.blit(each.getImage(), each.getLeftTop())

    # 刷新画面
    pygame.display.update()

    fpsClock.tick(FPS)


