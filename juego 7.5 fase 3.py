# PARTE 3: 7.5
import random
alias=input("introduce tu alias: ")
while True:
        acumulado = 0
        acumulado_banca=0
        print("Bienvenido al juego del 7 y medio ", alias)
        while True:
            
            respuesta=input("¿Quieres carta? (s/n): ")
            if respuesta=="n":
                break
            elif respuesta=="s":
                carta=random.randint(1, 12)
                while carta in [8, 9]:
                    carta=random.randint(1, 12)
                print(f" {alias}, Tu carta es:",carta)
                if carta in [10, 11, 12]:
                    acumulado +=0.5
                else:
                    acumulado +=carta
                print(f"{alias} ,Acumulas:",acumulado)
                
                
                if acumulado > 7.5:
                   while acumulado_banca <5:
                    print("Has perdido la partida! Ahora es el turno es de la BANCA")
                    banca=input("TURNO DE LA BANCA. Pulsa enter para visualizar carta a carta")
                    carta_banca=random.randint(1, 12)
                    while carta_banca in [8, 9]:
                        carta_banca=random.randint(1, 12)

                    print("la banca ha sacado:",carta_banca)
                    if carta_banca in [10, 11, 12]:
                        acumulado_banca +=0.5
                    else:
                        acumulado_banca +=carta_banca
                    print("la banca acumula", acumulado_banca)
                    if acumulado_banca>5 and acumulado_banca<7.5:
                        print("LA BANCA SE PLANTA Y GANA LA PARTIDA")
                        repetir=input("¿Quieres jugar otra partida? (s/n): ")
        
        
        if acumulado == 7.5:
            print("Enhorabuena, has ganado la partida Ahora es el turno es de la BANCA")
            banca=input("TURNO DE LA BANCA. Pulsa enter para visualizar carta a carta")
            carta_banca=random.randint(1, 12)
            while carta_banca in [8, 9]:
                carta_banca=random.randint(1, 12)
            print("la banca ha sacado:",carta_banca)
            if carta_banca in [10, 11, 12]:
                acumulado_banca +=0.5
            else:
                acumulado_banca +=carta_banca
            print("la banca acumula", acumulado_banca)
        
        
        elif 6 <= acumulado < 7.5:
            print("Has sido un poco conservador Ahora es el turno es de la BANCA")
            banca=input("TURNO DE LA BANCA. Pulsa enter para visualizar carta a carta")
            carta_banca=random.randint(1, 12)
            while carta_banca in [8, 9]:
                carta_banca=random.randint(1, 12)
            print("la banca ha sacado:",carta_banca)
            if carta_banca in [10, 11, 12]:
                acumulado_banca +=0.5
            else:
                acumulado_banca +=carta_banca
            print("la banca acumula", acumulado_banca)
        
        
        else:
            print("Quizás tendrías que arriesgar un poco ¿no? Ahora es el turno de la BANCA")
            banca=input("TURNO DE LA BANCA. Pulsa enter para visualizar carta a carta")
            carta_banca=random.randint(1, 12)
            while carta_banca in [8, 9]:
                carta_banca=random.randint(1, 12)
            print("la banca ha sacado:", carta_banca)
            if carta_banca in [10, 11, 12]:
                acumulado_banca +=0.5
            else:
                acumulado_banca +=carta_banca
            print("la banca acumula", acumulado_banca)
        repetir=input("¿Quieres jugar otra partida? (s/n): ")
        
        if repetir == "n":
            break
        
#TURNO DE LA BANCA. Pulsa enter para visualizar carta a carta