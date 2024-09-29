n = int(input())
for x in range(n):
	a = int(input())
	if(a==0):
		print(f"NULL")
	else:
		if(a%2==0):
			par = 'EVEN'
		else:
			par = 'ODD'
		if(a>0):
			pos = 'POSITIVE'
		else:
			pos = 'NEGATIVE'
		print(f"{par} {pos}")