# N명의 사람들이 있고
# 각 사람당 1번 부터 번호를 붙여 구별한다
# 친구의 친구가 되는 사람이 가장 많은 경우를 찾아 그 친구의 친구 수를 구하라
# 단, 본인을 제외하며, 바로 친구였던 경우도 제외

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
    # print(nums)

    # 친구의 친구 카운팅(len) 하고 조건에 맞는 수 빼서 비교
    for index in range(N):
        minus = 0
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
            rel_num = N # 가장 많은 친구를 가진 친구를 가진 사람


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
