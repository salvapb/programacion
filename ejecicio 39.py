#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0
num_numeros=int(input("introduce la cantidad de numeros que deseas introducir: "))
num_0=0
num_pos=num_0
num_neg=0
for contador in range(num_numeros):
    numero=float(input("introduce tu numero: "))
    
    if numero>0:
        num_pos=num_pos+1
    if numero<0:
        num_neg=num_neg+1
    if numero==0:
        num_0=num_0+1
print("La cantidad de números positivos es: ", num_pos)
print("La cantidad de números negativos es: ", num_neg)
print("La cantidad de ceros es: ", num_0)