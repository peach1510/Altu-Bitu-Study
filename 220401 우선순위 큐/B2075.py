import sys
import heapq
input = sys.stdin.readline

n = int(input())

table = []
heap = []
checked = [False] * n

for _ in range(n):
    table.append(list(map(int, input().split())))

for v in table[-1]:
    # 리스트 가장 마지막 값을 우선순위 큐에 추가
    heapq.heappush(heap, v)

# 역순으로 리스트 탐색
for t in reversed(table[:n-1]):
    for i in range(n):
        if checked[i]:
            continue
        pop_value = heapq.heappop(heap)
        # 값 비교 후 이번 값이 heap.pop() 값보다 크다면 추가
        if pop_value < t[i]:
            heapq.heappush(heap, t[i])
        else:
            heapq.heappush(heap, pop_value)
            # 현재 heap에 값이 들어갈 수 없다면 같은 열의 다른 수들도 못 들어가니 체크
            if pop_value > t[i]:
                checked[i] = True
    # 전부 체크되면 종료
    if all(checked):
        break

answer = heapq.heappop(heap)
print(answer)
