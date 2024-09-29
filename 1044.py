v = input().split()
a = int(v[0])
b = int(v[1])
if(a > b):
	x = a%b
else:
	x = b%a
if(x == 0):
	print(f"Sao Multiplos")
else:
	print(f"Nao sao Multiplos")