import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
	# 初始化pygame、设置和屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))

	pygame.display.set_caption('Alien Invasion')

	#创建一艘飞船
	ship = Ship(ai_settings, screen)

	#创建一个子弹的编组和外星人编组
	bullets = Group()
	aliens = Group()

	#创建一个外星人
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# 创建一个用于存储游戏统计的信息实例
	stats = GameStats(ai_settings)

	play_button = Button(ai_settings, screen, "Play")

	# 创建存储游戏统计信息的实例， 并创建记分牌
	sb = Scoreboard(ai_settings, screen, stats)


	#开始游戏的主循环
	while True:

		#监视键盘和鼠标事件
		gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			bullets.update()
			#更新子弹位置，删除已消失的子弹
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		#for bullet in bullets.copy():
		#	if bullet.rect.bottom <= 0:
		#		bullets.remove(bullet)

		# 让最近绘制的屏幕可见
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()