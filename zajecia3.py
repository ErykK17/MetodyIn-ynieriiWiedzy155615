import copy
file = open("australian.dat","r")
lista = []
for line in file:
    row = line.split()
    lista.append(list(map(lambda x: float(x),row)))


def metryka_euklidesowa(listaA,listaB):
    suma = 0
    for i in range(len(listaA)-1):
        suma += (listaA[i] - listaB[i]) ** 2
    return suma ** 0.5


y = lista[0]
slownik = {}

for element in lista [1:]:
    if slownik.get(element[-1]) == None:
        slownik[element[-1]] = [metryka_euklidesowa(element,y)]
    else:
        slownik[element[-1]].append(metryka_euklidesowa(element,y))


for key, value in slownik.items():
    print(key,value)