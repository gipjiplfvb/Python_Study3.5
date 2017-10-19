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