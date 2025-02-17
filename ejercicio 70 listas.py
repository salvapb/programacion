#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo.
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