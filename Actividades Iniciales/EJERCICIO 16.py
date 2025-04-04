#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. Elresultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre unresultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso(raíz y división).

import math
var1=int(input("introduce un numero: "))
print(math.sqrt(var1))
print(round(math.sqrt(var1)/2))
