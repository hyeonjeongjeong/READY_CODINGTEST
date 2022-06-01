from collections import deque

def bfs(a, b, n):
    visited = [[False] * N for _ in range(N)]
    queue = deque([(a, b, 0)])
    visited[a][b] = True
    
    while queue:
        y, x, cnt = queue.popleft()
        if y == a2 and x == b2:
            return cnt
        
        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx, cnt + 1))
            
    else:
        return -1
    
    
N = int(input())
a1, b1, a2, b2 = map(int, input().split())
directions = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
print(bfs(a1, b1, 0))