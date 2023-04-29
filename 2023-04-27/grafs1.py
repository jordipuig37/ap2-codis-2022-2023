import yogi as yg


def read_graph(n: int, m: int) -> list[list[int]]:
    """Read a directed graph with n nodes, m edges and return it represented by
    an adjecency list.
    """
    graph = [[] for _ in range(n)]
    for edge in range(m):
        src = yg.read(int)
        dest = yg.read(int)
        graph[src].append(dest)
    return graph


def has_path(
        source: int,
        destination: int,
        graph: list[list[int]],
        visited: list[bool]) -> bool:
    """Inicates whether there is a path from source to destination
    in the given graph.
    """
    if destination in graph[source]:
        return True
    else:
        visited[source] = True
        return any([has_path(next_, destination, graph, visited)
                        for next_ in graph[source] if not visited[next_]])


def main():
    n = yg.read(int)
    m = yg.read(int)

    graph = read_graph(n, m)
    visited = [False for i in range(len(graph))]

    src = yg.read(int)
    dst = yg.read(int)

    if has_path(src, dst, graph, visited):
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()