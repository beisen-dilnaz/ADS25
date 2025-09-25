from collections import deque
import sys

dq = deque()

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    if line[0] == '+':
        dq.appendleft(int(line.split()[1]))
    elif line[0] == '-':
        dq.append(int(line.split()[1]))
    elif line[0] == '*':
        if not dq:
            print("error")
        elif len(dq) == 1:
            x = dq.pop()
            print(x * 2)
        else:
            a = dq.popleft()
            b = dq.pop()
            print(a + b)
    elif line[0] == '!':
        break