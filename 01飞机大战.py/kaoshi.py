import pygame
import random
#设置窗口常量
SCEREN_RECT = pygame.Rect(0,0,1100,550)
DIJI_BA = pygame.USEREVENT

class AnHuaFeng_GameSprite(pygame.sprite.Sprite):
	def __init__(self,image_name,speed = 5):
		super().__init__()
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.x += self.speed
#背景类
class AnHuaFeng_Background(AnHuaFeng_GameSprite):
	def __init__(self,image_name,ai_j=False):
		super().__init__(image_name)
		self.rect.left=0
		if ai_j:
			self.rect.x = -SCEREN_RECT.width


	def update(self):
		super().update()
		if self.rect.x >=  self.rect.width:
			self.rect.x = -self.rect.width

	

#英雄1
class AnHuaFeng_Hero(AnHuaFeng_GameSprite):
	def __init__(self,image_name):
		super().__init__(image_name)
		self.rect.centery = SCEREN_RECT.centery+40
		self.rect.right = SCEREN_RECT.right -20
		self.panduan1 = False
		self.panduan2 =False
		self.panduan3 =False
		self.panduan4 =False
		self.diaoyong1 =False
		self.diaoyong2 = False
		self.diaoyong3 = False
		self.diaoyong4 = False
		self.bullte_group = pygame.sprite.Group()

	def update(self):
		#if self.diaoyong1 == True:
		if self.panduan1 == True and self.rect.y >= 0:
			self.rect.y -= 5
		elif self.panduan2 == True and self.rect.y <= SCEREN_RECT.height-self.rect.height:
			self.rect.y += 5
		elif self.panduan3 == True and self.rect.x >= 0:
			self.rect.x -= 5
		elif self.panduan4 == True and self.rect.x <= SCEREN_RECT.width-self.rect.width:
			self.rect.x += 5

		# elif self.diaoyong2 == True:
		# 	if self.panduan1 == True and self.rect.y >= 0:
		# 		self.rect.y -= 5
		# 	elif self.panduan2 == True and self.rect.bottom <= SCEREN_RECT.height :
		# 		self.rect.y += 5
		# 	elif self.panduan3 == True and self.rect.x >= 0:
		# 		self.rect.x -= 5
		# 	elif self.panduan4 == True and self.rect.x <= SCEREN_RECT.width-self.rect.width:
		# 		self.rect.x += 5

		# elif self.diaoyong3 == True:
		# 	if self.panduan1 == True and self.rect.y >=62 :
		# 		self.rect.y -= 5
		# 	elif self.panduan2 == True and self.rect.y <= SCEREN_RECT.height-self.rect.height:
		# 		self.rect.y += 5
		# 	elif self.panduan3 == True and self.rect.x >= 0:
		# 		self.rect.x -= 5
		# 	elif self.panduan4 == True and self.rect.x <= SCEREN_RECT.width-self.rect.width:
		# 		self.rect.x += 5
				
		# elif self.diaoyong4 == True:
		# 	if self.panduan1 == True and self.rect.y >= 55:
		# 		self.rect.y -= 5
		# 	elif self.panduan2 == True and self.rect.bottom <= 430:
		# 		self.rect.y += 5
		# 	elif self.panduan3 == True and self.rect.x >= 0:
		# 		self.rect.x -= 5
		# 	elif self.panduan4 == True and self.rect.x <= SCEREN_RECT.width-self.rect.width:
		# 		self.rect.x += 5

	def fort(self):
		for i in (1,2,3):
			self.bullte = AnHuaFeng_Bullte('./images/bullet1.png')
			self.bullte.rect.right = self.rect.left - i*20
			self.bullte.rect.centery = self.rect.centery
			self.bullte_group.add(self.bullte)
#英雄1
class AnHuaFeng_Hero1(AnHuaFeng_GameSprite):
	def __init__(self,image_name):
		super().__init__(image_name)
		self.rect.centery = SCEREN_RECT.centery-120
		self.rect.right = SCEREN_RECT.right -20
		self.panduan01 = False
		self.panduan02 =False
		self.panduan03 =False
		self.panduan04 =False

		self.bullte1_group = pygame.sprite.Group()

	def update(self):

		if self.panduan01 == True and self.rect.y >= 0:
			self.rect.y -= 5
		elif self.panduan02 == True and self.rect.y <= SCEREN_RECT.height-self.rect.height:
			self.rect.y += 5
		elif self.panduan03 == True and self.rect.x >= 0:
			self.rect.x -= 5
		elif self.panduan04 == True and self.rect.x <= SCEREN_RECT.width-self.rect.width:
			self.rect.x += 5
	def fort(self):
		for i in (1,2,3):
			self.bullte1 = AnHuaFeng_Bullte('./images/bullet1.png')
			self.bullte1.rect.right = self.rect.left - i*20
			self.bullte1.rect.centery = self.rect.centery
			self.bullte1_group.add(self.bullte1)
#敌机
class AnHuaFeng_Enemy(AnHuaFeng_GameSprite):
	def __init__(self,image_name):
		super().__init__(image_name)
		self.rect.right = 0
		self.speed = random.randint(5,10)
		ma_y = SCEREN_RECT.height-self.rect.height
		self.rect.y = random.randint(0,ma_y)

	def update(self):
		super().update()
		if self.rect.left >=SCEREN_RECT.width:
			self.kill()
#子弹
class AnHuaFeng_Bullte(AnHuaFeng_GameSprite):
	def __init__(self,image_name):
		super().__init__(image_name,-20)

	def update(self):
		super().update()
		if self.rect.left<0: 
			self.kill()
# #僚机1
# class AnHuaFeng_Hero2(AnHuaFeng_GameSprite):
# 	def __init__(self,image_name):
# 		super().__init__(image_name)
# 		self.hero1=AnHuaFeng_Hero('./images/fhfVE1`A.png')
# 		self.rect.centery= self.hero1.rect.centery -90
# 		self.rect.right = SCEREN_RECT.right-10
# 		self.panduan5 = False
# 		self.panduan6 = False
# 		self.panduan7 =False
# 		self.panduan8 =False
# 		self.liaojiyidong1 = False
# 		self.liaojiyidong2 = False
# 		self.bulltea_group = pygame.sprite.Group()

# 	def update(self):
# 		if self.liaojiyidong1 == True:
# 			if self.panduan5 == True and self.rect.y >=0:
# 				self.rect.y -= 5
# 			elif self.panduan6 == True and self.rect.bottom <= 159:
# 				self.rect.y += 5
# 			elif self.panduan7 == True and self.rect.left >= 10:
# 				self.rect.x -= 5
# 			elif self.panduan8 == True and self.rect.right <=621:
# 				self.rect.x += 5

# 		elif self.liaojiyidong2 == True:
# 			if self.panduan5 == True and self.rect.y >=0:
# 				self.rect.y -= 5
# 			elif self.panduan6 == True and self.rect.bottom <= 362:
# 				self.rect.y += 5
# 			elif self.panduan7 == True and self.rect.left >= 10:
# 				self.rect.x -= 5
# 			elif self.panduan8 == True and self.rect.right <=621:
# 				self.rect.x += 5

# 	def fort(self):
# 		for i in (1,2,3):
# 			self.bulltea = AnHuaFeng_Bullte('./images/bullet2.png')
# 			self.bulltea.rect.right = self.rect.left -i*20
# 			self.bulltea.rect.centery = self.rect.centery
# 			self.bulltea_group.add(self.bulltea)
# #僚机2
# class AnHuaFeng_Hero3(AnHuaFeng_GameSprite):
# 	def __init__(self,image_name):
# 		super().__init__(image_name)
# 		self.hero1=AnHuaFeng_Hero('./images/fhfVE1`A.png')
# 		self.rect.centery = self.hero1.rect.centery +90
# 		self.rect.right = SCEREN_RECT.right-10
# 		self.panduana = False
# 		self.panduanb = False
# 		self.panduanc =False
# 		self.panduand =False
# 		self.liaojiyidong3 = False
# 		self.liaojiyidong4 = False
# 		self.bulltes_group = pygame.sprite.Group()

# 	def update(self):
# 		if self.liaojiyidong3 == True:
# 			if self.panduana == True and self.rect.top >= 159:
# 				self.rect.y -= 5
# 			elif self.panduanb == True and self.rect.bottom <= SCEREN_RECT.bottom:
# 				self.rect.y += 5
# 			elif self.panduanc == True and self.rect.left >= 10:
# 				self.rect.x -= 5
# 			elif self.panduand == True and self.rect.right <=621:
# 				self.rect.x += 5

# 		elif self.liaojiyidong4 == True:
# 			if self.panduana == True and self.rect.top >=118:
# 				self.rect.y -= 5
# 			elif self.panduanb == True and self.rect.bottom <= SCEREN_RECT.bottom:
# 				self.rect.y += 5
# 			elif self.panduanc == True and self.rect.left >= 10:
# 				self.rect.x -= 5
# 			elif self.panduand == True and self.rect.right <=621:
# 				self.rect.x += 5

# 	def fort(self):
# 		for i in (1,2,3):
# 			self.bulltes = AnHuaFeng_Bullte('./images/bullet2.png')
# 			self.bulltes.rect.right = self.rect.left - i*40
# 			self.bulltes.rect.centery = self.rect.centery
# 			self.bulltes_group.add(self.bulltes)


class AnHuaFeng_Muisc(object):
	def __init__(self):
		pygame.init()
		pygame.mixer.music.load('儿童歌曲-黑猫警长1(1).mp3')
		pygame.mixer.music.play()
	def stopa(self):

		pygame.mixer.music.pause()	
	def pausea(self):
		pygame.mixer.music.unpause()	
