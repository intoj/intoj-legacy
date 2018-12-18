def Toascii(code):
	a = ""
	for i in code:
		a += hex(ord(i)) + ' '
	return a

while True:
	print(Toascii(input()))
