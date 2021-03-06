
import pygame
import math
import sys
from pygame.locals import *
import random

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

	def getImage(self):
		return self.image
	def getPosition(self):
		return (self.rect.top, self.rect.bottom, self.rect.left, self.rect.right)
	def setLeftTop(self, position):	
		self.rect.left, self.rect.top = position
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
	def __init__(self, stickType, image, position, bg_size):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = position
		self.width, self.height = bg_size[0], bg_size[1]
		self.stickType = stickType
		
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

	def setImage(self, image):
		self.image = pygame.image.load(image).convert_alpha()
		# self.rect = self.image.get_rect()
	def getImage(self):
		return self.image
	def getPosition(self):
		return (self.rect.top, self.rect.bottom, self.rect.left, self.rect.right)
	def getLeftTop(self):
		return (self.rect.left, self.rect.top)
	def setStickType(self,stickType):
		self.stickType = stickType		
	def getStickType(self):
		return self.stickType

class Pills(pygame.sprite.Sprite):
	"""docstring for zk"""
	def __init__(self, pillType, image, position, bg_size):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = position
		self.width, self.height = bg_size[0], bg_size[1]
		self.pillType = pillType
		
	def move(self):
		# 直落
		self.rect = self.rect.move((0,5))
		# return speed

	def getImage(self):
		return self.image
	def getPosition(self):
		return (self.rect.top, self.rect.bottom, self.rect.left, self.rect.right)
	def getLeftTop(self):
		return (self.rect.left, self.rect.top)
	def getPillType(self):
		return self.pillType

class Bullet(pygame.sprite.Sprite):
	"""docstring for bullet"""
	def __init__(self, image, position, bg_size):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = position
		self.width, self.height = bg_size[0], bg_size[1]
		
	def move(self):
		# 直落
		self.rect = self.rect.move((0,-6))
		# return speed

	def getImage(self):
		return self.image
	def getPosition(self):
		return (self.rect.top, self.rect.bottom, self.rect.left, self.rect.right)
	def getLeftTop(self):
		return (self.rect.left, self.rect.top)

# class ZKGroup(pygame.sprite.Group):
# 	"""docstring for ZKGroup"""
# 	def __init__(self):
# 		super(ZKGroup, self).__init__()
	
# 	def remove(self, member):
# 		pygame.sprite.Group.remove(member)

# 		# airbornSupply
# 		supplyType = random.randint(0,6)
# 		# supplyType = 2
# 		if supplyType == 0:
# 			pill_image = 'image/redPill.png'
# 		elif supplyType == 1:
# 			pill_image = 'image/bluePill.png'
# 		elif supplyType == 2:
# 			pill_image = 'image/greenPill.png'
# 		else:
# 			pass
# 		# print('supplyType= ',supplyType)
# 		if supplyType <=2:
# 			DropPill = Pills(supplyType, pill_image, member.getLeftTop(), bg_size)
#         return DropPill
#         #     pill_group.add(DropPill)

		