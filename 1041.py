v = input().split()
x = float(v[0])
y = float(v[1])
if(x == 0  and y == 0):
	print(f"Origem")
elif(x == 0):
	print(f"Eixo Y")
elif(y == 0):
	print(f"Eixo X")
elif(x > 0 and y >0):
	print(f"Q1")
elif(x <0 and y >0):
	print(f"Q2")
elif(x < 0 and y < 0):
	print(f"Q3")
elif(x > 0 and y < 0):
	print(f"Q4")