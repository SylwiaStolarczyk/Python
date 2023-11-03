lista = [-4,-3,-2,-1,0,1,2,3,4]

for v in lista:
    if v is 0:
        print(v, "liczba jest zerem")
    elif v%2 == 0:
        print(v, "liczba parzysta")
    else:
        print(v, "liczba nieparzysta")