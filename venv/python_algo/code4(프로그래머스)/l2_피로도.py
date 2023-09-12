# ㅋㅋㅋㅋ 꼴에 겜돌이라고 설명이 게임식이니까
# 읽히는게 술술 읽혀버리네 ㅋㅋㅋ 어처구니가 없다 ㅋㅋ
# 아 왜 세상은 게임으로 돌아가지 않는건데~~
# 물론 게임식으로 된다고 해서 내가 잘나간다는 소리는 아니고 ㅋ

# 이게 정렬로 풀면 안될꺼 같고  BFS 로 완전 탐색 갈겨야할듯??
# 아 근데 나 BFS 너무 못하는거 같애
# 어차피 이거 길이가 8밖에 안되서 이런건 그냥 DFS 로 조지는게 더 편할듯

from collections import deque

def solution(k, dungeons):
    answer = 0
    d_len = len(dungeons)

    for i in range(d_len):
        if k < dungeons[i][0]: continue
        visited = [False] * d_len
        q = deque()
        q.append((i, k, 1, [*visited]))

        while q:
            x, hp, cnt, check = q.popleft()
            check[x] = True
            answer = max(answer, cnt)
            hp -= dungeons[x][1]
            for j in range(d_len):
                if check[j] or hp < dungeons[j][0]: continue
                q.append((j, hp, cnt + 1, [*check]))
    return answer

if __name__ == "__main__":
    k = 80
    dungeons = [[80,20],[50,40],[30,10]]
    res = 3
    answer = solution(k, dungeons)
    print(res == answer, answer)