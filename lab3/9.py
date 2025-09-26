def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False


n = int(input())          
arr = list(map(int, input().split()))
x = int(input())          

if binary_search(arr, x):
    print("Yes")
else:
    print("No")