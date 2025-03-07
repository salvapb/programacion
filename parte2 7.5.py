import random

deposito = 100

print("Bienvenido al juego del 7 y medio")
print("INSTRUCCIONES:")
print("Las cartas suman al acumulado el valor de su número, las cartas 8 y 9 no están, y las cartas 10, 11 y 12 suman 0.5")
print("Hay un depósito de 100 puntos. Al acabar una partida con una puntuación exacta de 7.5 sumas 10 puntos al depósito, si te pasas de 7.5 restarás 10 puntos.")
print("Si te plantas entre 6 y 7 sumarás 5 puntos, si te plantas con menos de 6 restarás 5 puntos.")

while deposito > 0:
    acumulado = 0
    print(f"Tu depósito actual es: {deposito}")
    
    while True:
        respuesta = input("¿Quieres carta? (s/n): ")
        if respuesta == "n":
            break
        elif respuesta == "s":
            carta = random.randint(1, 12)
            
            while carta in [8, 9]:
                carta = random.randint(1, 12)
            print(f"Tu carta es: {carta}")
            
            if carta in [10, 11, 12]:
                acumulado += 0.5
            else:
                acumulado += carta
                
            print(f"Acumulas: {acumulado}")
            
            if acumulado > 7.5:
                print("Has perdido la partida!")
                deposito -= 10
                break

    if acumulado == 7.5:
        print("Enhorabuena, has ganado la partida")
        deposito += 10
    elif acumulado > 7.5:
        print("Te pasaste de 7.5, has perdido!")
    elif acumulado < 6:
        print("Te plantaste con menos de 6, pierdes 5 puntos.")
        deposito -= 5
    elif 6 <= acumulado < 7.5:
        print("Te plantaste con un buen número, sumas 5 puntos.")
        deposito += 5

    print(f"Tu depósito ahora es: {deposito}")
    
 
    if deposito == 0:
        print("Has quedado sin puntos, el juego ha terminado.")
        break
    
    repetir = input("¿Quieres jugar otra partida? (s/n): ")
    if repetir == "n":
        print("Gracias por jugar!")
        break