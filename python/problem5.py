# project euler problem 5

from datetime import datetime

startTime = datetime.now()

print("This run started at " + str(startTime))

number = 1

while(True):
	result = [False, False, False, False, False, False, False, False, False, False,
		False, False, False, False, False, False, False, False, False, False]
	remainder = 0

	
	for i in range(20):
		if number % (i+1) == 0:
			result[i] = True
		else:
			remainder = (i+1) - (number % (i+1))
			break
	
	if number % 1000000 == 0:
		print("fail")

	if all(result):
		print(number)
		break
	else:
		number += remainder

print("...completed in " + str(datetime.now() - startTime) + " seconds.")
