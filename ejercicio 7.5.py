import random

print("bienvenido al juego del 7 y medio")
respuesta=input("quieres carta s/n: ")
while respuesta=="s":
    carta=random.randint(1,12)
    print(f"tu carta es: {carta}")
    if carta>10 and carta<12:
        print("acumulas 0.5")