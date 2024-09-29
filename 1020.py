i = int(input())
print(f"{int(i/365)} ano(s)")
print(f"{int((i%365)/30)} mes(es)")
print(f"{int(((i%365)%30))} dia(s)")