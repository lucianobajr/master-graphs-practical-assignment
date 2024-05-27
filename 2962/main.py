import sys

def solver():
    return "S"

def run():
    
    input = sys.stdin.read
    data = input().strip().split('\n')

    index = 0
    while index < len(data):
        if data[index].strip() == '':
            break
        
        M,N,K = int(data[index].split())

        index += 1
        for _ in range(K):
            X, Y , S = int(data[index].split())
            index += 1

if __name__ == "__main__":
    run()