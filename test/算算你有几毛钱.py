# 询问你有多少个五分钱
f_number = int(input("请输入你有多少个五分钱："))
# 询问你有多少个二分钱
t_number = int(input("请输入你有多少个二分钱："))
# 询问你有多少个一分钱
o_number = int(input("请输入你有多少个一分钱："))
# 计算钱的总数，单位是RMB
sum_rmb = (f_number * 0.05) + (t_number * 0.02) + (o_number * 0.01)
print (str(sum_rmb) + " RMB")