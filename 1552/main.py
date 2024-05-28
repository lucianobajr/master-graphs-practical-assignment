import sys
import math
from heapq import heappush, heappop

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def solve(n, points):
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(points[i][0], points[i][1], points[j][0], points[j][1])
            heappush(edges, (distance, i, j))
    
    dsu = DisjointSet(n)
    mst_weight = 0.0
    edges_count = 0

    while edges_count < n - 1:
        distance, u, v = heappop(edges)
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst_weight += distance
            edges_count += 1

    return mst_weight / 100

def run():
    input = sys.stdin.read
    data = input().split()

    index = 0
    C = int(data[index])
    index += 1

    results = []

    for _ in range(C):
        n = int(data[index])
        index += 1

        points = []
        for _ in range(n):
            x = int(data[index])
            y = int(data[index + 1])
            points.append((x, y))
            index += 2

        value = solve(n, points)
        results.append("{:.2f}".format(value))

    print("\n".join(results))

if __name__ == "__main__":
    run()