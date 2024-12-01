#47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso. Respeta el formato de salida
var_primero = int(input("Introduce el primer intervalo: "))
var_segundo = int(input("Introduce el segundo intervalo: "))
if var_primero<var_segundo:
    for recorrido in range(var_primero, var_segundo):
        print(recorrido, end = "-")
    print(var_segundo)
else:
    for recorrido in range(var_primero, var_segundo, -1):
        print(recorrido, end = "-")
    print(var_segundo)