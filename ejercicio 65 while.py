#65. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor

var_num=int(input("introduce un numero: "))
var_par=0
var_impar=0
var_pos=0
var_neg=0
var_sum=0
var_cero=0
var_mayor=var_num
var_menor=var_num
while var_num!=-99:
    var_sum+=var_num
    if var_mayor<var_num:
        var_mayor=var_num
    if var_menor>var_num:
        var_menor=var_num
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
    if var_num==-99:
        print(f"el numero mas pequeño ha sido {var_menor}")
    if var_num==-99:
        print(f"el numero más grande ha sido {var_mayor}")