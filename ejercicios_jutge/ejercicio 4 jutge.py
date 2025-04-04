numero = input().split()
while len(numero)<3:
    numero+= input().split()
numero = [int(x) for x in numero]
print(sum(numero))