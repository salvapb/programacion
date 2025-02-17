cantidad = int(input("Introduce la cantidad de números que deseas ingresar: "))

numeros = []


for i in range(cantidad):
    numero =input(f"Introduce el número {i + 1}: ")
    numeros.append(numero)


numeros.sort()


print("Los números ordenados de menor a mayor son:")
print(numeros)