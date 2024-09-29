p = [4.0,4.5,5.0,2.0,1.5]
v = input().split()
print(f"Total: R$ {int(v[1])*float(p[int(v[0])-1]):.2f}")