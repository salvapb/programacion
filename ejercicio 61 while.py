#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar essuperior o igual a 40.
numero = int(input("Introduce el número que quieras multiplicar: "))

repeticiones = 0

while numero < 40 and repeticiones != 10:
    repeticiones += 1
    resultado = numero * repeticiones
    if resultado < 40:
        print(f"{numero} x {repeticiones} = {resultado}")
    else:
        print("Programa finalizado")
        break
