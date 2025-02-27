#75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por pantalla los siguientes resultados: a. Cantidad total de valores b. Cantidad de números c. Cantidad de letras d. Cantidad de mayúsculas e. Suma de los valores numéricos

lista1 = ['a', 'b', 'D', 'x', 'r', 'X', 3, 'h', 'w', 2, 'i']

total_valores = len(lista1)

cantidad_numeros = sum(1 for item in lista1 if isinstance(item, int))

cantidad_letras = sum(1 for item in lista1 if isinstance(item, str) and item.isalpha())

cantidad_mayusculas = sum(1 for item in lista1 if isinstance(item, str) and item.isupper())

suma_numeros = sum(item for item in lista1 if isinstance(item, int))

print("Número de valores:", total_valores)
print("Cantidad de números:", cantidad_numeros)
print("Cantidad de letras:", cantidad_letras)
print("Cantidad de mayúsculas:", cantidad_mayusculas)
print("Suma total de números:", suma_numeros)


