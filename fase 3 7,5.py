import random

alias = input("Introduce tu alias: ")

while True:
    acumulado = 0
    acumulado_banca = 0
    print(f"Bienvenido al juego del 7 y medio, {alias}")

    
    while True:
        
            respuesta = input("¿Quieres carta? (s/n): ")
            if respuesta == "n":
                break
            elif respuesta == "s":
                carta = random.randint(1, 12)
                while carta in [8, 9]: 
                    carta = random.randint(1, 12)

                print(f"{alias}, tu carta es: {carta}")
                acumulado += 0.5 if carta in [10, 11, 12] else carta
                print(f"{alias}, acumulas: {acumulado}")

                if acumulado > 7.5:
                    print("¡Te has pasado! Pierdes la partida. Ahora juega la banca.")
                    break
            
       

  
    print("TURNO DE LA BANCA")
    while True:
        input("Pulsa ENTER para ver la carta de la banca...")
        carta_banca = random.randint(1, 12)
        while carta_banca in [8, 9]:
            carta_banca = random.randint(1, 12)

        print(f"La banca ha sacado: {carta_banca}")
        acumulado_banca += 0.5 if carta_banca in [10, 11, 12] else carta_banca
        print(f"La banca acumula: {acumulado_banca}")

        
        if acumulado > 7.5: 
            if acumulado_banca >= 5:
                print("La banca se planta y gana la partida.")
                break
        elif acumulado == 7.5:  
            if acumulado_banca >= 7.5:
                print("¡La banca se ha pasado! Gana ",alias )
                break
        elif acumulado_banca > 7.5:  
            print("¡La banca se ha pasado! Gana ", alias)
            break
        elif acumulado_banca > acumulado:  
            print("La banca supera a " , alias," y se planta.")
            break

   
    if acumulado <= 7.5 and acumulado_banca <= 7.5:
        if acumulado == acumulado_banca:
            print("Empate.")
        elif acumulado > acumulado_banca:
            print("¡Gana el jugador!")
        else:
            print("¡Gana la banca!")

    
    repetir = input("¿Quieres jugar otra partida? (s/n): ")
    if repetir == "n":
        print("Gracias por jugar. ¡Hasta la próxima!")
        break