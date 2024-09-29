import math
v = input().split()
n1, n2, n3, n4 = float(v[0])*0.2, float(v[1])*0.3, float(v[2])*0.4, float(v[3])*0.1
media = round((n1+n2+n3+n4),2)
print(f"Media: {media:.1f}")
if(media >= 7.00):
	print("Aluno aprovado.")
elif(media >=5.00):
	print(f"Aluno em exame.")
	exam = float(input())
	print(f"Nota do exame: {exam:.1f}")
	exam = (exam + media)/2;
	if(exam >= 5):
		print(f"Aluno aprovado.")
	else:
		print(f"Aluno reprovado")
	print(f"Media final: {exam:.1f}")
else:
	print(f"Aluno reprovado.")