#83
import random

lista = ["casa", "barco", "gato", "perro", "madera", "agua", "puente", "pantalón"]
puntuaciones = []

while True:
    palabra_secreta = random.choice(lista)
    intentos = 0
    print("Nueva partida. Adivina la palabra secreta.")
    
    while True:
        intento = input("Introduce la palabra secreta: ")
        intentos += 1
        if intento == palabra_secreta:
            puntos = max(8 - (intentos - 1), 1)  
            puntuaciones.append(puntos)
            print("ACERTASTE")
            print(f"Puntuación en esta partida: {puntos}")
            break
        else:
            print("SIGUE JUGANDO")
    
    continuar = input("¿Quieres jugar otra partida? (s/n): ").lower()
    if continuar != 's':
        break

puntuacion_total = sum(puntuaciones)
media_posible = len(puntuaciones) * 8 / 2  
print(f"Puntuación total: {puntuacion_total}")
print(f"La media de las partidas realizadas es: {media_posible}")

if puntuacion_total > media_posible:
    print("Tienes buena suerte")
else:
    print("Dedícate al parchís")
