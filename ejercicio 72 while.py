#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista
letras = []

def normalizar_vocal(vocal):
    return vocal.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')

while True:
    letra = input("Introduce una letra: ")
    
    
    letra_normal = normalizar_vocal(letra)
    
    if letra_normal not in [normalizar_vocal(l) for l in letras]:
        letras.append(letra)  
    

    repetir = input("¿Deseas repetir s/n: ")
    if repetir.lower() != 's':
        break


print(letras)