import sys

data = list(map(int, sys.stdin.read().split()))
it = iter(data)
n = next(it); H = next(it)
bags = [next(it) for _ in range(n)]


if n > H:
    pass  

def ok(K: int) -> bool:
    total = 0
    for s in bags:
        total += (s + K - 1) // K  
        if total > H:              
            return False
    return total <= H

lo, hi = 1, max(bags)  
while lo < hi:
    mid = (lo + hi) // 2
    if ok(mid):
        hi = mid
    else:
        lo = mid + 1

print(lo)