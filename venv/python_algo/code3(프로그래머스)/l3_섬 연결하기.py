# Kruskal 알고리즘 를 사용해야하는데
# https://soohyun6879.tistory.com/145
# 탐욕적인 방법을 이용하여 네트워크(가중치를 간선에 할당한 그래프)의 모든 정점을 최소 비용으로 연결하는 최적 해답을 구하는 것
# Kruskal 알고리즘의 동작
# 
# 그래프의 간선들을 가중치의 오름차순으로 정렬한다.
# 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택한다.
# 즉, 가장 낮은 가중치를 먼저 선택한다. 사이클을 형성하는 간선을 제외한다. 해당 간선을 현재의 MST(최소 비용 신장 트리)의 집합에 추가한다.

# 이라는 소린데 그냥 가장 낮은 비용으로 sort 한 다음
# 연결 조지라는 소리임 이러면 그대로 N 만큼 밖에 안돌음
# 별거 아니긴 한데 잘 이해가 안 가는게
# 분명히 v[0], v[1] 모두 link 셋에 들어가 있다면 넘어가고
# v[0] 가 들어가 있거나 or v[1] 가 들어가 있거나 로 if 절로 한번 더 거르는데
# 이것을 구지 하는 이유가 뭐지??
# 그니까 아예 외딴섬 같은 경로를 배제하려고 하는건가 결국은 모두 연결해서 이동을 해야하니까?
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    link = set([costs[0][0]])
    while len(link) != n:
        for v in costs:
            if v[0] in link and v[1] in link:
                continue
            if v[0] in link or v[1] in link:
                link.update([v[0], v[1]])
                answer += v[2]
                break

    return answer

if __name__ == "__main__":
    n = 4
    costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    res = 4
    ans = solution(n, costs)
    print(res == ans)