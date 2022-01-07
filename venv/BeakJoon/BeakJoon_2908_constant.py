# 상수 쉑
nums = list(input().split())

def Sans(nums):
    max_num = 0
    Sans_num = []

    for num in nums:
        temp_num = 0
        temp = ''
        temp_list=list(num)
        for i in range(len(temp_list)-1,-1,-1):
            temp+= temp_list[i]

        temp_num = int(temp)

        #print(temp_num)
        if temp_num > max_num:
            max_num = temp_num

    return max_num


print(Sans(nums))