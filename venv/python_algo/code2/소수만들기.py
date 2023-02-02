# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때,
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

# 입출력 예
# nums	result
# [1,2,3,4]	1
# [1,2,7,6,4]	4
# 입출력 예 설명
# 입출력 예 #1
# [1,2,4]를 이용해서 7을 만들 수 있습니다.
#
# 입출력 예 #2
# [1,2,4]를 이용해서 7을 만들 수 있습니다.
# [1,4,6]을 이용해서 11을 만들 수 있습니다.
# [2,4,7]을 이용해서 13을 만들 수 있습니다.
# [4,6,7]을 이용해서 17을 만들 수 있습니다.

# 조합 갯수식은 nCr (중복)
import math
from collections import deque

def PrimeNum(num):
    strandNum = round(math.sqrt(num)) + 1

    for i in range(2, strandNum):
        if num % i == 0:
            return False

    return True




def solution(nums):
    ans = 0
    length = len(nums)

    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                val = sum([nums[i],nums[j],nums[k]])
                bool = PrimeNum(val)
                if bool:
                    ans += 1


    return ans

if __name__ == "__main__":
    nums = [1,2,3,4]
    nums2 = [1,2,7,6,4]

    res = 1
    res2 = 4


    result = solution(nums)
    result2 = solution(nums2)

    print(result)
    print("정답입니다." if res == result else "틀렸습니다. 모지리새끼야")
    print(result2)
    print("정답입니다." if res2 == result2 else "틀렸습니다. 모지리새끼야")