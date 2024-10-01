gas,alc,die,tipo=0,0,0,5
while(tipo != 4):
	tipo = int(input())
	if(tipo == 1):
		alc += 1
	elif(tipo == 2):
		gas += 1
	elif(tipo == 3):
		die += 1
print(f"MUITO OBRIGADO")
print(f"Alcool: {alc}")
print(f"Gasolina: {gas}")
print(f"Diesel: {die}")