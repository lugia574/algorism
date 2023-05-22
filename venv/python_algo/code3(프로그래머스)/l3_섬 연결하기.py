
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