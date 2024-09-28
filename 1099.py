qtd = int(input())
for passo in range(qtd):
	num = input().split()
	a = int(num[0])
	b = int(num[1])
	tt = 0
	if(a > b):
		aux = a
		a = b
		b = aux
	a+=1
	for x in range(a,b):
		if(not(x%2==0)):
			tt+=x
	print(f"{tt}")