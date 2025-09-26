n, k = map(int, input().split())
limits = []

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    limits.append(max(x2, y2))

limits.sort()
print(limits[k-1])