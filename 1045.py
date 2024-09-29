import sys
v = input().split()
x = []
x.append(float(v[0]))
x.append(float(v[1]))
x.append(float(v[2]))
x.sort(reverse = True)
A = float(x[0])
B = float(x[1])
C = float(x[2])
if(A >= (B+C)):
	print("NAO FORMA TRIANGULO")
	sys.exit()
if(A*A == ((B*B)+(C*C))):
	print("TRIANGULO RETANGULO")
if(A*A>((B*B)+(C*C))):
	print("TRIANGULO OBTUSANGULO")
if(A*A<((B*B)+(C*C))):
	print("TRIANGULO ACUTANGULO")
if((A==B)and(B==C)):
	print("TRIANGULO EQUILATERO")
if((A==B)and(B!=C)or(A==C)and(C!=B)or(B==C)and(C!=A)):
	print("TRIANGULO ISOSCELES")