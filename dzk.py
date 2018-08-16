#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
import sys

background_image = 'image/bg.jpg'
stick_image = 'image/head.jpg'

# 初始化pygame，为使用硬件做准备
pygame.init()
# 创建了一个窗口
screen = pygame.display.set_mode((480, 600), 0, 32)
# 设置窗口标题
pygame.display.set_caption("Happy 7c")

# 刷新频率
fpsClock = pygame.time.Clock()
FPS = 30

# 加载并转换图像
background = pygame.image.load(background_image).convert()
stick_cursor = pygame.image.load(stick_image).convert_alpha()

# 方向
direct_x = 0
direct_y = 0
keyPressed = False

# 杆坐标
stick_x = screen.get_rect().centerx - stick_cursor.get_rect().width/2
stick_y = screen.get_rect().bottom - stick_cursor.get_rect().height
print(stick_x,stick_y)

stick_width = stick_cursor.get_rect().width


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
                direct_x = -1
            if(event.key == K_RIGHT or event.key == K_d):
                direct_x = 1
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == KEYUP:
            keyPressed = False
            direct_x = 0
            direct_y = 0
    
    if keyPressed == True:
        if direct_x > 0:
            direct_x += 1
        elif direct_x < 0:
            direct_x -= 1
        stick_x += direct_x
        stick_y += direct_y

    if stick_x <= 0:
        stick_x = 0
    elif stick_x > screen.get_width() - stick_cursor.get_rect().width:
        stick_x = screen.get_width()- stick_cursor.get_rect().width
    if stick_y <= 0:
        stick_y = 0
    elif stick_y > screen.get_height():
        stick_y = screen.get_height()
    screen.blit(background, (0, 0))  # 画上背景图

    # direct_x, direct_y = pygame.mouse.get_pos()  # 获得鼠标位置
    # # 计算光标左上角位置
    # direct_x -= stick_cursor.get_width()/2
    # direct_y -= stick_cursor.get_height()/2

    # 画上光标
    screen.blit(stick_cursor, (stick_x, stick_y))

    # 刷新画面
    pygame.display.update()

    fpsClock.tick(FPS)