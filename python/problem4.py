# project euler problem 4

def palindromeCheck(n):

	try:
		n = str(n)
	except:
		print("hmm")
	
	if n == n[::-1]:
		return True
	else:
		return False


def findNumber():
	maxNumber = 0
	for i in range(999):
		for j in range(999):
			number = i*j
			if number > maxNumber and palindromeCheck(number):
				maxNumber = number
	return maxNumber



print(findNumber())
