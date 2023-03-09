import math
from yogi import read,tokens

def minim_autonomia(parades:int, camí: list[int], senderos: int) -> int:
    """Donades el nombre de parades permeses, la llista ordenada segons el trajecte amb les distàncies entre parades i el nombre de trajectes a fer,
     es retorna el mínim d'autonomia que necessita un vehicle per poder dur a terme tal tasca"""
    if parades == 0:
        return sum(camí)
    if parades == senderos - 1:
        return max(camí)
    
    divisor = camí[0]
    for k in range(1,len(camí)):
        divisor = math.gcd(divisor,camí[k])
    mínim = max(max(camí),sum(camí)//(parades+1))
    màxim = sum(camí)
    return minim_autonomia_rec(mínim,màxim,camí,divisor,parades)
    
def minim_autonomia_rec(minim: int, maxim: int, camí: list[int], divisor: int, parades: int) -> int:
    """Donat un interval [minim,maxim] d'autonomia, la distància entre les parades, el màxim comú divisor de les distàncies i
    el nombre de parades permeses, retorna el mínim d'autonomia necessàri recursivament"""
    if minim == maxim:
        return minim
    mid = (minim+maxim)//2
    mid = mid  - mid%divisor
    if legal(mid,parades,camí):
        return minim_autonomia_rec(minim,mid,camí,divisor,parades)
    else:
        return minim_autonomia_rec(mid+divisor,maxim,camí,divisor,parades)

def legal (autonomia: int, n_parades: int, cami: list[int]) -> bool:
    """Donat una autonomia, el nombre de parades permeses i les distàncies entre parades, retorna si es podrà fer el viatge"""
    kilometres = 0
    for i in cami:
        if autonomia >= kilometres + i:
            kilometres += i
        else:
            n_parades -= 1
            kilometres = i
    if n_parades < 0:
        return False
    
    else:
        return True
    
def main():
    for x in tokens(int):
        y = read(int)
        camí = [read(int) for _ in range(x)]
        print(minim_autonomia(y,camí,x))

if __name__ == "__main__":
    main()
