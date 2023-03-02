import yogi as yg
from typing import TypeAlias

Marcador: TypeAlias = dict[str, list[int]]


def llegeix_noms(n: int) -> Marcador:
    """Llegeix n noms, i ens genera un marcador inicialitzat a zero."""
    marcador: Marcador = dict()
    for i in range(n):
        nom = yg.read(str)
        marcador[nom] = [0, 0, 0]
    return marcador


def processa_resultat(p1: str, p2: str, res: str, marcador: Marcador) -> None:
    """Suma els punts als jugadors p1 i p2, segons el resultat res,
    actualitzant els valors del marcador.
    """
    if res == "1-0":
        marcador[p1][0] += 1
        marcador[p2][2] += 1
    elif res == "1/2-1/2":
        marcador[p1][1] += 1
        marcador[p2][1] += 1
    else:  # res == "0-1":
        marcador[p1][2] += 1
        marcador[p2][0] += 1


def escriu_marcador(marcador: Marcador) -> None:
    """Escriu les dades del marcador ordenades per nom de jugador."""
    llista_tuples = list(marcador.items())
    ordenat = sorted(llista_tuples, key=lambda x: x[0])
    for k, v in ordenat:
        print(k, *v)


def main():
    n = yg.read(int)
    marcador = llegeix_noms(n)
    p1 = yg.scan(str)
    while p1 is not None:
        p2 = yg.read(str)
        resultat = yg.read(str)
        processa_resultat(p1, p2, resultat, marcador)
        p1 = yg.scan(str)

    escriu_marcador(marcador)


if __name__ == "__main__":
    main()
