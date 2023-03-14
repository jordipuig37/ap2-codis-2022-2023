import math
from yogi import read, tokens
from functools import cmp_to_key

INF = 100000000

class Pt:
    x: float
    y: float
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Comparador que ordena segons la coordenada x
def comp(a : Pt, b : Pt) -> int:
    if(a.y < b.y): return 1
    return -1

# Comparador que ordena segons la coordenada y
def comp2(a : Pt, b : Pt) -> int:
    if(a.x < b.x): return 1
    return -1

def dist(a : Pt, b : Pt) -> float:
    return math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)

def findmin(a : list[Pt], l : int, r: int) -> float:

    if l >= r:
        return INF

    mid = (l+r)//2
   
   #Calculem la cota superior de les dues meitats
    d = min(findmin(a, l, mid), findmin(a, mid+1, r))

    #Filtrem els punts de cada meitat segons la cota obtinguda
    left : list[Pt]=list()
    right : list[Pt]=list()


    for i in range(l, mid+1):
        if abs(a[mid].x-a[i].x) <= d:
            left.append(a[i])
    for i in range(mid+1, r+1):
        if abs(a[mid].x-a[i].x) <= d:
            right.append(a[i])
    if len(left)==0 or len(right)==0:
        return d

    #Ordenem per coordenada y els dos conjunts de punts
    left.sort(key=cmp_to_key(comp2))
    right.sort(key=cmp_to_key(comp2))

    # itl i itr són els iteradors de la columna esquerra i dreta respectivament
    itl, itr = 0,0

    bestd = dist(left[itl], right[itr])
    while itl < len(left):
        while itr < len(right) and right[itr].y <= left[itl].y+d:
            bestd = min(bestd, dist(left[itl], right[itr]))
            itr += 1
        itl += 1
        if itl < len(left) and itr < len(right):
            bestd = min(bestd, dist(left[itl], right[itr]))
        itr = max(0, itr-10)

    return min(bestd, d)

def main():
    a : list[Pt]=list()
    for x in tokens(float):
        y = read(float)
        a.append(Pt(x, y))

    #ordenem per coordenada x
    a.sort(key=cmp_to_key(comp))
    print('{:.5f}'.format(findmin(a, 0, len(a)-1)))

if __name__ == '__main__':
    main()