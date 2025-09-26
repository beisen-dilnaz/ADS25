import bisect

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, q = int(data[0]), int(data[1])
    arr = list(map(int, data[2:2+n]))
    
    queries = []
    idx = 2 + n
    for _ in range(q):
        l1, r1, l2, r2 = map(int, data[idx:idx+4])
        queries.append((l1, r1, l2, r2))
        idx += 4
    
    arr.sort()
    
    def count_in_range(L, R):
       
        return bisect.bisect_right(arr, R) - bisect.bisect_left(arr, L)
    
    results = []
    for l1, r1, l2, r2 in queries:
        cnt1 = count_in_range(l1, r1)
        cnt2 = count_in_range(l2, r2)
        
        
        ol = max(l1, l2)
        orr = min(r1, r2)
        cnt_overlap = 0
        if ol <= orr:
            cnt_overlap = count_in_range(ol, orr)
        
        results.append(cnt1 + cnt2 - cnt_overlap)
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    solve()