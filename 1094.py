tt,ttc,ttr,tts = 0,0,0,0
num = int(input())
for i in range(num):
	entrada = input().split()
	tt += int(entrada[0])
	if(entrada[1] == "C"):
		ttc += int(entrada[0])
	if(entrada[1] == "R"):
		ttr += int(entrada[0])
	if(entrada[1] == "S"):
		tts += int(entrada[0])
print(f"Total: {tt} cobaias")
print(f"Total de coelhos: {ttc}")
print(f"Total de ratos: {ttr}")
print(f"Total de sapos: {tts}")
print(f"Percentual de coelhos: {((ttc/tt)*100):.2f} %")
print(f"Percentual de ratos: {((ttr/tt)*100):.2f} %")
print(f"Percentual de sapos: {((tts/tt)*100):.2f} %")