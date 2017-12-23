class KaoDiGua:
	def __init__(self):
		self.cookedLv = 0
		self.cookedString = "生的"
	def __str__(self):
		return '''
		**********************
		这个地瓜现在是：%s
		这个地瓜现在的等级是：%d'''%(self.cookedString, self.cookedLv)
	def cook(self, times):
		self.cookedLv += times
		if self.cookedLv > 8:
			self.cookedString = "烤焦了"
		elif self.cookedLv > 5:
			self.cookedString = "熟了"
		elif self.cookedLv > 3:
			self.cookedString = "半生不熟"
		else:
			self.cookedString = "生的"

digua = KaoDiGua()
print (digua)
digua.cook(1)
print (digua)
digua.cook(3)
print (digua)
