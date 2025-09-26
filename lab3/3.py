def solve():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(q):
        l1, r1, l2, r2 = map(int, input().split())
        count = 0
        for x in arr:
            if (l1 <= x <= r1) or (l2 <= x <= r2):
                count += 1
        print(count)

if __name__ == "__main__":
    solve()