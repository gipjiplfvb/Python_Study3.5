import pygame
class Ship():
	def __init__(self, ai_settings, screen):
		"""初始化飞船并设置其初始位置"""
		self.screen = screen
		self.ai_settings = ai_settings

		#加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		#get_rect()获取图像的尺寸
		self.screen_rect = screen.get_rect()
		#获取界面的尺寸
		# 将每艘飞船放到屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
			#rect.centerx 图像的X轴    screen_rect.centerx 界面的X轴
		self.rect.bottom = self.screen_rect.bottom
			#使图片的低部和界面低部对齐
		#self.rect.centery = self.screen_rect.centery
			#可以全图片和界面的Y重对齐

		# 在飞船的属性center中存储小数值
		self.center_1 = float(self.rect.centerx)
		self.center_2 = float(self.rect.centery)


		#移动标示
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False


	#def test(self):
	#	print (self.rect)



	def update(self):
		"""根据移动标志调整飞船的位置"""
		# 更新飞船的center值，而不是rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			#rect.right 图像的最右边  screen_rect.right   界面的最右边
			self.center_1 += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			# rect.left 同上图像的最左边， 0是界面的起始点在左上角0.0开始，到1200.800
			self.center_1 -= self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top >0:
			self.center_2 -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.center_2 += self.ai_settings.ship_speed_factor

		# 根据self.center更新rect对象
		self.rect.centerx = self.center_1
		self.rect.centery = self.center_2


	def blitme(self):
		"""指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)
	def center_ship(self):
		"""让飞船在屏幕上居中"""
		self.center = self.screen_rect.centerx
