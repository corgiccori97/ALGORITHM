import sys
from collections import deque
input = sys.stdin.readline
# 파이썬에서 queue 쓸 땐 반드시 deque 사용할 것 !
## queue는 한 쪽으로만 입력, 반대쪽으로만 출력
## deque는 양쪽으로 입출력 가능
def bfs():
    q = deque()
    # 출발점 deque에 입력
    q.append(n)
    while q:
        # 가장 왼쪽 값을 pop한 다음 x에 저장
        x = q.popleft()
        # x값이 동생이 있는 위치인 k일 시 visited[x] 출력 후 종료
        if x == k:
            print(visited[x])
            break
        for i in (x - 1, x + 1, x * 2):
            # 0 <= i < max_num 했는데 틀렸다..
            if 0 <= i <= max_num and not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)
    
n, k = map(int, input().split())
max_num = 100000
visited = [0] * (max_num + 1)

bfs()