def max(a, b, c):

	if (a >= b) and (a >= c):
		res = a

	elif (b >= a) and (b >= c):
		res = b
	else:
		res = c
		
	return res

a = 10
b = 100
c = 12
print(max(a, b, c))
