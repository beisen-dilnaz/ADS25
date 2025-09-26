n, k = map(int, input().split())
words = input().split()

k = k % n
shifted = words[k:] + words[:k]

print(" ".join(shifted))