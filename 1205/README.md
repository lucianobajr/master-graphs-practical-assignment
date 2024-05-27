# Cerco a Leningrado - 1285

## Descrição

A cidade de São Petersburgo mudou de nome depois da revolção russa em 1914 para Petrogrado. Após a morte de Lênin, em homenagem ao grande líder o nome da cidade mudou novamente para Leningrado em 1924, e assim permaneceu até o fim da União Soviética. Em 1991, a cidade voltou a ter o nome antigo. Durante a segunda guerra mundial a cidade de Leningrado sofreu um cerco das tropas alemãs que durou cerca de 900 dias. Foi uma época terrível, de muita fome e perdas humanas, que terminou em 27 de janeiro de 1944 com a vitória dos soviéticos. É considerada uma das vitórias mais custosas da história em termos de vidas humanas perdidas.

No auge da ofensiva alemã, no ano de 1942, vários atiradores de elite foram espalhados pela cidade, inclusive, em alguns pontos estratégicos da cidade mais de um atirador aguardavam soldados inimigos. A espionagem russa tinha informações detalhadas das habilidades desses atiradores, mas seus esconderijos eram excelentes, tornando a tarefa de um soldado soviético que desejasse cruzar a cidade extremamente difícil. Os soldados soviéticos eram bem treinados, mas com o passar do tempo e a continuação do cerco à cidade, os melhores soldados foram sendo dizimados, uma vez que se errassem o alvo na primeira tentativa certamente eram mortos pelos soldados alemães na tocaia.

Sabendo a probabilidade de um soldado em matar um atirador alemão e sabendo também o número de balas que ele tinha à sua disposição, desejamos saber a probabilidade desse soldado conseguir chegar a um ponto estratégico de destino, partindo de um ponto estratégico de origem. O soldado, sendo muito experiente, sempre usava um caminho que maximizava a probabilidade de sucesso. Note que o soldado deve matar todos os atiradores presentes no caminho usado, inclusive os que estiverem nos pontos estratégicos de origem e destino.

## Entrada
A entrada é composta por diversas instâncias e termina com final de arquivo (EOF). A primeira linha de cada instância contém 3 inteiros, N (2 ≤ N ≤ 1000), M, e K (0 ≤ K ≤ 1000) e a probabilidade P (0 ≤ P ≤ 1) do soldado matar um atirador. Os inteiros N, M, e K representam respectivamente os números de pontos estratégicos, estradas ligando pontos estratégicos e balas carregadas pelo soldado soviético. Os pontos estratégicos são numerados de 1 a N.

Cada uma das próximas M linhas contém um par de inteiros i e j indicando que existe uma estrada ligando o ponto i ao j. Em seguida tem uma linha contendo um inteiro A (0 ≤ A ≤ 2000), correspondendo ao número de atiradores na cidade, seguido por A inteiros indicando a posição de cada atirador. A última linha de cada instância contém dois inteiros indicando o ponto de partida e o destino do soldado.

## Saída
Para cada instância imprima uma linha contendo a probabilidade de sucesso do soldado soviético. A probabilidade deve ser impressa com 3 casas decimais.

----------------------------------------------------------------------------------------------------------------------------

## Documentação para o Projeto "Cerco a Leningrado"

### Descrição do Problema

A cidade de Leningrado, atual São Petersburgo, sofreu um cerco prolongado durante a Segunda Guerra Mundial. Durante o auge da ofensiva alemã em 1942, atiradores de elite foram posicionados em pontos estratégicos da cidade. Os soldados soviéticos, precisando cruzar a cidade, enfrentavam o desafio de evitar ou eliminar esses atiradores. Nosso objetivo é determinar a probabilidade de um soldado soviético chegar de um ponto estratégico de origem a um ponto estratégico de destino, dado o número de balas que ele possui e a probabilidade de matar um atirador.

### Explicação do Código

O código é escrito em Python e resolve o problema utilizando uma abordagem de Busca em Largura com Fila de Prioridade (BFS com Priority Queue), que é eficiente para encontrar o caminho de maior probabilidade de sucesso em um grafo. 

#### Importações e Definições

```python
import sys
from collections import defaultdict
import heapq
```

- `sys`: Para leitura de entrada padrão.
- `defaultdict` e `heapq`: Para a estrutura de dados necessária para o grafo e a fila de prioridade, respectivamente.

#### Função `soldiers_probability_success_bfs`

Esta função calcula a probabilidade de sucesso do soldado em chegar ao destino.

```python
def soldiers_probability_success_bfs(
        N: int,  # número de pontos estratégicos
        K: int,  # balas carregadas pelo soldado soviético
        P: float,  # probabilidade do soldado matar um atirador
        roads: defaultdict[any, list],  # dicionário representando as estradas entre os pontos
        shooter_positions: list[int],  # lista das posições dos atiradores
        starting_point: int,  # ponto de partida do soldado
        destination_point: int  # ponto de destino do soldado
    ) -> float:
```

**1. Inicialização do Contador de Atiradores**

```python
    shooter_count = [0] * (N + 1)
    for position in shooter_positions:
        shooter_count[position] += 1
```
- Conta quantos atiradores estão presentes em cada ponto estratégico.

**2. Cálculo da Probabilidade Acumulada**

```python
    probability_multiplier = [1.0] * (N + 1)
    for i in range(1, N + 1):
        for _ in range(shooter_count[i]):
            probability_multiplier[i] *= P
```
- Calcula a probabilidade acumulada de sucesso em cada ponto estratégico, levando em consideração a probabilidade de matar todos os atiradores presentes naquele ponto.

**3. Inicialização da Fila de Prioridade (Max-Heap)**

```python
    pq = [(-probability_multiplier[starting_point], starting_point, K - shooter_count[starting_point])]
    probability_success = [0.0] * (N + 1)
    probability_success[starting_point] = probability_multiplier[starting_point]
```
- Usa valores negativos na fila de prioridade para criar um Max-Heap, o que facilita a extração do valor máximo.

**4. Loop Principal da BFS com Priority Queue**

```python
    while pq:
        probability, u, bullets = heapq.heappop(pq)
        probability = -probability  # Convertendo de volta para positivo

        if u == destination_point:
            return probability

        if probability < probability_success[u]:
            continue

        for v in roads[u]:
            if bullets - shooter_count[v] < 0:
                continue

            new_prob = probability * probability_multiplier[v]
            if new_prob > probability_success[v]:
                probability_success[v] = new_prob
                heapq.heappush(pq, (-new_prob, v, bullets - shooter_count[v]))

    return 0.0
```
- Processa a fila de prioridade, explorando os vizinhos e atualizando as probabilidades de sucesso.
- Verifica se há balas suficientes para eliminar os atiradores no próximo ponto antes de atualizar a probabilidade e inserir na fila.

#### Função `run`

```python
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
```

- **Leitura de Entrada**: Lê e processa os dados de entrada.
- **Construção do Grafo**: Constrói o grafo com as estradas entre pontos estratégicos.
- **Leitura dos Atiradores e Pontos de Partida/Destino**: Lê as posições dos atiradores e os pontos de partida e destino.
- **Chamada para `soldiers_probability_success_bfs`**: Calcula a probabilidade de sucesso e imprime o resultado formatado com 3 casas decimais.

### Max-Heap Explicação

No contexto de nosso código, usamos um Max-Heap para garantir que exploramos sempre o caminho com a maior probabilidade de sucesso. Em Python, `heapq` fornece uma implementação de Min-Heap por padrão, então usamos valores negativos para simular um Max-Heap. Isso é crucial para nosso algoritmo, pois queremos sempre explorar o caminho mais promissor primeiro.

### Conclusão

Este código busca resolver o problema de determinar a probabilidade de sucesso de um soldado soviético atravessar uma cidade cheia de atiradores, utilizando um algoritmo eficiente baseado em BFS com uma fila de prioridade (Max-Heap). Ele é projetado para lidar com grandes conjuntos de dados e encontrar o caminho mais seguro com base nas balas disponíveis e nas probabilidades de eliminar atiradores.