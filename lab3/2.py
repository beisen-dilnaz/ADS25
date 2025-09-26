def can_divide(arr, k, max_sum):
    blocks, curr = 1, 0
    for x in arr:
        if curr + x > max_sum:
            blocks += 1
            curr = x
            if blocks > k:
                return False
        else:
            curr += x
    return True

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    low, high = max(arr), sum(arr)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if can_divide(arr, k, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    print(ans)

if __name__ == "__main__":
    solve()