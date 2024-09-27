import math
x = input().split()
y = input().split()
a = (float(x[0])-float(y[0]))
b = (float(x[1])-float(y[1]))
print(f"{math.sqrt((a**2)+(b**2)):.4f}")