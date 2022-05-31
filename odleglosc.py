import math as math

plik = open("australian.dat")
lista = []

for value in plik:
    w = list(map(lambda e: float(e),value.split()))
    lista.append(w)

def MetrykaEuklidesowa(listaA, listaB):
    e = 0
    for i in range(len(listaA)-1):
        e = e + (listaA[i]-listaB[i])**2
    wynik = math.sqrt(e)
    return wynik



print(MetrykaEuklidesowa(lista[0], lista[1]))
print(MetrykaEuklidesowa(lista[0], lista[2]))
print(MetrykaEuklidesowa(lista[0], lista[3]))