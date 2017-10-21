menu = """请选择你要的业务：
	***********************************
	余额请按“1”
	存款请按“2”
	取款请按“3”
	返回主菜单请按“4”
	退出请按“5”
	***********************************
	"""
press = input(menu)
money = 999
new_money = 0
def atm_1(press):
	"返回主菜单"
	if press == "4":
		print(menu)
def atm_2(press):
	if press == "1":
		print(money)
def atm_3(press):
	global money
	if press == "2":
		money_add = int(input("请输入你要存的钱数："))
		money += money_add
		print("您现在的总金额是%s" % (money))
		return money
def atm_4(press):
	global money
	if press == "3":
		money_draw = int(input("请输入你要取的钱数："))
		money -= money_draw
		print("您现在的总金额是%s" % (money))
	return money
def atm_5(press):
	if press == "5":
		print("感谢你使用屌丝银行！")
atm_1(press)
atm_2(press)
atm_3(press)
atm_4(press)
atm_5(press)



'''









#
class Atm():
	"""银行取钱简单尝试"""
	def __init__(self,  press):
		#self.atm_menu = atm_menu
		#self.money_add = money_add
		#self.money_draw = money_draw
		#self.money_all = 9999
		self.press = press
		#press = input("请选择你要的业务：")
	def atm_1(self):
		"""显示菜单"""
		if self.press == "4":
			menu ="""请选择你要的业务：
***********************************
余额请按“1”
存款请按“2”
取款请按“3”
返回主菜单请按“4”
退出请按“5”
***********************************
"""
			print (menu)

	def atm_2(self):
		"""显示总金额"""
		if self.press == "1":
			print(self.money_all)
a = input("""请选择你要的业务：
***********************************
余额请按“1”
存款请按“2”
取款请按“3”
返回主菜单请按“4”
退出请按“5”
***********************************
""")
Atm.atm_1(a)
Atm.atm_2(a)

	#	def money_add(self):
#		if self.press == "2":
#			add_money = int(input("你要存多少钱："))
#			new_money = self.money_all + add_money
#			money = new_money
#			return money
#Atm.money_add()
'''
'''
money_all = 9999
while True:
	# 1. 我要做什么的选择
	print("显示余额请按1")
	print("存钱请按2")
	print("取钱请按3")
	print("退出请按4")
	print("返回首页请按5")
	press = input("请选择你要的业务：")
	# 2. 我一共有多少钱
	if press == '1':
		print(money_all)
		continue
	elif press == '5':
		continue
	#3. 我要存钱
	elif press == '2':
		money_add = int(input("你要存的钱数："))
		# 3.1 存钱之后一共是多少钱
		print("你现在的总额为：%d"%(money_all + money_add))
		continue
	#4. 我要取钱
	elif press == '3':
		money_jian = int(input("你要取的钱数："))
		#4.1 取钱之后还剩下多少。
		print("你现在的余额为：%d"%(money_all - money_jian))
		continue
	#5. 退出
	else:
		print("退出请按4")
		break
print("谢谢你使用屌丝银行。")


#def money_add(press):
#	if press == 1

#atm_menu()
'''
'''
		# 1. 我要做什么的选择
		press = input("请选择你要的业务：")
		# 2. 我一共有多少钱
		if press == '1':
			print(money_all)
			continue

		elif press == '5':
			continue
		#3. 我要存钱
		elif press == '2':
			money_add = int(input("你要存的钱数："))
			# 3.1 存钱之后一共是多少钱
			print("你现在的总额为：%d"%(money_all + money_add))
			continue
			#4. 我要取钱
		elif press == '3':
			money_jian = int(input("你要取的钱数："))
			#4.1 取钱之后还剩下多少。
			print("你现在的余额为：%d"%(money_all - money_jian))
			continue
		#5. 退出
		else:
			print("退出请按4")
			break
	print("谢谢你使用屌丝银行。")
'''