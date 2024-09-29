while(True):
    a,b=input().split()
    a=int(a)
    b=int(b)
    if(a!=b):
        if(a < b):
            print('Crescente')
        else:
            print('Decrescente')
    else:
        exit()