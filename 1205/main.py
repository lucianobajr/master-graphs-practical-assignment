import sys
import math
from collections import defaultdict

def soldiers_probability_success_bfs(
        N:int, # números de pontos estratégicos
        K:int, # balas carregadas pelo soldado soviético
        P:float, # probabilidade do soldado matar um atirador
        roads:defaultdict[any, list], # par indicando existência de uma estrada ligando o ponto i ao j
        shooter_positions:list[int],  # posição de cada atirador
        starting_point:int, # ponto de partida de cada soldado
        destination_point:int # ponto de destino de cada soldado
    ) -> float:

    shooters = [0] * (N + 1)
    for position in shooter_positions:
        shooters[position] += 1

    probability_success = [0.0] * (N + 1)
    probability_success[starting_point] = math.pow(P,shooters[starting_point])

    queue = [(starting_point, K)]

    while queue:
        current_point, bullets = queue.pop(0)
        for neighbor in roads[current_point]:
            if bullets > 0:
                neighbor_probability = probability_success[current_point] * math.pow(P,shooters[neighbor])
                if neighbor_probability > probability_success[neighbor]:
                    probability_success[neighbor] = neighbor_probability
                    queue.append((neighbor,bullets - 1))

    return probability_success[destination_point]

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
        shooter_positions = list(map(int, data[index].split()[1:]))
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

        # resultado com três casas decimais
        print("{:.3f}".format(probability_success_value))

if __name__ == "__main__":
    run()