import random
acumulado=0
print("bienvenido al juego del 7 y medio")
respuesta= ""
repetir=""
respuesta=input("quieres carta s/n: ")
while respuesta != "n" and repetir !="n":
   
    if respuesta=="s":
        carta=random.randint(1,12)
        print("tu carta es:",carta)
    
    if carta>9 and carta<13:
        acumulado+=0.5 
        print("acumulas ",acumulado)
        
    else:
        acumulado+=carta
        print("acumulas:", acumulado)
    respuesta=input("quieres carta s/n: ")
        
if acumulado==7.5:
    print("Enhorabuena, has ganado la partida")
if acumulado>5.9 and acumulado<7.5:
    print("Has sido un poco conservador")
if acumulado<6:
    print("Quizás tendrías que arriesgar un poco ¿no?")
if acumulado>7.5:
    print("Has perdido la partida!")
    repetir=input("¿quieres repetir la partida? s/n: ")
