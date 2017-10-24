import sys
import pygame
from bullet import Bullet
def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		#创建一个颗子弹，并将其加入到编组bullets中
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)


def check_keyup_events(event, ship):
	"""响应松开"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False
#上面两个函数中响应键盘方向键的对应为pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygam.K_RIGHT
#注意大写
def check_events(ai_settings, screen, ship, bullets):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship , bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)


#此函数功能是你是否按了某个键，如上面的pygam.KEYDOWN就是按下了键pygame.UP就是键弹上来。
def update_screen(ai_settings, screen, ship, bullets):
	"""更新屏幕上的图像，并切换到新屏幕"""
	#每次循环时都重绘屏幕
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	# 在飞船和外星人后面所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	#让最近绘制的屏幕可见
	pygame.display.flip()


