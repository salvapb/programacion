#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10
num_notas=int(input("introduce el numero de notas que quieres introducir: "))

for contador in range (num_notas):
    nota=float(input("introduce tu primera nota: "))
    if nota>5:
        print("asignatura aprobada")
    if nota<5:
        print("asignatura suspendida")
    if nota>11 or nota<0:
        print("has introducido la nota equivocada")