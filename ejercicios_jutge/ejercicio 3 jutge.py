numero = input().split()
while len(numero) < 2:
    numero += input().split()
numero =[int(x) for x in numero]
print(sum(numero))