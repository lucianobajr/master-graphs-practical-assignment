import sys


def solve(m: int, n: int, queries: list):
    MAXC = 26

    f = [[0] * MAXC for _ in range(MAXC)]
    for i in range(MAXC):
        f[i][i] = 1

    for _ in range(m):
        s1, s2 = queries.pop(0).split()
        f[ord(s1[0]) - ord('a')][ord(s2[0]) - ord('a')] = 1

    for k in range(MAXC):
        for i in range(MAXC):
            for j in range(MAXC):
                f[i][j] |= f[i][k] & f[k][j]

    results = []
    for _ in range(n):
        s1, s2 = queries.pop(0).split()
        valid = len(s1) == len(s2)
        for i in range(len(s1)):
            if i >= len(s2):  # Verifica se o índice está dentro dos limites da segunda palavra
                valid = False
                break
            valid &= f[ord(s1[i]) - ord('a')][ord(s2[i]) - ord('a')]
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
            if index >= len(input_data):  # Verifica se ainda há linhas disponíveis
                break
            queries.append(input_data[index])
            index += 1

        results = solve(m=m, n=n, queries=queries)
        print('\n'.join(results))


if __name__ == "__main__":
    run()