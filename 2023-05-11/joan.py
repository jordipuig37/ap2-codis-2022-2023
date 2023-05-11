from dataclasses import dataclass

from yogi import read


@dataclass()
class Edge:
    u: int
    v: int
    weight: int


def find_set(v: int, parent: list[int]) -> int:
    if parent[v] == v:
        return v
    parent[v] = find_set(parent[v], parent)
    return parent[v]


def union_sets(a: int, b: int, size: list[int], parent: list[int]) -> None:
    a = find_set(a, parent)
    b = find_set(b, parent)

    if a != b:
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]


def minimum_spanning_tree(edges: list[Edge], n: int) -> int:
    edges.sort(key=lambda e: e.weight)

    size: list[int] = [1 for i in range(n)]
    parent: list[int] = [i for i in range(n)]

    cost: int = 0

    for edge in edges:
        if find_set(edge.v, parent) == find_set(edge.u, parent):
            continue

        cost += edge.weight
        union_sets(edge.u, edge.v, size, parent)

    return cost


def main() -> None:
    n, m = read(int), read(int)
    while n:
        edges: list[Edge] = [
            Edge(read(int) - 1, read(int) - 1, read(int)) for _ in range(m)
        ]
        print(minimum_spanning_tree(edges, n))
        n, m = read(int), read(int)


if __name__ == "__main__":
    main()
