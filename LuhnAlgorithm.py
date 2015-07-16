# Program: Luhn's Verficiation Algorithm
#  Author: Colling Mitchell
#    Date: 2015 July 16th
# Purpose: Theoretical program to test if a set of 16 digit numbers can be considered a credit card number.
#          The intent is to check if it works, but not actually run it since it would take more life times
#          than about 20 generations of human beings just to compile it all.

# CONSTANTS
ALGORITHM_CONSTANT = 9


def confirmLuhn(number):                                 #==== Luhn's Algo ==========================
	count = 0                                            # Sum all numbers excluding the last number.
	sum   = 0                                            # For every other number, square it.
                                                         # Comapre the last digit of the CC number
	for digit in number:                                 # against the last digit of the sum.
		num = int(digit)
		if   count == 15:                                # If final digit,
			return (sum *ALGORITHM_CONSTANT %10 == num)  # compare final digits.
		elif count % 2 == 1:                             # If off number,
			sum   += num*num                             # square number.
			count +=1
		else:                                            # If not off number,
			sum   += num                                 # just add the number to the sum
			count += 1                                   #===========================================


outfile = open("CCNumbers.txt", 'w')                      # File openning, obviously.
                                                          # First we generate the number space that we're testing.
for x in range(0, 0000000000000100):                      # The real CC number space is actually [0, 9999999999999999], but that's too much.
	xString = "%.16d" % x                                 # This is probably lazy design, but I want to fill out the space of numbers and keep the 0's
	if confirmLuhn(xString): outfile.write(xString+"\n")  # If it's one of them, then write the result to the file.

outfile.close()                                           # BILLIONS OF YEARS OF WORK AND YOU FORGOT TO CLOSE THE STORAGE FILE IN THE CODE?!?
