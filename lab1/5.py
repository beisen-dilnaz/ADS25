from collections import deque
import sys

def solve():
    data = sys.stdin.read().strip().split()
    boris = deque(map(int, data[:5]))
    nursik = deque(map(int, data[5:]))

    moves = 0
    MAX_MOVES = 10**6

    while boris and nursik and moves < MAX_MOVES:
        moves += 1
        b = boris.popleft()
        n = nursik.popleft()

        if (b == 0 and n == 9) or (b > n and not (b == 9 and n == 0)):
            # Boris wins
            boris.append(b)
            boris.append(n)
        else:
            # Nursik wins
            nursik.append(b)
            nursik.append(n)

    if moves >= MAX_MOVES:
        print("blin nichya")
    elif not boris:
        print("Nursik", moves)
    else:
        print("Boris", moves)

if __name__ == "__main__":
    solve()