from collections import deque
import sys

def solve():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    out_lines = []

    for _ in range(t):
        n = int(data[idx]); idx += 1
        dq = deque()
        for i in range(n, 0, -1):
            dq.appendleft(i)               
            dq.rotate(i % len(dq))         
        out_lines.append(" ".join(map(str, dq)))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()