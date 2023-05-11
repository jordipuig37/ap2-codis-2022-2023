'''
Un spanning tree d'un graf connex i no dirigit és un tree que conté tots els seus nodes
Un tree de n nodes té n-1 edges, i no conté cicles
'''

from yogi import read, tokens
import heapq

def mst(n: int, edges: list[dict[int, int]]) -> int:
    """
    Donats el nombre n de vèrtex d'un graf no dirigit, 
    i una llista de diccionaris edges que indiqui les arestes i els seus pesos d'aquest graf, 
    retorna la suma dels pesos de les arestes del seu minimum spanning tree.
    """

    visited = [True if i==1 else False for i in range(n+1)]
    heap: list[tuple[int, int]] = [] #heapq d'arestes a les quals podem accedir des del MST i el seu pes, implementades amb tuples (pes, nxt).
    pes_total = 0
    i = 0
    for v, p in edges[1].items():
        heapq.heappush(heap, (p, v))

    while i < n-1: #un MST té |V|-1 arestes 
        pes, nxt = heapq.heappop(heap) #Python fa el heap d'una tuple segons el primer element, en el nostre cas el pes
        if not visited[nxt]:
            i += 1
            visited[nxt] = True
            pes_total += pes
            for v, p in edges[nxt].items():
                if not visited[v]:
                    heapq.heappush(heap, (p, v))

    return pes_total  

def read_edges(n: int, m: int) -> list[dict[int, int]]:
    """
    Llegeix les m arestes i els seus pesos d'un graf amb n vèrtexs, 
    i les retorna en una llista de diccionaris, on el diccionari de la 
    i-èsima posició conté les arestes que van de i a j com a claus i el seu pes com a valors.
    """

    edges: list[dict[int, int]] = [dict() for _ in range(n+1)]
    for _ in range(m):
        u, v, p = read(int), read(int), read(int)
        if v not in edges[u] or edges[u][v] > p: #Només ens interessa l'aresta si no n'hi ha cap que connecti els mateixos vèrtexs amb <= pes
            edges[u][v] = p
            edges[v][u] = p
    return edges

def main() -> None:
    for n in tokens(int):
        print(mst(n, read_edges(n, read(int))))

if __name__ == "__main__":
    main()
