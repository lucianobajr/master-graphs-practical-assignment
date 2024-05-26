import sys
import heapq
from collections import defaultdict

INF = float('inf') # constante de infinito

def dijkstra(O: dict, D: dict, adj: defaultdict[any, list], num_nodes: int):
    dist: list[list[float]] = [[INF] * 30 for _ in range(num_nodes)] # matriz de distancia dist[u][c] -> menor distancia de u com a ultima palavra começa com c
    pq:list = [] # fila de prioridade

    for i in range(30):
        dist[O][i] = 0

    for v, t, cx in adj[O]: # adicionando as arestas do nó origem na fila de prioridade
        dist[v][cx] = t
        heapq.heappush(pq, (t, v, cx))

    while pq: # até ficar vazio
        d, u, c = heapq.heappop(pq) # menor item do heap
        if u == D: # caso alcance nó destino D, retorna menor distancia
            return d
        if d > dist[u][c]: # distancia é maior
            continue
        for v, t, cx in adj[u]: # processa vizinhos de u
            if cx == c: # verifica se a proxima palavra começa com a mesma da inteior
                continue
            if dist[v][cx] > dist[u][c] + t: # atualiza a distancia com caminho mais curto
                dist[v][cx] = dist[u][c] + t
                heapq.heappush(pq, (dist[v][cx], v, cx))

    return INF


def run():
    input = sys.stdin.read
    data = input().strip().split('\n')

    index = 0
    while True:
        M = int(data[index])
        if M == 0: # finalizar leitura quando M == 0 
            break
        index += 1

        a, b = data[index].split() # idiomas de origem e destino
        index += 1

        adj = defaultdict(list)
        mapa = {} # idiomas a indices numericos
        cnt = 0

        if a not in mapa:
            mapa[a] = cnt
            cnt += 1
        if b not in mapa:
            mapa[b] = cnt
            cnt += 1

        O = mapa[a]
        D = mapa[b]

        for _ in range(M): # pares de idiomas e palavra comuns
            idiom1, idiom2, commom_word = data[index].split()
            index += 1
            tam = len(commom_word)
            if idiom1 not in mapa: # mapeia idioma caso nao tenha sido
                mapa[idiom1] = cnt
                cnt += 1
            if idiom2 not in mapa:
                mapa[idiom2] = cnt
                cnt += 1
            u = mapa[idiom1]
            v = mapa[idiom2]

            # ord -> unicode do caracter
            # aresta bidirecional
            adj[u].append((v, tam, ord(commom_word[0]) - ord('a')))
            adj[v].append((u, tam, ord(commom_word[0]) - ord('a')))

        result = dijkstra(O, D, adj, cnt)
        if result == INF:
            print("impossivel")
        else:
            print(result)

if __name__ == "__main__":
    run()