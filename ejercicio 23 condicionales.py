#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógico

var1=float(input("introduce tu nota: "))

if var1 >10:
    print("tu nota no esta entre 0 0 10")

elif var1>8.5:
    print(f"tu nota es un {var1} has sacado un excelente")

elif var1 > 6.5 and var1<8.5 :
    print(f"tu nota es un {var1} has sacado un notable")
    
elif var1>=5 and var1<6.5:
    print(f"tu nota es un {var1} has sacado un satisfactorio")
    
elif var1<5:
    print(f"tu nota es un {var1} has sacado un insuficiente")