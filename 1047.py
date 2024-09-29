hrs = input().split()
hi, mi, hf, mf = int(hrs[0]), int(hrs[1]), int(hrs[2]), int(hrs[3])
d = ((hf*60)+mf) - ((hi*60)+mi)
if(d<=0):
	d += 24*60
print(f"O JOGO DUROU {int(d/60)} HORA(S) E {d%60} MINUTO(S)")