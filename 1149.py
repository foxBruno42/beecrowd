"""
Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma de A + i para cada i com os valores (0 <= i <= N-1). Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.
Entrada

A entrada contém somente valores inteiros, podendo ser positivos ou negativos. Todos os valores estão na mesma linha.
Saída

A saída contém apenas um valor inteiro.
"""
num = input().split()
A=0
B=0
for n in num:
    if(int(n)>0):
        if(A==0):
            A=int(n)
        elif(B==0):
            B=int(n)
tt=0
for i in range(B):
    tt+=A
    A+=1
print(tt)