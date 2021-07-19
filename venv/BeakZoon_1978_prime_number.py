# N 개의 수가 주어지고
# 그중 소수인 숫자들의 갯수 세기
import math


def PrimeMemberCnt (tr, nums):
    count = 0
    for i in range(tr):
        true = 1
        standard = int(math.sqrt(nums[i]))

        if nums[i] != 1:
            for j in range(2, standard + 1):
                if nums[i] % j ==0:
                    true = 0

            if true == 1:
                count += 1


    return count

tr = int(input())
nums = list(map(int,input().split()))

print(PrimeMemberCnt(tr,nums))
