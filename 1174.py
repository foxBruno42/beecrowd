"""
Faça um programa que leia um vetor A[100]. No final, mostre todas as posições do vetor que armazenam um valor menor ou igual a 10 e o valor armazenado em cada uma das posições.

Entrada
A entrada contém 100 valores, podendo ser inteiros, reais, positivos ou negativos.

Saída
Para cada valor do vetor menor ou igual a 10, escreva "A[i] = x", onde i é a posição do vetor e x é o valor armazenado na posição, com uma casa após o ponto decimal.
"""
vetor = []
for i in range(100):
    n = float(input())
    vetor.append(n)

for i in range(100):
    if(vetor[i]<=10):
        print(f'A[{i}] = {vetor[i]:.1f}')