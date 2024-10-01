op,gremio,inter,empate,qtdgn=1,0,0,0,0
while(op!=2):
	jg = input().split()
	qtdgn += 1
	if(int(jg[0]) < int(jg[1])):
		gremio += 1
	elif(int(jg[0]) > int(jg[1])):
		inter += 1
	else:
		empate += 1
		
	print("Novo grenal (1-sim 2-nao)")
	op = int(input())
print(f"{qtdgn} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{empate}")
if(gremio>inter):
	print("Gremio venceu mais")
elif(gremio<inter):
	print("Inter venceu mais")
else:
	print("Nao houve vencedor")