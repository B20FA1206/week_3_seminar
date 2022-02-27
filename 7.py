list = [1, 1, 2, 2, 3]

res = []
for i in list:
	if i not in res:
		res.append(i)

print (str(res))
