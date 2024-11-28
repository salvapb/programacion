posicion=1
var=input("inttroduce una palabra: ")
letra=input("introdyuce una letra: ")

for recorrido in var:
    if recorrido==letra:
        print("la posicion de la letra", letra," es:", posicion)
    posicion=posicion+1
