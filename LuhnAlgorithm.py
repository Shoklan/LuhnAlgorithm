# Program: Luhn's Verficiation Algorithm
# Author: Colling Mitchell
# Date: 2015 March 24th
# Purpose: Theoretical program to test if a set of 16 digit numbers can be considered a credit card number.
#          The intent is to check if it works, but not actually run it since it would take more life times
#          than about 20 generations of human beings just to compile it all.


def confirmLuhn(number):
	count = 0
	sum   = 0

	for digit in number:
		num = int(digit)
		if count % 2 == 1: num = returnSingleDigit(num)   # Luhn's algorithm doubles every odd number before summing.
		if count == 15   : return (sum % 10 == num)       # Return if the check is true.
		else: count += 1




def returnSingleDigit(num):
	if num < 10: return num
	else       : return (num % 10) + (digit / 10)         # Be very careful about which version of Python you use.
		                                                  # 2.x will give give you an integer value, 3.x will return float.

outfile = file("CCNumbers.txt")                      # File openning, obviously.
                                                     # First we generate the number space that we're testing.
for x in range(0, 0000000000000100):                 # The real CC number space is actually [0, 9999999999999999], but that's too much.
	xString = "%.16d" % x                            # This is probably lazy design, but I want to fill out the space of numbers and keep the 0's
	if confirmLuhn(xString): outfile.write(xString)  # If it's one of them, then write the result to the file.

outfile.close()                                      # BILLIONS OF YEARS OF WORK AND YOU FORGOT TO CLOSE THE STORAGE FILE IN THE CODE?!?
