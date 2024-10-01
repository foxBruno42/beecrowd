"""
Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.
Entrada

O arquivo de entrada contém um número inteiro positivo N.
Saída

Imprima a saída conforme o exemplo fornecido.
"""
num=int(input())
p=1
for x in range(num):
    print(f'{p} {p+1} {p+2} PUM')
    p+=4