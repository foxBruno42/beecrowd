from datetime import datetime
d1=input().split()
h1=input()
d2=input().split()
h2=input()
diferenca = datetime.strptime(h2,'%H : %M : %S') - datetime.strptime(h1,'%H : %M : %S')
h1=h1.split()
h2=h2.split()
if(int(h2[0])<int(h1[0])):
    print(f'{(int(d2[1])-int(d1[1]))-1} dia(s)')
else:
    if(int(h2[2])<int(h1[2])):
        print(f'{(int(d2[1])-int(d1[1]))-1} dia(s)')
    else:
        if(int(h2[2])<int(h1[2])):
            print(f'{(int(d2[1])-int(d1[1]))-1} dia(s)')
        else:
            print(f'{(int(d2[1])-int(d1[1]))} dia(s)')
print(f'{diferenca.seconds // 3600} hora(s)')
print(f'{(diferenca.seconds % 3600) // 60} minuto(s)')
print(f'{diferenca.seconds % 60} segundo(s)')