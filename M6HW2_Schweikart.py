# Brain Schweikart
# M6HW2 - Employee & ShiftSupervisor Class
# 12/09/18
# Create Employee and ShiftSupervisor  Classes
# Inheritance from emp to ShiftSupervisor class then display

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
	def __init__(self, name, number, salary, bonus):
		Employee.__init__(self,name,number)
		self.__salery = salary
		self.__bonus = bonus
	
	def set_salary(self, salary):
		self.__salery = salary
	def set_pay_rate(self, bonus):
		self.__bonus = bonus
		
	def get_salary(self):
		return self.__salery
	def get_bonus(self):
		return self.__bonus
		
def main():
	
	print('Please enter the informaton')
	name = input('Enter name:')
	number = input('Enter employee number:')
	salary = input('Enter Salary:')
	bonus = input('Enter Bouns:')
	print()
	
	emp = ShiftSupervisor(name, number, salary, bonus)
	
	print('Employee Information as follows')
	print('Name: ', emp.get_emp_name())
	print('Number: ', emp.get_emp_number())
	print('Salary: ', emp.get_salary())
	print('Bouns: ', emp.get_bonus())

main()