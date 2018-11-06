# Brain Schweikart
# M2HW1 - Number Analysis
# 11/01/18
# This program takes user input set at 20 then
# finds the min-max-avg value

twenty_number_list = []

for i in range (20):
	num = input ('Enter number ' +str(i+1)+':')
	twenty_number_list.append(int(num))
	
	min_value = twenty_number_list[0]
	max_value = twenty_number_list[0]
	
	total = 0
	
for i in range(20):
		total += int(twenty_number_list[i])
if min_value > twenty_number_list[i]:
		min_value = twenty_number_list[i]
if max_value < twenty_number_list[i]:
		max_value = twenty_number_list[i]
		
average = total/20
	
print ('\nThe Details of the list are shown below')
print ('The lowest number is: '+str(min_value))
print ('The highest number is: '+str(max_value))
print ('The average value is: '+str(average))
