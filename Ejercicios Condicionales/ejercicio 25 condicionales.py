#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos

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