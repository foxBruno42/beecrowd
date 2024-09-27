import math
v = input().split()
A = float(v[0])
B = float(v[1])
C = float(v[2])
if(A == 0 or C == 0) :
	print(f"Impossivel calcular")
else:
	try:
		R1 = (-B+(math.sqrt((B**2)-4*A*C)))/(2*A)
		R2 = (-B-(math.sqrt((B**2)-4*A*C)))/(2*A)
		if((pow(B,2)-4*A*C) < 0 or A == 0):
			print(f"Impossivel calcular")
		else:
			print(f"R1 = {R1:.5f}")
			print(f"R2 = {R2:.5f}")
	except ValueError:
		print(f"Impossivel calcular")