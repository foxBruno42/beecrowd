"""
Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?
Entrada

Não há nenhuma entrada neste problema.
Saída

A saída contém um valor correspondente ao valor de S.
O valor deve ser impresso com dois dígitos após o ponto decimal.
"""
x=3
y=2
s=1+(x/y)
while(x<=39):
    x+=2
    y=y*2
    s+=(x/y)
print(f'{s:.2f}')