#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
var1=float(input("introduce el primer numero: "))
var2=float(input("introduce el segundo numero: "))


if var1 >10 or var2>10:
    print("uno o los dos numeros introducidos son mayores que los limites establecidos")

elif var1<var2:
    print(f"el numero {var2} es mayor que el numero {var1}")
    
elif var1>var2:
    print(f"el numero {var1} es mayor que el numero {var2}")
    
else:
    print("ambos numeros son iguales")
    