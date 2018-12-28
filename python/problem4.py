# project euler problem 4

numberOfDigits = int(input("enter the number of digits of the two numbers that the palindrome \nshould be made from (eg. 3 for a three digit number): "))

temp = ""
for i in range(numberOfDigits):
	temp = temp + "9"


maxNumber = int(temp)

print(maxNumber)

palindrome = False

def palindromeCheck(n):
	n = str(n)
	if n == n[::-1]:
		palindrome = True
		n = int(n)
		return True
	else:
		return False


while(palindrome != True):
	for i in range(1, 11):
		for n1 in range(maxNumber-(i*100), maxNumber):
			for n2 in range(maxNumber-(i*100), maxNumber):
				num = n1 * n2
				if palindromeCheck(num):
					largestPalindrome = num	
	

print(n)

