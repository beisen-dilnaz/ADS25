n = int(input())
arr = list(map(int, input().split()))
k = int(input())

ans = 0
diff = abs(arr[0] - k)

for i in range(1, n):
    d = abs(arr[i] - k)
    if d < diff:
        diff = d
        ans = i

print(ans)