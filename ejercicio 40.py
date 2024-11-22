#40. Crea un programa que cuente todos los números pares hasta el número 50

num=50
pares=0
impares=0
for contador in range(num):
    if contador%2:
        pares=pares+1
    else:
        impares=impares+1
print(f"el total de pares es {pares}")
print(f"el total de impares es {impares}")