# 시바
# 걍 666 부터 시작해서 1씩 더한 값을 string 으로 변환
# 그 값에서 666이 있으면 통과
# 그걸 카운터 해서 N 값과 같으면 해당 값을 출력

N = int(input())


def series (N):
    s_num = 666
    cnt = 0

    while(True):

        st_num = str(s_num)

        if "666" in st_num:
            cnt += 1

        if cnt == N:
            break

        s_num += 1

    return s_num

print(series(N))

