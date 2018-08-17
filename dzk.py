#!/usr/bin/env python
# -*- coding:utf-8 -*-

from zk import *
import pygame
from pygame.locals import *
import sys
import random

background_image = 'image/bg.jpg'
stick_image = 'image/head.jpg'
ball_image = 'image/ball.png'
bluezk_image = 'image/blueZK.png'

# 初始化pygame，为使用硬件做准备
pygame.init()
# 创建了一个窗口
bg_size = (480,600)
screen = pygame.display.set_mode(bg_size, 0, 32)
# 设置窗口标题
pygame.display.set_caption("Happy 7c")

# 刷新频率
fpsClock = pygame.time.Clock()
FPS = 60

# 加载并转换图像
background = pygame.image.load(background_image).convert()

# 球砖杆
ball_speed = [0,0]
ball = Ball(ball_image,(140,360),bg_size)
bluezk = ZK(bluezk_image,(100,100),bg_size)
stick = Stick(stick_image,(140,400),bg_size)

# 方向
direct_x = (0,0)
Colide_direct = 1
keyPressed = False

# 杆坐标
stick_x = screen.get_rect().centerx - stick.getImage().get_rect().width/2
stick_y = screen.get_rect().bottom - stick.getImage().get_rect().height
print(stick_x,stick_y)
stick_width = stick.getImage().get_rect().width

zkGroup = pygame.sprite.Group()
zkGroup.add(bluezk)

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
                direct_x = (-3,0)
            if(event.key == K_RIGHT or event.key == K_d):
                direct_x = (3,0)
            if(event.key == K_SPACE):
                ball_speed = [random.choice([-3,3]),-3]
                
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == KEYUP:
            keyPressed = False
            direct_x = (0,0)
    # 杆加速
    # if keyPressed == True:
    #     if direct_x[0] > 0:
    #         direct_x = (direct_x[0]+1,0)
    #     elif direct_x[0] < 0:
    #         direct_x = (direct_x[0]-1,0)

    # 杆移动
    stick.move(direct_x)

    # 球设定
    Colide_direct = 0
    #ball_speed = ball.move(ball_speed,0)

    # 碰撞检测
    # 碰砖
    for each in zkGroup:
        if pygame.sprite.collide_mask(ball, bluezk):
            print("peng zhao le!!!")
            bluezk.setVisable(False)
            Colide_direct = 1
            zkGroup.remove(each)
            # if zkGroup.sprites():
            #     # continue
            # else:
            #     # win the game
    # 碰杆
    if pygame.sprite.collide_mask(ball, stick):
        Colide_direct = 2

    ball_speed = ball.move(ball_speed,Colide_direct)

    screen.blit(background, (0, 0))  # 画上背景图

    # direct_x, direct_y = pygame.mouse.get_pos()  # 获得鼠标位置
    # # 计算光标左上角位置
    # direct_x -= stick.getImage().get_width()/2
    # direct_y -= stick.getImage().get_height()/2

    # 画上光标
    screen.blit(stick.getImage(), stick.getPosition())
    screen.blit(ball.getImage(), ball.getPosition())
    if bluezk.getVisable():
        screen.blit(bluezk.getImage(), bluezk.getPosition())



    # 刷新画面
    pygame.display.update()

    fpsClock.tick(FPS)