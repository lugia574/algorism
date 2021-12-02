# N명의 사람들이 있고
# 각 사람당 1번 부터 번호를 붙여 구별한다
# 친구의 친구가 되는 사람이 가장 많은 경우를 찾아 그 친구의 친구 수를 구하라
# 단, 본인을 제외하며, 바로 친구였던 경우도 제외

# 샘플
# 7
# 3 7 5 6 1 5 2 7 4 2 5 4 1 2 3 6 7 1 3 4 2 5 1 4

# 25
# 21 2 8 3 19 4 9 22 23 15 14 17 22 19 3 23 18 1 1 15 12 21 22 7 6 21 17 18 7 17 21 10 10 15 1 6 5 11 8 14 7 10 14 10 2 25 6 11 12 1 22 21 4 1 14 22 7 24 7 8 13 19 18 23 22 24 23 19 3 17


## 이거 이상함 뭔가 이상함 비교하는 항목에서 이상함
## 지금 보면 시간 낭비니까 나중에 다시 보자

def relation_cnt(N,relation):
    rel_rel_cnt = 0 # 가장 많은 친구의 친구 수
    rel_rel_cnt_index = 0 # 가장 많은 친구를 가진 번호
    rel_num = 0 # 가장 많은 친구를 가진 친구를 가진 사람
    nums = []*(N)

    # 각 번순의 친구 리스트 만들기
    for index in range(1,N+1):
        rel = []
        for i in relation:
            if index == i[0]:
                rel.append(i[1])
        nums.append(rel)

    # 제대로 친구 리스트를 만들었는가 확인
    print(nums)

    # 친구의 친구 카운팅(len) 하고 조건에 맞는 수 빼서 비교
    for index in range(N):
        minus = 0
        rel_index = 0
        for i in nums[index]:
            for j in range(len(nums[index])):
                if nums[index][j] in nums[i-1]:
                    minus += 1

            #print(index+1 , '확인해야할 리스트', nums[i-1])
            if (index+1) in nums[i-1]:
                minus += 1

        # 기존 친구의 친구수 랑 비교해서 높으면 값 덮어씌우기
        if len(nums[index]) - minus > rel_rel_cnt:
            rel_rel_cnt = len(nums[index]) - minus # 가장 많은 친구의 친구 수
            rel_rel_cnt_index = index+1 # 가장많은 친구 번호
            rel_num = index+1 # 가장 많은 친구를 가진 친구를 가진 사람 여기 이상해


    return rel_rel_cnt , rel_rel_cnt_index , rel_num

N = int(input()) # N = 7
arr = list(map(int,input().split()))

relation = []

for i in range(0,len(arr),2):
    relation.append([arr[i],arr[i+1]])

# 제대로 받아왔는가 확인
# print(relation)

ans = relation_cnt(N,relation)
print('가장 많은 친구의 친구 수: ', ans[0])
print('가장 많은 친구의 번호: ', ans[1])
print('가장 많은 친구를 가진 친구를 가진 사람: ', ans[2])
