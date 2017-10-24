class Settings():
	"""存储《外星人入侵》的所有设置的类"""
	def __init__(self):
		"""初始化设置"""
		#界面的长宽
		self.screen_width = 1200
		self.screen_height = 800
		#界面的底色
		self.bg_color = (230, 230, 230)
		# 飞船移动的步长单位是像素
		self.ship_speed_factor = 1.5
		#子弹设置
		self.bullet_speed_factor = 1.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
