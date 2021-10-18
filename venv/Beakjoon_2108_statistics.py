# 통계학
## 파이파이3 로 돌려야 시초 안뜸 ㅅㅂ

def statistics (N, num_list):
    num_list.sort()

    # 산술 평균
    avg = round(sum(num_list)/N)

    # 중앙값
    mid = len(num_list)//2
    median = num_list[mid]

    # 최빈값
    mode = Counting(num_list, max(num_list))

    # 범위
    max_num = max(num_list)
    min_num = min(num_list)
    range_num = max_num - min_num


    return avg, median, mode, range_num


def Counting(arr, max_num):
    cnt_dic = {}


    for i in range(len(arr)):
        cnt = 1
        if arr[i] not in cnt_dic:
            for j in range(i+1,len(arr)):
                if arr[i] == arr[j]:
                    cnt += 1

            cnt_dic[arr[i]] = cnt
    #print(cnt_dic)


    max_val = max(cnt_dic.values())
    mode_list = []
    for key, val in cnt_dic.items():
        if val == max_val:
            mode_list.append(key)

    #print('최빈값 애들만',mode_list)

    if len(mode_list) >= 2:
        mode_num = mode_list[1]
    else:
        mode_num = mode_list[0]

    return mode_num



N = int(input())

num_list = []

for i in range(N):
    num_list.append(int(input()))

ans = statistics(N, num_list)

for i in ans:
    print(i)
