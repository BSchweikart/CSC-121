# Brian Schweikart
#09-01-2018
#CSC-121 H1HW1 - Average Numbers
# This takes the numbers saved to a .txt file adds them then divides total by amount of numbers
# then displays the avg of the numbers

def main():
	# Read and set the file name
	numbers_file = open('numbers.txt', 'r')	

	# Set var
	total = 0 # set to zero
	lineNumber = 0 # set to zero
	line = numbers_file.readline() # set to zero
	
	while line != '':
		lineNumber += 1 # read line add one
		total += int(line) # read each line get numbers from line
		line = numbers_file.readline() # set line as each line read
	# total number of numbers then divided by the amount of numbers used
	avg = total / lineNumber
	
	#display the avg of the numbers
	print(format(avg, '.2f'))
			
			
main()