#64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:a) total de paresb) total de imparesc) total de números positivosd) total de números negativose) total de cerosf) total de la suma de todos los números introducidos

var_num=int(input("introduce un numero: "))
var_par=0
var_impar=0
var_pos=0
var_neg=0
var_sum=0
var_cero=0
while var_num!=-99:
    var_sum+=var_num
    if var_num>0:
        var_pos+=1
    else:
        var_neg+=1
    if var_num%2==0:
        var_par+=1
    else:
        var_impar+=1
    if var_num==0:
        var_cero+=1
    
    var_num=int(input("introduce un numero: "))
    if var_num==-99:
        print("RESUMEN")
    if var_num==-99 and var_par>0:
        print(f"el numero de pares ha sido {var_par}")
    if var_num==-99 and var_impar>0:
        print(f"el numero de impares ha sido {var_impar}")
    if var_num==-99 and var_pos>0:
        print(f"el numero de numeros positivos ha sido {var_pos}")
    if var_num==-99 and var_neg>0:
        print(f"el numero de numeros negativos ha sido {var_neg}")
    if var_num==-99 and var_cero>0:
        print(f"el numero de ceros ha sido {var_cero}")
    if var_num==-99:
        print(f"la suma total es {var_sum}")
        
        
    
    
    
