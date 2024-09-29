v = float(input())
if(v < 0 or v > 100.0):
	print(f"Fora de intervalo")
elif(v <= 25.0):
	print(f"Intervalo [0,25]")
elif(v <= 50.0):
	print(f"Intervalo (25,50]")
elif(v <= 75):
	print(f"Intervalo (50,75]")
else:
	print(f"Intervalo (75,100]")