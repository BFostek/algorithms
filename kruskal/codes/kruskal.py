from unionFind import UnionSet


class Kruskal:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def kruskal_mst(self):
        self.edges.sort(key=lambda edge: edge[2])

        mst = []
        uf = UnionSet(self.vertices)

        for u, v, weight in self.edges:
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                mst.append((u, v, weight))

        return mst


def main():
    vertices = ["A", "B", "C", "D"]
    kruskal = Kruskal(vertices)
    kruskal.add_edge("A", "B", 1)
    kruskal.add_edge("B", "C", 2)
    kruskal.add_edge("C", "D", 3)
    kruskal.add_edge("A", "D", 4)
    mst = kruskal.kruskal_mst()
    print("Arestas na Árvore Geradora Mínima (MST):")
    for u, v, weight in mst:
        print(f"{u} -- {v} (peso: {weight})")


if __name__ == "__main__":
    main()
