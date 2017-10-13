"""一个模块里面存储多个类"""
"""一组用于表示燃油汽车和电动汽车的类"""
class Car():
	"""一次模拟描述汽车的简单尝试"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.oldmeter_reading = 0

	def get_descriptive_name(self):
		"""返回整洁的描述性名称"""
		long_name = str(self.year) + ' ' + self.make + self.model
		print (long_name.title())

	def read_odometer(self):
		"""打印一条消息，指出汽车的里程"""
		print ("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		"""
		将里程表读数设置为指定值
		拒绝将里程表往回拨
		:param mileage:
		:return:
		"""
		if mileage >= self.read_odometer:
			self.read_odometer = mileage
		else:
			print ("You can't roll back on odometer!")
	def increment_odometer(self, miles):
		"""将里程表的读数增加指定的量"""
		self.odometer_reading += miles
class Battery():
	"""一次模拟电动汽车电瓶的简单尝试"""

	def __init__(self, batter_size = 70):
		"""初始化电瓶的属性"""
		self.battery_size = batter_size

	def descrie_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print ("This car has a " + str(self.battery_size) + "-KWh battery.")

	def get_range(self):
		"""打印一条描述电瓶续航里程的消息"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "This car can go approximately " + str(range)
		message += " miles on full charge"
		print (message)
class ElectricCar(Car):
	"""模拟电动汽车的独特之处"""
	def __init___(self, make, model, year):
		"""
		初始化父类的属性，再初始化电动汽车特有的属性
		:param make:
		:param model:
		:param year:
		:return:
		"""
		super().__init__(make, model, year)
		self.battery == Battery()
my_tesla = ElectricCar('tesla', 'model s', 2016)
print (my_tesla.get_descriptive_name)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print ("当电瓶容量是85时")
my_tesla.battery_size = 85
my_tesla.battery.describe_battery()
my_tesla.battery.get_range