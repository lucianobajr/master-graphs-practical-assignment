import sys
from collections import defaultdict
import heapq

INF = float('inf')

def soldiers_probability_success_bfs(
        N:int, # números de pontos estratégicos
        K:int, # balas carregadas pelo soldado soviético
        P:float, # probabilidade do soldado matar um atirador
        roads:defaultdict[any, list], # par indicando existência de uma estrada ligando o ponto i ao j
        shooter_positions:list[int],  # posição de cada atirador
        starting_point:int, # ponto de partida de cada soldado
        destination_point:int # ponto de destino de cada soldado
    ) -> float:

    # Inicializa o contador de atiradores em cada ponto estratégico
    shooter_count = [0] * (N + 1)
    for position in shooter_positions:
        shooter_count[position] += 1

    # Inicializa aa com a probabilidade acumulada de sucesso para cada ponto
    probability_multiplier = [1.0] * (N + 1)
    for i in range(1, N + 1):
        for _ in range(shooter_count[i]):
            probability_multiplier[i] *= P

    # Inicializa a fila de prioridade e a probabilidade de sucesso do ponto de partida
    pq = [(-probability_multiplier[starting_point], starting_point, K - shooter_count[starting_point])]  # Usamos valores negativos para criar uma max-heap
    probability_success = [0.0] * (N + 1)
    probability_success[starting_point] = probability_multiplier[starting_point]

    while pq:
        probability, u, bullets = heapq.heappop(pq)
        probability = -probability  # Convertendo de volta para positivo

        # chegou ao ponto de destino
        if u == destination_point:
            return probability
        
        if probability < probability_success[u]:
            continue
        
        # olhando os vizinhos do ponto atual
        for v in roads[u]:
            if bullets - shooter_count[v] < 0:
                continue
            
            # probabilidade ao ir para o ponto vizinho
            new_prob = probability * probability_multiplier[v]
            if new_prob > probability_success[v]:
                probability_success[v] = new_prob
                heapq.heappush(pq, (-new_prob, v, bullets - shooter_count[v]))

    return 0.0  # Se não encontrar um caminho

def run():
    input = sys.stdin.read
    data = input().strip().split('\n')

    index = 0
    
    while index < len(data):
        if data[index].strip() == '':
            break
        
        # Lê N, M, K, P
        N, M, K, P = data[index].split()
        N, M, K = int(N), int(M), int(K)
        P = float(P)

        index += 1

        # Construção do grafo
        roads = defaultdict(list)
        for _ in range(M):
            i, j = map(int, data[index].split())
            roads[i].append(j)
            roads[j].append(i)
            index += 1

        # Lê o número de atiradores e suas posições
        A = int(data[index].split()[0])
        shooter_positions = list(map(int, data[index].split()[1:A+1]))

        index += 1

        # Lê o ponto de partida e destino
        starting_point, destination_point = map(int, data[index].split())
        index += 1

        probability_success_value = soldiers_probability_success_bfs(
            N=N,
            K=K,
            P=P,
            roads=roads,
            shooter_positions=shooter_positions,
            starting_point=starting_point,
            destination_point=destination_point
        )

        # O problema pede que a probabilidade seja mostrada com 3 casas decimais
        print("{:.3f}".format(probability_success_value))

if __name__ == "__main__":
    run()