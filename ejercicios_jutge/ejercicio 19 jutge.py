
a1, b1, a2, b2 = map(int, input().split())


inicio_interseccion = max(a1, a2)
fin_interseccion = min(b1, b2)


if inicio_interseccion > fin_interseccion:
    print("[]")  
else:
    print(f"[{inicio_interseccion},{fin_interseccion}]")  