import yogi

def es_valid(auton: int, atur: int, distancies: list[int]) -> bool:
    """
    Donades una llista de distàncies entre ciutats, un nombre d'aturades i
    l'autonomia desitjada retorna la possibilitat de recórrer tota la carretera.   
    """
    
    acumulat = 0
    for tram in distancies:
        if tram > auton:
            return False
        
        if acumulat + tram > auton:
            atur -= 1
            if atur < 0:
                return False
            acumulat = tram            
        else:
            acumulat += tram
            
    return True
        
def min_autonomia_necessaria(atur: int, distancies: list[int]) -> int:
    """
    Donades una llista de distàncies entre ciutats i un nombre d'aturades,
    retorna l'autonomia necessària per recórrer tota la carretera.
    """
    
    left, right = -1, sum(distancies)
    mid = (left + right) // 2
    while left + 1 < right:
        mid = (left + right) // 2
        
        if es_valid(mid, atur, distancies):
            right = mid
        else:
            left = mid
    
    return left + 1
    
def main() -> None:
    
    for n in yogi.tokens(int):
        p = yogi.read(int)
        
        distancies = [yogi.read(int) for _ in range(n)]
    
        print(min_autonomia_necessaria(p, distancies))

if __name__ == '__main__':
    main()
