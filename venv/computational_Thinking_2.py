# N명의 사람들이 있고
# 각 사람당 1번 부터 번호를 붙여 구별한다
# 친구의 친구가 되는 사람이 가장 많은 경우를 찾아 그 친구의 친구 수를 구하라
# 단, 본인을 제외하며, 바로 친구였던 경우도 제외

def relation_cnt(N,relation):
    rel_rel_num = 0
    rel_rel_num_index = 0
    nums = []*(N)

    # 각 번순의 친구 리스트 만들기
    for index in range(1,N+1):
        rel = []
        for i in relation:
            if index == i[0]:
                rel.append(i[1])
        nums.append(rel)

    print(nums)
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
        if len(nums[index]) - minus > rel_rel_num:
            rel_rel_num = len(nums[index]) - minus
            rel_rel_num_index = index+1


    return rel_rel_num , rel_rel_num_index

N = int(input()) # N = 7
arr = list(map(int,input().split()))

relation = []

for i in range(0,len(arr),2):
    relation.append([arr[i],arr[i+1]])

print(relation)

ans = relation_cnt(N,relation)
print(ans)