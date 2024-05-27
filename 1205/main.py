import sys
from collections import defaultdict

def soldiers_probability_success(
        N:int, 
        M:int, 
        K:int, 
        P:float, 
        roads:defaultdict[any, list], 
        shooter_positions:list[int], 
        starting_point:int, 
        destination_point:int
    ) -> float:

    return 1.000

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

        probability_success_value = soldiers_probability_success

        # resultado com três casas decimais
        print("{:.3f}".format(probability_success_value))

if __name__ == "__main__":
    run()