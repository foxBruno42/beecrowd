i,o = 0,0
n = int(input())
for x in range(n):
	c = int(input())
	if(c >= 10 and c <= 20):
		i+=1
	else:
		o+=1
print(f"{i} in")
print(f"{o} out")