pos,neg,par,imp = 0,0,0,0
for x in range(5):
	n = int(input())
	if(n>0):
		pos+=1
	elif(n<0):
		neg+=1
	if(n%2==0):
		par+=1
	else:
		imp+=1
print(f"{par} valor(es) par(es)")
print(f"{imp} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)")
print(f"{neg} valor(es) negativo(s)")