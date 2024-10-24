#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado

var1=float(input("introduce tu nota: "))

if var1 >10:
    print("tu nota no esta entre 0 0 10")

elif var1>5:
    print(f"tienes un {var1}, estas aprobado")
    
elif var1<5:
    print(f"tienes un {var1}, estas suspendido")
    