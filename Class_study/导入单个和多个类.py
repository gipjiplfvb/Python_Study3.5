"""导入单个类"""
print ("********汽车********")
from car import Car
my_new_car = Car('audi', 'a4', 2016)
print (my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


"""从一模块中导入多个类"""
print ("********电动汽车********")
from more_class import Car, ElectricCar, Battery

my_tesla = ElectricCar ('tesla', ' model s', 2016)
print (my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery
my_tesla.battery.get_range()
print ("当电瓶容量是85时")
my_tesla.battery.battery_size = 85
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()




