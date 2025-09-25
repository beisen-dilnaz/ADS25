import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    s = data[1]

    qS = deque()
    qK = deque()

    for i, ch in enumerate(s):
        if ch == 'S':
            qS.append(i)
        else:
            qK.append(i)

    while qS and qK:
        s_idx = qS.popleft()
        k_idx = qK.popleft()
        if s_idx < k_idx:
            qS.append(s_idx + n)  # Sakayanagi wins this round
        else:
            qK.append(k_idx + n)  # Katsuragi wins this round

    if qS:
        print("SAKAYANAGI")
    else:
        print("KATSURAGI")

if __name__ == "__main__":
    solve()