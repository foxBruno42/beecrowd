x = input().split()
if(int(x[0]) >= int(x[1])):
	h = (int(x[1])+24) - int(x[0])
else:
	h = int(x[1]) - int(x[0])
print(f"O JOGO DUROU {h} HORA(S)")