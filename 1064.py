p,m = 0,0
for x in range(6):
	n = float(input())
	if(n>0):
		p+=1
		m+=n
print(f"{p} valores positivos")
print(f"{m/p:.1f}")