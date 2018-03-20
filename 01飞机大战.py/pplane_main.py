#主程序
import pygame
from pplane_sprites import *

#子弹的
ZIDAN_DE = pygame.USEREVENT+1

#主程序类
class PlaneGame(object):
	#初始化
	def __init__(self):
		#游戏窗口
		self.screen = pygame.display.set_mode((SCEREN_RECT.width,SCEREN_RECT.height))
		#游戏标题
		pygame.display.set_caption('小蜜蜂')
		#创建游戏时钟
		self.clock = pygame.time.Clock()
		#创建精灵和精灵组
		self.__cretar_sprite()
		pygame.time.set_timer(DIJI_BA,800)
		pygame.time.set_timer(ZIDAN_DE,500)
		self.life1 = 1
		self.life2 = 1
		self.yinyue = Muisc()
		self.guanting = 0
		# 分数
		self.wan_yi = 0
		self.wan_er = 0
	#游戏开始
	def start_game(self):
		print('游戏开始') 
		while True:
			self.clock.tick(60)
			#监听事件
			self.__event_handler()
			#碰撞检测   
			self.__check_collide()
			#精灵组更新绘制
			self.__update_sprites()
			self.__print_score()
			#刷新
			pygame.display.update()
	#精灵精灵组
	def __cretar_sprite(self):
		bg1 = Background('./sdssmeitu_1_meitu_3.png')
		bg2 = Background('./sdssmeitu_1_meitu_3.png')
		bg2.rect.x = bg2.rect.width
		self.back_group = pygame.sprite.Group(bg1,bg2)
		self.hero = Hero('./fhfVE1`A.png')
		self.hero_group = pygame.sprite.Group(self.hero)
		self.hero1 = Hero1('./images/me1.png')
		self.hero1_group = pygame.sprite.Group(self.hero1)
		self.enemy = Enemy('./images/sdssmeitu_1_meitu_3.png')
		self.enemy_group = pygame.sprite.Group(self.enemy)
		self.hero2 = Hero2('./images/life.png')
		self.hero2_group = pygame.sprite.Group(self.hero2)
		self.hero3 = Hero3('./images/life.png')
		self.hero3_group = pygame.sprite.Group(self.hero3)
	# #事件监听
	def __event_handler(self):
		
		for event in pygame.event.get():
			print(event)

			if event.type == pygame.QUIT:
				self.__game_over()

			elif event.type == DIJI_BA:
				self.enemy_group.add(Enemy('./images/sdssmeitu_1_meitu_3.png'))

			elif event.type == ZIDAN_DE:
				self.hero.fort()
				self.hero2.fort()
				self.hero3.fort()
				self.hero1.fort()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.hero.panduan1 = True
					# self.hero2.panduan5 = True
					# self.hero3.panduana = True
				elif event.key == pygame.K_DOWN:
					self.hero.panduan2 = True
					self.hero2.panduan6 = True
					self.hero3.panduanb = True
				elif event.key == pygame.K_LEFT:
					self.hero.panduan3 = True
					self.hero2.panduan7 = True
					self.hero3.panduanc = True
				elif event.key == pygame.K_RIGHT:
					self.hero.panduan4 = True
					self.hero2.panduan8 = True
					self.hero3.panduand = True
				elif event.key == pygame.K_w:
					self.hero1.panduan01 = True
				elif event.key == pygame.K_s:
					self.hero1.panduan02 = True
				elif event.key == pygame.K_a:
					self.hero1.panduan03 = True
				elif event.key == pygame.K_d:
					self.hero1.panduan04 = True
				#音乐控制
				elif event.key == pygame.K_SPACE:
					self.guanting+=1
					if self.guanting%2 == 0:
						self.yinyue.pausea()
					else:
						self.yinyue.stopa()

			elif event.type ==pygame.KEYUP:
				if event.key == pygame.K_UP:
					self.hero.panduan1 = False
					self.hero2.panduan5 = False
					self.hero3.panduana = False
				elif event.key == pygame.K_DOWN:
					self.hero.panduan2 =False
					self.hero2.panduan6 = False
					self.hero3.panduanb =False
				elif event.key == pygame.K_LEFT:
					self.hero.panduan3 = False
					self.hero2.panduan7 =False
					self.hero3.panduanc =False
				elif event.key == pygame.K_RIGHT:
					self.hero.panduan4 = False
					self.hero2.panduan8 =False
					self.hero3.panduand =False
				elif event.key == pygame.K_w:
					self.hero1.panduan01 = False
				elif event.key == pygame.K_s:
					self.hero1.panduan02 = False
				elif event.key == pygame.K_a:
					self.hero1.panduan03 = False
				elif event.key == pygame.K_d:
					self.hero1.panduan04 = False
		
	#碰撞检测
	def __check_collide(self):
		if pygame.sprite.groupcollide(self.hero.bullte_group,self.enemy_group,True,True):
			self.wan_yi+=1
		
		elif pygame.sprite.groupcollide(self.hero2.bulltea_group,self.enemy_group,True,True):
			self.wan_yi+=1
		
		elif pygame.sprite.groupcollide(self.hero3.bulltes_group,self.enemy_group,True,True):
			self.wan_yi+=1
		
		elif pygame.sprite.groupcollide(self.hero1.bullte1_group,self.enemy_group,True,True):
			self.wan_er+=1
		eneims = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		eneime = pygame.sprite.spritecollide(self.hero2,self.enemy_group,True)
		eneima = pygame.sprite.spritecollide(self.hero3,self.enemy_group,True)
		eneima1 = pygame.sprite.spritecollide(self.hero1,self.enemy_group,True)
		#主机碰撞
		if len(eneims)>0:
			self.hero.kill()
			self.hero2.kill()
			self.hero3.kill()
			self.__game_over()
		#第二个玩家
		elif len(eneima1)>0:
			self.hero1.kill()
			self.hero1.rect.y = -10000

		elif len(eneime)>0:
			self.life1 -= 1
			if self.life1 == 0:
				#主机移动
				self.hero.diaoyong1=False
				self.hero.diaoyong2 = True
				self.hero.diaoyong3 = False
				self.hero.diaoyong4 = False
				#僚机1移动
				self.hero3.liaojiyidong3 = False
				self.hero3.liaojiyidong4 = True
				#僚机2移动
				self.hero2.liaojiyidong1 = False
				self.hero2.liaojiyidong2 = False

				self.hero2.rect.y = -10000
				self.hero2.rect.x = -10000
				self.hero2.kill()
		
		elif len(eneima)>0:
			self.life2 -= 1
			if self.life2 == 0:
				#主机移动
				self.hero.diaoyong1=False
				self.hero.diaoyong2 = False
				self.hero.diaoyong3 = True
				self.hero.diaoyong4 = False
				#僚机1移动
				self.hero2.liaojiyidong1 = False
				self.hero2.liaojiyidong2 = True
				#僚机2移动
				self.hero3.liaojiyidong3 = False
				self.hero3.liaojiyidong4 = False

				self.hero3.rect.y = -10000
				self.hero3.rect.x = -10000
				self.hero3.kill()

		elif self.life2 == 1 and self.life1 == 1:
				#主机移动
				self.hero.diaoyong1=False
				self.hero.diaoyong2 = False
				self.hero.diaoyong3 = False
				self.hero.diaoyong4 = True
				#僚机1移动
				self.hero2.liaojiyidong1 = True
				self.hero2.liaojiyidong2 = False
				#僚机2移动
				self.hero3.liaojiyidong3 = True
				self.hero3.liaojiyidong4 = False
			

		elif self.life2 == 0 and self.life1 == 0:
				#主机移动
				self.hero.diaoyong1=True
				self.hero.diaoyong2 = False
				self.hero.diaoyong3 = False
				self.hero.diaoyong4 = False
				#僚机1移动
				self.hero2.liaojiyidong1 = False
				self.hero2.liaojiyidong2 = False
				#僚机2移动
				self.hero3.liaojiyidong3 = False
				self.hero3.liaojiyidong4 = False
		
	def __print_score(self):
		'''显示分数'''
		pygame.font.init()
		#位置
		pos1 = (200,0)
		pos2 = (600,0)
		#颜色
		color = (0,0,0)
		text1 = 'integral1:'+str(self.wan_yi)
		text2 = 'integral2:'+str(self.wan_er)
		cur_font = pygame.font.SysFont('楷体',30)
		text_font1 = cur_font.render(text1,1,color)
		text_font2 = cur_font.render(text2,1,color)
		self.screen.blit(text_font1,pos1)
		self.screen.blit(text_font2,pos2)	
	#精灵组更新和绘制
	def __update_sprites(self):
		self.back_group.update()
		self.back_group.draw(self.screen)
		self.hero_group.update()
		self.hero_group.draw(self.screen)
		self.hero1_group.update()
		self.hero1_group.draw(self.screen)
		self.hero2_group.update()
		self.hero2_group.draw(self.screen)
		self.hero3_group.update()
		self.hero3_group.draw(self.screen)
		self.enemy_group.update()
		self.enemy_group.draw(self.screen)
		self.hero.bullte_group.update()
		self.hero.bullte_group.draw(self.screen)
		self.hero1.bullte1_group.update()
		self.hero1.bullte1_group.draw(self.screen)
		self.hero2.bulltea_group.update()
		self.hero2.bulltea_group.draw(self.screen)
		self.hero3.bulltes_group.update()
		self.hero3.bulltes_group.draw(self.screen)

		
	#游戏结束
	def __game_over(self):
		print('游戏结束')
		pygame.quit()
		exit()
if __name__  == '__main__':
	game = PlaneGame()
	game.start_game()