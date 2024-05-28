import sys

def floyd_warshall(m:int, n:int, queries:list):
    MAXC = 26 # alfabeto

    translation_matrix = [[0] * MAXC for _ in range(MAXC)]
    for i in range(MAXC):
        translation_matrix[i][i] = 1
    
    for _ in range(m):
        from_char, to_char = queries.pop(0).split()
        translation_matrix[ord(from_char[0]) - ord('a')][ord(to_char[0]) - ord('a')] = 1
    
    # computar o fecho transitivo
    for k in range(MAXC):
        for i in range(MAXC):
            for j in range(MAXC):
                translation_matrix[i][j] |= translation_matrix[i][k] & translation_matrix[k][j]
    
    # Verificando se os pares de palavras correspondem após as traduções
    results = []
    for _ in range(n):
        from_char, to_char = queries.pop(0).split()
        valid = len(from_char) == len(to_char)
        for i in range(len(from_char)):
            valid &= translation_matrix[ord(from_char[i]) - ord('a')][ord(to_char[i]) - ord('a')]
        results.append("yes" if valid else "no")
    
    return results

def run():
    input_data = sys.stdin.read().strip().split('\n')

    index = 0
    while index < len(input_data):
        if input_data[index].strip() == '':
            break
        
        # m -> número de traduções de letras
        # n -> número de pares de palavras
        m, n = map(int, input_data[index].split())
        index += 1

        queries = []
        for _ in range(m + n):
            queries.append(input_data[index])
            index += 1
        
        results = floyd_warshall(m=m, n=n, queries=queries)
        print('\n'.join(results))

if __name__ == "__main__":
    run()