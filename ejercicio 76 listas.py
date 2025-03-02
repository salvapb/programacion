#76. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letrasy por otro los números permitiendo escoger orden ascendente o descendente. Como observarásen la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.
lista1 = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']

numeros = [int(c) for c in lista1 if c.isdigit()]
letras = [c for c in lista1 if c.isalpha()]

orden = int(input("Introduce 1 para visualizar en orden ascendente o 2 descendente: "))

if orden == 1:
    print(sorted(numeros))
    print(sorted(letras, key=lambda c: (c.lower(), c)))
elif orden == 2:
    print(sorted(numeros, reverse=True))
    print(sorted(letras, key=lambda c: (c.lower(), c), reverse=True))
else:
    print("Opción no válida")
