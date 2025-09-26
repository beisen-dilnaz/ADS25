n = int(input())
arr = list(map(int, input().split()))

freq = {}
for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

max_count = max(freq.values())

modes = [num for num, cnt in freq.items() if cnt == max_count]
modes.sort(reverse=True)

print(" ".join(map(str, modes)))