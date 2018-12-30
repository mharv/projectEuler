# project euler problem 6

import math
from datetime import datetime

startTime = datetime.now()

sumOfNumbers = 0 
arrayOfSquares = []

for i in range(100):
	sumOfNumbers += (i+1)
	arrayOfSquares.append(math.pow(i+1, 2))


sumSquared = math.pow(sumOfNumbers, 2)
result = sumSquared - sum(arrayOfSquares)	
print(str(result) + " ...took " + str(datetime.now() - startTime) + " to calculate.")
