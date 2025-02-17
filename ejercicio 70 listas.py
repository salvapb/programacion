x = int(input("Introduce el número de palabras que deseas ingresar: "))

lista1 = []
for i in range(x):
    palabra = input(f"Introduce la palabra {i + 1}: ")
    lista1.append(palabra)

lista2 = lista1.copy()

lista1.sort()

lista2.sort(reverse=True)

print("Contenido de lista1 en orden ascendente:")
print(lista1)
print("Contenido de lista2 en orden descendente:")
print(lista2)