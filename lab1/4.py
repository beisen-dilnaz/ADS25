import sys

def solve():
    s = sys.stdin.read().strip()
    stack = []
    
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()   
        else:
            stack.append(ch)
    
    if not stack:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()