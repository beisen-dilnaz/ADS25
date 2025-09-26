import sys
import math

def can_deliver(c, f, cap):
    flights = 0
    for x in c:
        flights += (x + cap - 1) // cap 
        if flights > f:  
            return False
    return flights <= f

def main():
    n, f = map(int, sys.stdin.readline().split())
    c = list(map(int, sys.stdin.readline().split()))
    
    low, high = 1, max(c)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if can_deliver(c, f, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)

if __name__ == "__main__":
    main()