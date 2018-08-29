# Opens a text document writes your name to the file
# 08/30/2018
# CSC121-0001 AW1T1 - Name Input
# Brian Schweikart
#

def main():
    # Get information from unser
    print('Enter your name')
    name1 = input('Name #1: ')

    # Open stated file 
    myfile = open('my_name.txt', 'w')

    # write name to file
    myfile.write(name1 + '\n')

    # Display statment and close file.
    myfile.close()
    print('The name was written to my_name.txt')

# Start program
main()
    
