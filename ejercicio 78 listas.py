#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se deseaeliminar de la lista, siendo únicamente los números los valores permitidos para suprimir



lista1 = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']

while True:
    valor = input("Introduce el valor que deseas eliminar: ")

    if valor.isdigit():
        if valor in lista1:
            lista1.remove(valor)
            print(lista1)
        else:
            print("El valor introducido no está en la lista")
    else:
        print("Introduce un valor numérico")
    
    continuar = input("Deseas introducir otro valor s/n: ").lower()
    if continuar != 's':
        break
