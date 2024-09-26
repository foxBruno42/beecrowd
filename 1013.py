m = input().split()
a = int(m[0])
b = int(m[1])
c = int(m[2])
x = (a+b+abs(a-b))/2
print(f"{int((x+c+abs(x-c))/2)} eh o maior")