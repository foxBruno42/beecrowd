sal = float(input())
if(sal <= 2000):
	print(f"Isento")
else:
	if(sal <= 3000):
		tax = ((sal - 2000) * 0.08)
	elif(sal <= 4500):
		tax = ((sal - 3000) * 0.18) + 80
	else:
		tax = ((sal - 4500) * 0.28)+350
	print(f"R$ {tax:.2f}")