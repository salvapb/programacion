#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra.
palabra = input("Introduce una palabra: ")

for recorrido in range(len(palabra)):
    letra = input("Introduce una letra: ")
    for recorrido in range(len(palabra)):    
        if palabra[recorrido]==letra:
            print("La letra está en la posición",recorrido+1)
      