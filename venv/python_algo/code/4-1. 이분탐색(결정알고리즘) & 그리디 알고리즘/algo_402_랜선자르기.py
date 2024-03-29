# 랜선자르기(결정알고리즘)
# K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다. 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에
# K개의 랜선을 잘라서 만들어야 한다. 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면
# 20cm 은 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)
# 랜선을 자를때 손실되는 길이는 없다고 가정, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정.
# 그리고 자를 때는 항상 센티미터 단위로 정수 길이만큼 자른다고 가정.
#
# N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때
# 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.
#
# ▣ 입력설명
# 첫째 줄에는 엘리트학원이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이
# 입력된다. K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고
# 항상 K ≦ N 이다. 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의
# 
#   이하의 자연수로 주어진다.
# ▣ 출력설명
# 첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.
# ▣ 입력예제 1
# 4 11
# 802
# 743
# 457
# 539
# ▣ 출력예제 1
# 200
#
# 예제설명) 802cm 랜선에서 4개, 743cm 랜선에서 3개, 457cm 랜선에서 2개, 539cm 랜선에서 2개를
# 잘라내 모두 11개를 만들 수 있다.

def Counter (mid):
    cnt = 0
    for i in lan:
        cnt += i // mid
    return cnt

def LanCutFunc(k,n,lan):
    start_num = 1
    end_num = max(lan)
    res = 1

    while start_num <=  end_num:
        mid = (start_num + end_num) // 2
        cnt = Counter(mid)

        if cnt < n:
            end_num = mid-1
        else :
            start_num = mid+1
            res = mid


    return res


K, N = map(int, input().split())

lanList = []
for _ in range (K):
    lanList.append(int(input()))

ans = LanCutFunc(K, N, lanList)
print(ans)