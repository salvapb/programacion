#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales

var1=float(input("introduce el primer numero: "))
var2=float(input("introduce el segundo numero: "))

if var1<var2:
    print(f"el numero {var2} es mayor que el numero {var1}")
    
if var1>var2:
    print(f"el numero {var1} es mayor que el numero {var2}")
    
if var1==var2:
    print("ambos numeros son iguales")