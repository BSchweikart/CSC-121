# Brain Schweikart
# M2HW3 - Lottery Number Gen.
# 11/01/18
# This program takes 9 numbers then random pick 7
# then display the 7 numbers

import random
random_digit = 0
random_number_list = []

print('Welcome to the lottery')
print('Pick your 7 numbers from 0 - 9\n')
for i in range(7):
	random_number = random.randint(0,9)
	random_number_list.append(random_number)
	random_digit = random_digit * 10 + random_number
	
print('Displaying the Lottery Number')
print('The Lottery Number is: ' + str(random_digit))

