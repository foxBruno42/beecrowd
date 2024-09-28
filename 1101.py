while(True):
    a,b=input().split()
    a=int(a)
    b=int(b)
    if(a>0 and b>0):
        if(a > b):
            aux = a
            a = b
            b = aux
        sum = 0
        nums = []
        for x in range(a,(b+1)):
            sum += x
            nums.append(x)
        
        print(*nums, end=' ')
        print(f'Sum={sum}')
    else:
        exit()