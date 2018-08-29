# Opens the text document reads - display information
# 08/29/2018
# CSC121-0001 AW1T2 - Name Output
# Brian Schweikart
#

def main():
    # Opens named file
    infile = open('my_name.txt', 'r')

    # Reads information in named file
    file_contents = infile.read()

    # Closes named file
    infile.close()

    # Displays the information saved from file
    print(file_contents)

# Start program
main()

    
    
