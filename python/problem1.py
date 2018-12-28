# project euler problem 1

total = 0

for i in range(1000):
  if i % 5 == 0:
    total += i
  elif i % 3 == 0:
    total += i
  else:
    pass

print(total)
