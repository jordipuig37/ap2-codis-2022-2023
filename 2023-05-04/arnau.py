from yogi import *
import heapq
from typing import TypeAlias


Punt: TypeAlias = tuple[int,int]


def h(p:Punt, t:Punt)->int:
    """Retorna l'heurísitca d'un punt qualssevol. Segueix la norma del taxista."""

    return abs(p[0] - t[0]) + abs(p[1] - t[1])


def trobacami(s:Punt, t:Punt, obstacles: list[Punt]) -> None:
    """Troba el camí més curt possible del punt S al punt T"""
    
    f = {} # diccionari per valor de f 
    g = {} # diccionari per valor de g
    pred = {s:0} # diccionari de predecessors
    g[s] = 0
    f[s] = h(s,t)
    Q = [(f[s],s)] # open nodes
    G : set[Punt] = {s} #punts visitats
    
    while Q:
        
        u: Punt = heapq.heappop(Q)[1]
        if u == t: 
            return pred[u]
        adjacents: set[Punt] = {(u[0]+1,u[1]), (u[0]-1,u[1]), (u[0],u[1]+1), (u[0]+1,u[1]-1)} - set(obstacles) #connexions de u
        for punt in adjacents: 
            if punt not in G: # g[v]=∞ if v ∉ g
                G.add(punt)
                g[punt]=10**6 
        for v in adjacents: 
            gv = g[u] + 1 #1 cost de desplaçar-se d'un punt a un altre
            if v not in G or gv < g[v]: 
                g[v] = gv
                f[v] = gv + h(v,t)
                pred[v] = pred[u] + 1
                heapq.heappush(Q, (f[v],v))
        

def main()->None:
    s: Punt = (read(int),read(int))
    t: Punt = (read(int),read(int))
    obstacles: list[Punt] = list()
    x: int = scan(int)
    while x is not None:
        y: int = read(int)
        obstacles.append((x,y))
        x=scan(int)
    print(trobacami(s,t,obstacles))
    
if __name__ == "__main__":
    main()
