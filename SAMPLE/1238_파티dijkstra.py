import sys
input = sys.stdin.readline

# 그래프에 가중치가 없을 떈 BFS
# 가중치가 다르고 음수간선이 없을 때는(0보다 작은 값을 가지는 간선이 없을 때) 다익스트라

# 다익스트라: 매번 가장 비용이 적은 노드를 선택하여 과정을 반복하므로 기본적으로 그리디 알고리즘으로 분류

# 원리
# 1. 출발 노드 설정
# 2. 최단 거리 테이블 초기화
# 3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용 계산하여 최단 거리 테이블 갱신
# 5. 3, 4번 과정 반복

# 다익스트라 알고리즘의 기본 구성은 아래와 같습니다.

# 1. 각 정점까지의 최단 거리를 배열하는 dist[]를 만듭니다. 맨 처음에는 시작점을 제외한 최단경로를 알지 못하므로, 시작점은 0, 나머지는 그래프에서의 거리로 나오지 않을 충분히 큰 값으로 초기화 합니다.
# 2. BFS에서는 큐에 정점의 번호를 넣었지만, 다익스트라 알고리즘에서는 정점의 번호와, 해당 정점까지의 최단거리를 한 쌍으로 넣습니다. 물론 큐는 우선순위 큐 입니다.
# 3. BFS 처럼 반복문을 돌면서, 큐에서 원소 하나를 꺼내서, 간선으로 연결된 다른 정점들을 검사합니다. dist[]를 참고해서, 이때까지 알고 있던 해당 정점까지의 최단경로보다, 현재 검사중인 정점까지의 최단거리 + 간선의 가중치가 더 작다면, dist[]를 갱신합니다. 그리고, BFS 처럼 해당 정점의 이름과 거리를 큐에다가 넣습니다. 기존까지 알고있던 값보다 더 짧은 경로를 찾지 못했다면, 굳이 큐에 넣을 필요는 없죠.

import heapq


def dijkstra(s):
    D = [float('inf')] * (N + 1)
    D[s] = 0
    q = []
    # heap에 (가중치, 노드) 형식 삽입
    heapq.heappush(q, (0, s))
    
    while q:
        dist, now = heapq.heappop(q)
        if D[now] >= dist:
            for v, val in graph[now]:
                if dist + val < D[v]:
                    D[v] = dist + val
                    heapq.heappush(q, (dist + val, v))
    
    return D

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    first, last, time = map(int, input().split())
    graph[first].append([last, time])

result = dijkstra(X)
result[0] = 0
for i in range(1, N + 1):
    if i != X:
        res = dijkstra(i)
        result[i] += res[X]
    
print(max(result))