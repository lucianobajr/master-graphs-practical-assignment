import sys
import math

class DisjointSet:
    def __init__(self, n: int):
        # Inicializa a lista 'parent' onde cada elemento é seu próprio pai
        # Inicializa a lista 'rank' que mantém o "peso" ou a "profundidade" da árvore
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int):
        '''
        - busca com compressao de caminho
        - nao representa quem nao é pai de si mesmo
        - busca recursiva para encontrar o representante
        '''
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # aqui faz a compressao
        return self.parent[x]

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        # Unir dois conjuntos distintos em um único conjunto
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


def euclidean_distance(x1: int, y1: int, x2: int, y2: int):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def kruskal(n: int, edges: list) -> float:
    dsu = DisjointSet(n)

    edges.sort(key=lambda x: x[2])  # ordenando pelo peso
    mst_weight = 0.0  # valor arvore geradora minima

    for x, y, weight in edges:
        if dsu.find(x) != dsu.find(y):  # verifica se nao é ciclo
            dsu.union(x, y)
            mst_weight += weight

    return mst_weight


def solve(n: int, points: list) -> float:
    # criando os nós, par e distancia entre eles
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(
                x1=points[j][0],
                x2=points[i][0],
                y1=points[j][1],
                y2=points[i][1]
            )
            edges.append((i, j, distance))

    return kruskal(n=n, edges=edges) / 100


def run():
    input = sys.stdin.read
    data = input().strip().split('\n')

    index = 0
    while index < len(data):
        if data[index].strip() == '':
            break

        # quantidade de casos de teste
        C = int(data[index])
        index += 1

        for _ in range(C):
            # número de pessoas no grupo
            n = int(data[index])
            index += 1

            # Lista para armazenar as coordenadas das pessoas
            points = []

            for _ in range(n):
                # uma pessoa do grupo pelas suas coordenadas x e y na malha
                x, y = map(int, data[index].split())
                points.append((x, y))
                index += 1

            value = solve(n=n, points=points)

            print("{:.2f}".format(value))


if __name__ == "__main__":
    run()
