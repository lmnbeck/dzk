
import pygame
import math
import sys
from pygame.locals import *
from random import *

class Ball(pygame.sprite.Sprite):
	def __init__(self, image, position, bg_size):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = position
		self.width, self.height = bg_size[0], bg_size[1]

	def move(self,speed,direct):
		
		# 撞墙反弹
		if self.rect.left < 0 or self.rect.right > self.width:
			speed = (-speed[0],speed[1])
		if self.rect.top < 0:
			speed = (speed[0],-speed[1])
		# if self.rect.top < 0:
		# 	speed = (speed[0],-speed[1])

		# 撞物反弹
		if direct == 1:	#上
			speed = (speed[0], -speed[1])
		if direct == 2:	#下
			speed = (speed[0], -speed[1])
		if direct == 3:	#左
			speed = (-speed[0], speed[1])
		if direct == 4:	#右
			speed = (-speed[0], speed[1])


		self.rect = self.rect.move(speed)

		return speed


	def collide(self):
		pass

	def getImage(self):
		return self.image
	def getPosition(self):
		return (self.rect.top, self.rect.bottom, self.rect.left, self.rect.right)
	def getLeftTop(self):
		return (self.rect.left, self.rect.top)

class ZK(pygame.sprite.Sprite):
	"""docstring for zk"""
	def __init__(self, image, position, bg_size):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = position
		self.width, self.height = bg_size[0], bg_size[1]
		self.visable = True
	def collide(self):
		pass

	def getImage(self):
		return self.image
	def getPosition(self):
		return (self.rect.top, self.rect.bottom, self.rect.left, self.rect.right)
	def getLeftTop(self):
		return (self.rect.left, self.rect.top)
	def setVisable(self, visableFlag):
		self.visable = visableFlag
	def getVisable(self):
		return self.visable

class Stick(pygame.sprite.Sprite):
	"""docstring for zk"""
	def __init__(self, image, position, bg_size):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = position
		self.width, self.height = bg_size[0], bg_size[1]
		
	def move(self, speed):
		# 撞墙停止
		if self.rect.left < 0:
			self.rect.left = 0
			speed = (0,speed[1])
		if self.rect.right > self.width:
			self.rect.right = self.width
			speed = (0,speed[1])
		self.rect = self.rect.move(speed)
		return speed

	def collide(self):
		pass

	def getImage(self):
		return self.image
	def getPosition(self):
		return (self.rect.top, self.rect.bottom, self.rect.left, self.rect.right)
	def getLeftTop(self):
		return (self.rect.left, self.rect.top)
