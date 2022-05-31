import numpy as np 
import math as m 

def projekcja (v,u):
    ulamek = np.dot(v,u)/ np.dot (u,u)
    wynik = []
    for elem in u:
        wynik.append(elem*ulamek)
    return wynik 

def normalizacja (u):
    wynik = m.sqrt((u[0])**2 + (u[1])**2 + (u[2])**2)
    return wynik 

def obliczwektorE (u):
    wynik = []
    for elem in u:
        wynik.append(elem / normalizacja(u))
    return wynik 

def odejmowanie_wektorow(w1,w2):
    wynik = []
    for i in range (len(w1)):
        wynik.append (w1[i] - w2[i])
    return wynik

def obliczwektorQ(v1,v2):
    wektorQ = []
    u1 = v1
    e1 = obliczwektorE(u1)
    u2 = odejmowanie_wektorow (v2, projekcja(v2,u1))
    e2 = obliczwektorE(u2)
    wektorQ.append(e1)
    wektorQ.append(e2)
    return wektorQ

def obliczwektorR(q,a):
    qt = np.matrix(q)
    wynik = qt @ a
    return wynik

def rozkladQR(q, r):
    wynik  =  q @ r
    return wynik

v1 = [1,1,0]
v2 = [1,0,1]
at = [[1,1,0],[1,0,1]]
a = np.transpose(at)
q = obliczwektorQ(v1,v2)
r = obliczwektorR(q,a)
wynik = rozkladQR(np.transpose(q),r)
print (wynik)
wynikr = np.round(wynik,decimals=8)
print(wynikr)

