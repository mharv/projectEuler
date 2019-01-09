# project euler problem 16

bigNumber = 2**1000
bigString = str(bigNumber)
total = 0

for i in range(len(bigString)):
	total += int(bigString[i])

print(total)

