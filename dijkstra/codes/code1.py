import heapq


def dijkstra_problema1(grafo, origem):
    h_queue = []
    distances = {item: (float("inf")) for item in grafo}
    parent = {item: None for item in grafo}
    visited = set()
    distances[origem] = 0
    h_queue.append((0, origem))
    while h_queue:
        dist, curr = heapq.heappop(h_queue)
        if curr in visited:
            continue
        visited.add(curr)
        for vizinho in grafo[curr].keys() :
            curr_size = grafo[curr][vizinho] + dist
            if curr_size < distances[vizinho]:
                distances[vizinho] = curr_size
                parent[vizinho] = curr
                heapq.heappush(h_queue, (curr_size, vizinho))

    return distances, {item: reconstruir_caminho(parent, item) for item in grafo}

def reconstruir_caminho(parent, destino):
    caminho = []
    while destino is not None:
        caminho.append(destino)
        destino = parent[destino]
    return list(reversed(caminho))

if __name__ == "__main__":
    grafo = {
        "X": {"Y": 1, "Z": 4},
        "Y": {"X": 1, "Z": 2, "W": 7},
        "Z": {"X": 4, "Y": 2, "W": 1},
        "W": {"Y": 7, "Z": 1, "V": 3},
        "V": {"W": 3},
    }
    print(dijkstra_problema1(grafo, "X"))
