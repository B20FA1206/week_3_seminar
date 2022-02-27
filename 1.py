def palindrome(s):
	return s == s[::-1]

s = "121"
res = palindrome(s)

if res:
	print("Yes")
else:
	print("No")
