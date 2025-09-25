import sys

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def solve():
    n = int(sys.stdin.read().strip())

    primes = []
    num = 2
    while len(primes) < 2000:   
        if is_prime(num):
            primes.append(num)
        num += 1

    superprimes = []
    for i, p in enumerate(primes, start=1):
        if is_prime(i):  
            superprimes.append(p)

    print(superprimes[n-1])

if __name__ == "__main__":
    solve()