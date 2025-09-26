t = int(input())                      
targets = list(map(int, input().split()))  

n, m = map(int, input().split())       

matrix = []
pos = {}                              

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    for j in range(m):
        pos[row[j]] = (i, j)          

for x in targets:
    if x in pos:
        print(pos[x][0], pos[x][1])
    else:
        print(-1)