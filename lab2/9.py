from collections import deque

t = int(input())   

for _ in range(t):
    n = int(input())        
    chars = input().split() 
    
    q = deque()             
    freq = {}               
    
    result = []
    
    for ch in chars:
        
        freq[ch] = freq.get(ch, 0) + 1
        q.append(ch)
        
        while q and freq[q[0]] > 1:
            q.popleft()
        
        if q:
            result.append(q[0])
        else:
            result.append("-1")
    
    print(" ".join(result))