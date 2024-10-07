"""
Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos. Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os valores do vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.

Entrada
A entrada contém 15 números inteiros.

Saída
Imprima a saída conforme o exemplo abaixo.
"""
def imprimeVetor(vet,txt):
    i=0
    for num in vet:
        print(f'{txt}[{i}] = {num}')
        i+=1

impar=[]
par=[]
for i in range(15):
    n=int(input())
    if(n%2==0):
        par.append(n)
    else:
        impar.append(n)
    
    if(len(par)==5):
        imprimeVetor(par,'par')
        par=[]
    
    if(len(impar)==5):
        imprimeVetor(impar,'impar')
        impar=[]
imprimeVetor(impar,'impar')
imprimeVetor(par,'par')