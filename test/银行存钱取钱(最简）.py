def atm_2():
	"""显示总金额"""
	print(money)
def atm_3():
	"""存钱"""
	global money
	money_add = int(input("请输入你要存的钱数："))
	money += money_add
	print("您现在的总金额是%s" % (money))
	return money


def atm_4():
	"""取钱"""
	global money
	money_draw = int(input("请输入你要取的钱数："))
	money -= money_draw
	print("您现在的总金额是%s" % (money))
	return money


def atm_5():
	"""退出"""
	print("感谢你使用屌丝银行！")
money = 999
while True:
	menu = """请选择你要的业务：
		***********************************
		余额请按“2”
		存款请按“3”
		取款请按“4”
		返回主菜单请按“1”
		退出请按“5”
		***********************************
		"""
	press = input(menu)
	if press == '2':
		atm_2()
	elif press == '3':
		atm_3()
	elif press == '4':
		atm_4()
	elif press == '5':
		atm_5()
		break
	else:
		print(menu)

print ("您现在的存款是%d"%money)

'''menu = """请选择你要的业务：
	***********************************
	余额请按“2”
	存款请按“3”
	取款请按“4”
	返回主菜单请按“1”
	退出请按“5”
	***********************************
	"""
press = input(menu)
money = 999
#new_money = 0

class Atm():

	def __init__(self, press):
		self.press = press

	def atm_1(self):
		"""返回主菜单"""
		if self.press == "1":
			print(menu)
			choose = input("请选择你需要的业务：")
			self.press = choose
			return self.press

	def atm_2(self):
		"""显示总金额"""
		if self.press == "2":
			print(money)
			choose = input("""
			返回上一层请按'1'
			退出请按5：""")
			self.press = choose
			return self.press

	def atm_3(self):
		"""存钱"""
		global money #

		if press == "3":
			money_add = int(input("请输入你要存的钱数："))
			money += money_add
			print("您现在的总金额是%s" % (money))
			choose = input("""
						返回上一层请按'1'
						退出请按5：""")
			self.press = choose
			a = self.press + "money"
			return self.press, money

	def atm_4(self):
		"""取钱"""
		global money
		if press == "4":
			money_draw = int(input("请输入你要取的钱数："))
			money -= money_draw
			print("您现在的总金额是%s" % (money))
			choose = input("""
						返回上一层请按'1'
						退出请按5：""")
			self.press = choose
			return self.press, money

	def atm_5(self):
		"""退出"""
		if self.press == "5":
			print("感谢你使用屌丝银行！")

#while True:
#	atm = Atm(press)
#	press = atm.atm_2()
#	if press == '1':
#		atm.atm_1()
#		continue
#	elif press == '5':
#		atm.atm_5()
#		break
#while True:
#	atm = Atm(press)
#	press = atm.atm_3()
#	if press == "1":
#		atm.atm_1()
#		continue
#	elif press == '5':
#		atm.atm_5()
#		break
while True:
	atm = Atm(press)
	press = atm.atm_4()
	print (money)
	if press == "1":
		atm.atm_1()
	elif press == '5':
		atm.atm_5()
		print(money)
		break

'''