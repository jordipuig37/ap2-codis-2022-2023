import yogi as yg


def llegeix_xarxa(n, m):
    """Llegeix les dades i retorna la reresentacio de la xarxa."""
    xarxa= [set() for i in range(n)]
    for _ in range(m):
        i = yg.read(int)
        j = yg.read(int)

        xarxa[i].add(j)
        xarxa[j].add(i)

    return xarxa


def calcula_amics(jo, xarxa):
    """Calcula quants amics d'amics tinc (jo)."""
    els_meus_amics = xarxa[jo]
    resultat = els_meus_amics.copy()
    for amic in els_meus_amics:
        resultat = resultat | xarxa[amic]
    resultat.discard(jo)

    return len(resultat)


def main():
    n = yg.read(int)
    m = yg.read(int)
    
    xarxa = llegeix_xarxa(n, m)

    for amic in yg.tokens(int):
        print(calcula_amics(amic, xarxa))


if __name__ == "__main__":
    main()
