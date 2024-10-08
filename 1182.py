def linhas():
    return [0 for i in range(12)]
matriz = [linhas() for i in range(12)]

line=int(input())
op=input()
num=0
for i in range(12):
    for j in range(12):
        x=float(input())
        matriz[i][j]=x

for i in range(12):
    num+=matriz[i][line]

if(op=='S'):
    print(f'{num:.1f}')
else:
    print(f'{(num/12):.1f}')