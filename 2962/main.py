import sys
import math

class DisjointSet:
    def __init__(self, n:int):
        # Inicializa a lista 'parent' onde cada elemento é seu próprio pai
        # Inicializa a lista 'rank' que mantém o "peso" ou a "profundidade" da árvore
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x:int):
        '''
        - busca com compressao de caminho
        - nao representa quem nao é pai de si mesmo
        - busca recursiva para encontrar o representante
        '''
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # aqui faz a compressao
        return self.parent[x]

    def union(self, x:int, y:int):
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

def union_find_check(M:int, N:int, sensors:list) -> str:
    t = len(sensors) # numero dos sensores
    dsu = DisjointSet(t + 5) # cria nós adicionais

    # verificando os nos com as bordas e une ao nós adicionais
    for i, sensor in enumerate(sensors):
        x, y, r = sensor['x'], sensor['y'], sensor['r']

        if x - r <= 0: # esquerda
            dsu.union(t, i)
        if y + r >= N: # cima
            dsu.union(t + 1, i)
        if x + r >= M: # direita
            dsu.union(t + 2, i)
        if y - r <= 0: # baixo
            dsu.union(t + 3, i)

    # verifica o que sobrepoe no par dos sensores
    for i in range(t):
        for j in range(i + 1, t):
            dx = sensors[i]['x'] - sensors[j]['x']
            dy = sensors[i]['y'] - sensors[j]['y']
            distance_squared = dx * dx + dy * dy
            radius_sum_squared = math.pow((sensors[i]['r'] + sensors[j]['r']),2)
            
            # se tiver sensores soprepostos une
            if radius_sum_squared >= distance_squared:
                dsu.union(i, j)

    # verificando as conexoes nas extremidades
    left = dsu.find(t)
    top = dsu.find(t + 1)
    right = dsu.find(t + 2)
    bottom = dsu.find(t + 3)

    # Se há uma conexão entre extremidades nao da pra roubar
    if left == bottom  or left == right or top == right or top == bottom:
        return "N"

    return "S"

def run():
    input = sys.stdin.read
    data = input().strip().split('\n')

    index = 0
    while index < len(data):
        if data[index].strip() == '':
            break
        
        # Dimensões do salão e o número de sensores
        M, N, K = map(int, data[index].split())
        index += 1

        # Lista para armazenar as informações dos sensores
        sensors = []

        # K sensores
        for _ in range(K):
            # (X, Y) indica a localização do sensor e S indica a sua sensibilidade
            X, Y, S = map(int, data[index].split())
            sensors.append({'x': X, 'y': Y, 'r': S})
            index += 1

        sensors.sort(key=lambda sensor: (sensor['x'], sensor['y']))

        vaunion_find_check_value =  union_find_check(M, N, sensors)

        print(vaunion_find_check_value)

if __name__ == "__main__":
    run()