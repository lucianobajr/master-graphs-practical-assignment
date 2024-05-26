import sys

def run():
    input = sys.stdin.read
    data = input().strip().split('\n')

    index = 0
    
    while True:
        N,M,K,P = map(float, data[index].split())
        index += 1

        for _ in range(int(M)):
            i, j = data[index].split() # idiomas de origem e destino
            index += 1

        # numero de atiradores
        A = int(data[index].split()[0])

        # posições dos atiradores
        shooter_positions = list(map(int, data[index].split()[1:]))
        
        index += 1

        starting_point, destination_point = map(int,data[index].split())
        index += 1
        print(starting_point,destination_point)

if __name__ == "__main__":
    run()