# project euler problem 14

import pyperclip

def collatzSequence(number):
	if number % 2 == 0:
		return number / 2
	else:
		return (number * 3) + 1




startingNumber = 1 
result = [0, 0] # first number is the starting number
		# second is number of terms to belonging to starting number

while startingNumber < 1000000:
 	#print(startingNumber)
	startingNumberCopy = startingNumber
	termCounter = 1
	while startingNumberCopy != 1:
		startingNumberCopy = collatzSequence(startingNumberCopy)
		termCounter += 1
	
	if termCounter > result[1]:
		result[1] = termCounter
		result[0] = startingNumber

	startingNumber += 1

print("the number " + str(result[0]) + " has " + str(result[1]) + " terms, the highest amoung the numbers below 1 million.")

pyperclip.copy(result[0])
