# Brain Schweikart
# M5HW2 - Employee Class
# 12/08/18
# Create a Class called Employee set the val get the vals 
# then print the informaton out

class Employee:
	def __init__(self, name, ID_number, dept, job_title):
		self.__name = name
		self.__ID_number = ID_number
		self.__depatment = dept
		self.__job_title = job_title
	
	def set_name(self, name):
		self.__name = name
	def set_ID_number(self, ID_number):
		self.__ID_number = ID_number
	def set_dept(self, dept):
		self.__depatment = dept
	def set_job_title(self, job_title):
		self.__job_title = job_title
		
	def get_name(self):
		return self.__name
	def get_ID_number(self):
		return self.__ID_number
	def get_dept(self):
		return self.__depatment
	def get_job_title(self):
		return self.__job_title
		
def main():
	
	e1 = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President') 
	e2 = Employee('Mark Jones', 39119, 'IT', 'Programmer')
	e3 = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')
	
	print('Employee 1 Information')
	print('Name: ', e1.get_name())
	print('ID Number: ', e1.get_ID_number())
	print('Department: ',e1.get_dept())
	print('Title: ', e1.get_job_title())
	print()
	print('Employee 2 Information')
	print('Name: ', e2.get_name())
	print('ID Number: ', e2.get_ID_number())
	print('Department: ',e2.get_dept())
	print('Title: ', e2.get_job_title())
	print()
	print('Employee 3 Information')
	print('Name: ', e3.get_name())
	print('ID Number: ', e3.get_ID_number())
	print('Department: ',e3.get_dept())
	print('Title: ', e3.get_job_title())
	
main()