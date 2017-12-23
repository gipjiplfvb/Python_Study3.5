class Ren:
	"""关于人的描述"""
	def __init__(self, name):
		"""人的一些属性"""
		#人的名字
		self.name = name
		#人的血量
		self.xueliang = 100
		#刚开始这个人没有枪
		self.qiang = None

	def addzidan(self, danjia, zidan):
		"""给弹夹装子弹"""
		danjia.addzidan(zidan)

	def adddanjia(self, qiang, danjia):
		"""给枪装弹夹"""
		qiang.adddanjia(danjia)
	def addqiang(self, qiang):
		"""给人拿枪"""
		self.qiang = qiang
	def kaiqiang(self,diren):
		"""向敌人开枪"""
		self.qiang.she(diren)
	def diaoxue(self, shashangli):
		"""敌人掉血的信息"""
		self.xueliang -= shashangli
	def __str__(self):
		if self.xueliang > 0:
			return self.name + "剩余的血量为" + str(self.xueliang)
		else:
			return self.name + "已经死了，不要再打了太不人道了"
class DanJia:
	"""关于弹夹的描述"""
	def __init__(self, rongliang):
		"""弹夹的一些属性"""
		#弹甲的容量
		self.rongliang = rongliang
		#弹甲里面有多少子弹
		self.danjialist = []

	def addzidan(self,zidan):
		"""判断弹夹容量未满时，安装子弹"""
		if len(self.danjialist) < self.rongliang:
			self.danjialist.append(zidan)

	def __str__(self):
		"""打印弹夹的信息"""
		return "弹夹当前的子弹数量为：" + str(len(self.danjialist)) + "/" + str(self.rongliang)

	def chuzidan(self):
		#判断当前弹夹中是否有子弹
		if len(self.danjialist) > 0:
			#取弹夹里面最后压进去的一颗子弹
			zidan = self.danjialist[-1]
			#取了一个就少了，一个于是删除最后压进去的那个
			self.danjialist.pop()
			return zidan
		else:
			return None
class ZiDan:
	"""关于子弹的描述"""
	def __init__(self, shashangli):
		self.shashangli = shashangli
	def shanghai(self, diren):
		diren.diaoxue(self.shashangli)

class Qiang:
	"""关于枪的描述"""
	def __init__(self):
		self.danjia = None
	def __str__(self):
		if self.danjia:
			return "枪当前没有弹甲"
		else:
			return "枪当前有弹甲"
	def adddanjia(self, danjia):
		if not self.danjia:
			self.danjia = danjia
	def she(self, diren):
		zidan = self.danjia.chuzidan()
		if zidan:
			zidan.shanghai(diren)
		else:
			print("没有子弹了放空枪了。")

#人的名字
laowang = Ren("老王")
#弹夹的容量
danjia = DanJia(20)
print(danjia)
#给弹夹装子弹  五发子弹
i = 0
while i < 100:
	zidan = ZiDan(5)
	laowang.addzidan(danjia, zidan)
	i += 1
print(danjia)

qiang = Qiang()
print(qiang)

laowang.adddanjia(qiang, danjia)
print(qiang)

#创建一个敌人
diren = Ren("敌人")
print(diren)
a = 0
while a < 20:
	laowang.addqiang(qiang)
	laowang.kaiqiang(diren)
	a += 1
print(diren)
