import sys
input = sys.stdin.read
data = list(map(int, input().split()))

n = data[0]
arr = data[1:1+n]
p = data[1+n]
queries = data[2+n:]

freq = [0] * 1001
for x in arr:
    freq[x] += 1

prefix_count = [0] * 1001
prefix_sum = [0] * 1001
for i in range(1, 1001):
    prefix_count[i] = prefix_count[i-1] + freq[i]
    prefix_sum[i] = prefix_sum[i-1] + freq[i] * i

out = []
for q in queries:
    out.append(f"{prefix_count[q]} {prefix_sum[q]}")

print("\n".join(out))