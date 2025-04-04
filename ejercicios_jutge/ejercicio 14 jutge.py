import math


palabra= float(input())

piso = math.floor(palabra)
techo = math.ceil(palabra)
redondeo = math.ceil(palabra) if (palabra - piso) >= 0.5 else piso

print(piso, techo, redondeo)