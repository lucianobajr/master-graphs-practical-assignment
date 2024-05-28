import sys
import math
import heapq

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_distances(points):
    n = len(points)
    distances = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(points[i][0], points[i][1], points[j][0], points[j][1])
            distances[i][j] = distances[j][i] = distance
    return distances

def prim(n, distances):
    min_heap = [(0, 0)]
    visited = set()
    mst_weight = 0.0
    edges_count = 0

    while min_heap and edges_count < n:
        distance, u = heapq.heappop(min_heap)
        if u not in visited:
            visited.add(u)
            mst_weight += distance
            edges_count += 1
            for v in range(n):
                if v not in visited:
                    heapq.heappush(min_heap, (distances[u][v], v))

    return mst_weight / 100.0

def main():
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

        distances = calculate_distances(points)
        value = prim(n, distances)
        results.append("{:.2f}".format(value))

    print("\n".join(results))

if __name__ == "__main__":
    main()