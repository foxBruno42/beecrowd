v = input().split()
if (int(v[1]) > int(v[2])) and (int(v[3]) > int(v[0])) and (int(v[2])+int(v[3]) > int(v[0])+int(v[1])) and int(v[2]) > 0 and int(v[3]) > 0 and (int(v[0])%2==0):
	print(f"Valores aceitos")
else:
	print(f"Valores nao aceitos")