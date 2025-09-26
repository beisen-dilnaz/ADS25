n, k = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
current_sum = 0
min_len = n + 1

for right in range(n):
    current_sum += arr[right]
    
    while current_sum >= k:
        min_len = min(min_len, right - left + 1)
        current_sum -= arr[left]
        left += 1

print(min_len)