a1, b1, a2, b2 = map(int, input().split())

resultado = "?"
interseccion = []


if a1 == a2 and b1 == b2:
    resultado = "="
elif a1 >= a2 and b1 <= b2:
    resultado = "1"
elif a2 >= a1 and b2 <= b1:
    resultado = "2" 


inicio_interseccion = max(a1, a2)
fin_interseccion = min(b1, b2)

if inicio_interseccion <= fin_interseccion:
    interseccion = [inicio_interseccion, fin_interseccion]


if interseccion:
    print(f"{resultado} , [{interseccion[0]},{interseccion[1]}]")
else:
    print(f"{resultado} , []")