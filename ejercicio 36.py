#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.

var1=int(input("introduce los numeros: "))
total=0
for contador in range (var1):
    total=total+contador+1
print("la suma total de los numeros es",total)
