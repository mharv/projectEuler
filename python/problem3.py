# project euler problem 3

import sympy

number = int(input("give a number: "))


def getLargestPrimeFactor(number):
	i = 1
	while number / sympy.prime(i) != 1:
		if number % sympy.prime(i) != 0:
			i += 1
		else:
			number = number / sympy.prime(i)
	
	return sympy.prime(i)

print("the largest prime factor is: " + str(getLargestPrimeFactor(number)))


