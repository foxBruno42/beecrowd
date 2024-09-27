import sys
sal = float(input())
if(sal <= 0):
	sys.exit()
if(sal <= 400.00):
	taxa = 15
	dif = sal*(taxa/100)
elif(sal <=800):
	taxa = 12
	dif = sal*(taxa/100)
elif(sal<=1200):
	taxa = 10
	dif = sal*(taxa/100)
elif(sal <= 2000):
	taxa = 7
	dif = sal*(taxa/100)
elif(sal >2000.00):
	taxa = 4
	dif = sal*(taxa/100)

print(f"Novo salario: {(sal+dif):.2f}")
print(f"Reajuste ganho: {dif:.2f}")
print(f"Em percentual: {taxa:.0f} %")