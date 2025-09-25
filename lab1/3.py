import sys

def process(s: str) -> str:
    stack = []
    for ch in s:
        if ch == '#':
            if stack:
                stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)

def solve():
    s1, s2 = sys.stdin.read().split()
    if process(s1) == process(s2):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()