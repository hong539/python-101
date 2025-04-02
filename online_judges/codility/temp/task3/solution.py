# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# DFS
# def solution(plan):
#     R, C = len(plan), len(plan[0])
#     visited = [[False]*C for _ in range(R)]

#     def dfs(x, y):
#         visited[x][y] = True
#         for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
#             nx, ny = x+dx, y+dy
#             if 0 <= nx < R and 0 <= ny < C:
#                 if not visited[nx][ny] and plan[nx][ny] in ('.', '*'):
#                     dfs(nx, ny)

#     count = 0
#     for i in range(R):
#         for j in range(C):
#             if plan[i][j] == '*' and not visited[i][j]:
#                 dfs(i, j)
#                 count += 1
#     return count

# DFS（Depth-First Search）= 深度優先搜尋

def solution(plan):
    rows = len(plan)
    cols = len(plan[0])

    visited = []
    for i in range(rows):
        row_flags = [False] * cols
        visited.append(row_flags)

    robot_runs = 0
    for i in range(rows):
        for j in range(cols):
            if plan[i][j] == '*' and not visited[i][j]:
                print(f"\n🦾 Robot run #{robot_runs} starts at ({i},{j})")
                dfs(plan, visited, i, j)
                robot_runs += 1

    return robot_runs                



def dfs(plan, visited, x, y):
    rows = len(plan)
    cols = len(plan[0])
    visited[x][y] = True
    print(f"🧹 Cleaning ({x},{y})")
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if not visited[nx][ny] and plan[nx][ny] in ('.', '*'):
                dfs(plan, visited, nx, ny)

# PEP8
# from typing import List


# def solution(plan: List[str]) -> int:
#     rows = len(plan)
#     cols = len(plan[0])
#     visited = []
#     for _ in range(rows):
#         row = [False] * cols
#         visited.append(row)

#     robot_runs = 0
#     for i in range(rows):
#         for j in range(cols):
#             if plan[i][j] == '*' and not visited[i][j]:
#                 dfs(plan, visited, i, j)
#                 robot_runs += 1

#     return robot_runs


# def dfs(plan: List[str], visited: List[List[bool]], x: int, y: int) -> None:
#     rows = len(plan)
#     cols = len(plan[0])
#     visited[x][y] = True

#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     for dx, dy in directions:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < rows and 0 <= ny < cols:
#             if not visited[nx][ny] and plan[nx][ny] in ('.', '*'):
#                 dfs(plan, visited, nx, ny)


# BFS
# from collections import deque

# def solution(plan):
#     R, C = len(plan), len(plan[0])
#     visited = [[False for _ in range(C)] for _ in range(R)]
    
#     def bfs(r, c):
#         queue = deque([(r, c)])
#         visited[r][c] = True
#         while queue:
#             x, y = queue.popleft()
#             for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < R and 0 <= ny < C:
#                     if not visited[nx][ny] and plan[nx][ny] in ['.', '*']:
#                         visited[nx][ny] = True
#                         queue.append((nx, ny))

#     robot_runs = 0
#     for i in range(R):
#         for j in range(C):
#             if plan[i][j] == '*' and not visited[i][j]:
#                 bfs(i, j)
#                 robot_runs += 1

#     return robot_runs

if __name__ == "__main__":
    # solution(['.*#..*', '.*#*.#', '######', '.*..#.', '...###'])
    # solution(['*#..', '#..#', '.##.', '...*'])
    # solution(['**###**', '*#*#*#*', '##*#*##', '*#***#*', '.#####.', '..*#*..'])
    
    plan = ['.*#..*', '.*#*.#', '######', '.*..#.', '...###']
    total_runs = solution(plan)
    print(f"\n✅ Total robot runs needed: {total_runs}")