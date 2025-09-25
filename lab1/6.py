import sys

def solve():
    n = int(sys.stdin.read().strip())

    limit = 9000
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    primes = []
    for i in range(2, limit + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
        if len(primes) >= n:
            break

    print(primes[n - 1])

if __name__ == "__main__":
    solve()