# project euler problem 10


import sympy

'''

number = 0
i = 1
total = 0

while number < 2000000:
	number = sympy.prime(i)
	total += number
	i += 1
	number = sympy.prime(i)


print(total)
'''

print(sum([i for i in sympy.primerange(1, 2000000)]))	
