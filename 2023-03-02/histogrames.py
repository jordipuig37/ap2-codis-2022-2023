""" Problema P80928   Histogrames
Notes: codi poc modular, falta documentació, utilitzar noms de variables reservats
       com per exemple 'max' enlloc de 'max_'.
"""
from yogi import *
import turtle



def main():
    barres=read(int)
    fronteres = [0.0]
    ll = []
    max = 0

    x=scan(int)
    while x is not None:
        ll.append(x)
        if(x>max):
            max=x
        x=scan(int)

    interval=max/barres
    ll.sort()
    altures = {}
    index=0
    max_altura=0

    for i in range(1,barres+1):
        fronteres.append(round(interval*i, 1))
        a = 0
        j = index
        while j<len(ll) and (ll[j]<=interval*i or ll[j] == max) :
            a += 1
            j += 1

        index=j

        altures[round(interval*i,1)] = a

        if(a>max_altura):
            max_altura=a


    for i in fronteres:
        if i != 0.0:
            altures[i] = (300/max_altura)*altures[i]

    dibuixar(barres,altures,fronteres)

def dibuixar(barres: int, altures: dict[float,int], fronteres: list[float]) -> None:
    amplada=300/barres
    turtle.hideturtle()
    for i in range(0, barres):
        turtle.penup()
        turtle.right(90)
        turtle.forward(15)
        turtle.write(fronteres[i])
        turtle.backward(15)
        turtle.left(90)
        turtle.pendown()

        turtle.forward(amplada)
        turtle.left(90)
        turtle.forward(altures[fronteres[i+1]])
        turtle.left(90)
        turtle.forward(amplada)
        turtle.left(90)
        turtle.forward(altures[fronteres[i+1]])
        turtle.left(90)
        turtle.forward(amplada)
        
    turtle.penup()
    turtle.right(90)
    turtle.forward(15)
    turtle.write(fronteres[-1])
    turtle.done()

if __name__ == "__main__":
    main()
