import sys

def run():
    input = sys.stdin.read
    data = input().strip().split('\n')

    index = 0
    while index < len(data):
        if data[index].strip() == '':
            break

if __name__ == "__main__":
    run()