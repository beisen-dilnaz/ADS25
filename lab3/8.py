import sys
import bisect

def main():
    input = sys.stdin.read
    data = input().split()
    
    N, M = int(data[0]), int(data[1])
    a = list(map(int, data[2:2+N]))
    mistakes = list(map(int, data[2+N:]))
    
    prefix = []
    total = 0
    for x in a:
        total += x
        prefix.append(total)
    
    for b in mistakes:
        block = bisect.bisect_left(prefix, b) + 1  
        print(block)

if __name__ == "__main__":
    main()