# Brain Schweikart
# M6HW1 - Employee & Production Class
# 12/09/18
# Create Employee and Production worker Classes
# Inheritance from emp to production class then display

class Employee:
	def __init__(self, name, number):
		self.__name = name
		self.__number = number
	
	def set_emp_name(self, name):
		self.__name = name
	def set_emp_number(self, number):
		self.__number = _number
		
	def get_emp_name(self):
		return self.__name
	def get_emp_number(self):
		return self.__number

class ShiftSupervisor(Employee):
	def __init__(self, name, number, shift_num, pay_rate):
		Employee.__init__(self,name,number)
		self.__shift_num = shift_num
		self.__pay_rate = pay_rate
	
	def set_shfit_num(self, shift_num):
		self.__shift_num = shift_num
	def set_pay_rate(self, pay_rate):
		self.__pay_rate = pay_rate
		
	def get_shift_num(self):
		return self.__shift_num
	def get_pay_rate(self):
		return self.__pay_rate
		
def main():
	
	print('Please enter the informaton')
	name = input('Enter name:')
	number = input('Enter employee number:')
	shift = input('Enter shift number:')
	pay = input('Enter pay rate:')
	
	emp = ShiftSupervisor(name, number, shift, pay)
	
	print('Employee Information as follows')
	print('Name: ', emp.get_emp_name())
	print('Number: ', emp.get_emp_number())
	print('Shift Number: ', emp.get_shift_num())
	print('Pay Rate: ', emp.get_pay_rate())

main()