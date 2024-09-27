v = input().split()
a, b, c = float(v[0]), float(v[1]), float(v[2])
if((a+b)>c and (b+c)>a and (a+c)>b):
	print(f"Perimetro = {(a+b+c):.1f}")
else:
	print(f"Area = {(((a+b)*c)/2):.1f}")