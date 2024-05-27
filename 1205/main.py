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

    # numeros de atirados em cada um dos pontos estratégicos
    shooter_count = [0] * (N + 1)
    for position in shooter_positions: # conta a partir da posição
        shooter_count[position] += 1

    probability_success = [0.0] * (N + 1)
    probability_success[starting_point] = math.pow(P,shooter_count[starting_point]) # probabilidade de sucesso do ponto de partida é a probabilidade de matar os atiradores presentes naquele ponto

    # fila para bfs
    queue = [(starting_point, K)]

    # probabilidades de sucesso em cada ponto estratégico
    while queue:
        current_point, bullets = queue.pop(0)
        for neighbor in roads[current_point]:
            if bullets > 0:
                # probabilidade de sucesso para ir até o vizinho atual
                neighbor_probability = probability_success[current_point] * math.pow(P,shooter_count[neighbor])
                if neighbor_probability > probability_success[neighbor]:
                    probability_success[neighbor] = neighbor_probability
                    queue.append((neighbor,bullets - 1)) # explora os vizinhos, já que conseguiu diminui balas

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