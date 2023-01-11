def dfs(v):
    # 방문처리
    visited1[v] = 1
    print(v, end=' ')
    # for문으로 if graph[v][i]로 v와 연결된 노드를 찾고 재귀함수로 반복.
    for i in range(1, n + 1):
        if graph[v][i] == 1 and visited1[i] == 0:
            dfs(i)


def bfs(v):
    # 큐에 탐색 노드 넣기
    queue = [v]
    # 방문처리
    visited2[v] = 1
    # queue에 값이 없을 때까지(탐색이 끝날 때까지) 반복
    while queue:
        # queue는 FIFO 구조이므로 0번째 요소부터 빼고, 삭제한 요소를 v변수로 돌려받음
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, n + 1):
            if graph[v][i] == 1 and visited2[i] == 0:
                queue.append(i)
                visited2[i] = 1


n, m, v = map(int, input().split())

# 행렬 만들기
graph = [[0] * (n + 1) for _ in range(n + 1)]
# 정점 개수만큼의 행렬을 만들고 정점 간 연결을 행렬에 표시
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 방문 리스트 행렬
visited1 = [0] * (n + 1)
visited2 = visited1.copy()

dfs(v)
print()
bfs(v)
