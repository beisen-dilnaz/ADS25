import sys

def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n = data[0]
    ages = data[1:]

    ans = [-1] * n
    stack = []  

    for i in range(n):
        while stack and stack[-1][1] > ages[i]:  
            stack.pop()
        if stack:
            ans[i] = stack[-1][1]
        stack.append((i, ages[i]))

    sys.stdout.write(" ".join(map(str, ans)) + "\n")

if __name__ == "__main__":
    solve()