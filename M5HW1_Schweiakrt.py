# Brain Schweikart
# M5HW1 - Number Analysis
# 11/07/18
# This program takes the car class then speeds up by 5 then slows by 5
# 

class Car:
		def __init__(self,year_model,make):
			self.__year_model = year_model
			self.__make = make
			self.__speed = 0
		
		def accelerate(self):
			self.__speed +=5
		
		def brake(self):
			self.__speed -=5
		
		def get_speed(self):
			return self.__speed

def main():
	
	#Call Car Class and set
	car1 = Car(2016, 'GTR')
	
	#Accelerate
	car1.accelerate()
	
	print ('The current speed of the car is: ', + car1.get_speed())
	car1.accelerate()
	
	print ('The current speed of the car is: ', + car1.get_speed())
	car1.accelerate()
	
	print ('The current speed of the car is: ', + car1.get_speed())
	car1.accelerate()
		
	print ('The current speed of the car is: ', + car1.get_speed())
	car1.accelerate()	

	print ('The current speed of the car is: ', + car1.get_speed())
	car1.brake()
	
	print ('The current speed of the car is: ', + car1.get_speed())
	car1.brake()
	
	print ('The current speed of the car is: ', + car1.get_speed())
	car1.brake()
	
	print ('The current speed of the car is: ', + car1.get_speed())
	car1.brake()
	
	print ('The current speed of the car is: ', + car1.get_speed())
	car1.brake()
	
	print ('The current speed of the car is: ', + car1.get_speed())
		
main()