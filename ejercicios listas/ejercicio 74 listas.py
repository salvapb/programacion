#74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de entre las 2 listas.

lista1 = ["casa", "mesa", "sal", "sol", "agua"]
lista2 = ["casa", "luz", "tres", "tren", "sol", "pan"]

repetidos = []
no_repetidos = []

for palabra in lista1:
    if palabra in lista2:
        repetidos.append(palabra)
    else:
        no_repetidos.append(palabra)
for palabra in lista2:
    if palabra not in lista1:
        no_repetidos.append(palabra)
print("Palabras que se repiten:", repetidos)
print("Palabras que no se repiten:", no_repetidos)