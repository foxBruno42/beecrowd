n = int(input())
for x in range(n):
	nuns = input().split()
	print(f"{(float(nuns[0])*0.2)+(float(nuns[1])*0.3)+(float(nuns[2])*0.5):.1f}")