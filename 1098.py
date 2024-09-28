i = 0.0
j = 1.0
print(f"I=0 J={int(j)}")
print(f"I=0 J={int(j+1)}")
print(f"I=0 J={int(j+2)}")
for x in range(4):
	i+=0.2
	j+=0.2
	print(f"I={i:.1f} J={j:.1f}")
	print(f"I={i:.1f} J={j+1:.1f}")
	print(f"I={i:.1f} J={j+2:.1f}")
i=1.0
j=2.0
print(f"I=1 J={int(j)}")
print(f"I=1 J={int(j+1)}")
print(f"I=1 J={int(j+2)}")
for x in range(4):
	i+=0.2
	j+=0.2
	print(f"I={i:.1f} J={j:.1f}")
	print(f"I={i:.1f} J={j+1:.1f}")
	print(f"I={i:.1f} J={j+2:.1f}")
print(f"I=2 J=3")
print(f"I=2 J=4")
print(f"I=2 J=5")