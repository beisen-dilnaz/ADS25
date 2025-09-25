import sys
import math

def solve():
    a = int(sys.stdin.read().strip())
    if a < 2:
        print("NO")
        return
    
    for i in range(2, int(math.isqrt(a)) + 1):
        if a % i == 0:
            print("NO")
            return
    
    print("YES")

if __name__ == "__main__":
    solve()