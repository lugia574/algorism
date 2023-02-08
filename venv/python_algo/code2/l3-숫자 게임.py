# xx 회사의 2xN명의 사원들은 N명씩 두 팀으로 나눠 숫자 게임을 하려고 합니다.
# 두 개의 팀을 각각 A팀과 B팀이라고 하겠습니다. 숫자 게임의 규칙은 다음과 같습니다.
# 먼저 모든 사원이 무작위로 자연수를 하나씩 부여받습니다.
# 각 사원은 딱 한 번씩 경기를 합니다.
# 각 경기당 A팀에서 한 사원이, B팀에서 한 사원이 나와 서로의 수를 공개합니다.
# 그때 숫자가 큰 쪽이 승리하게 되고, 승리한 사원이 속한 팀은 승점을 1점 얻게 됩니다.
# 만약 숫자가 같다면 누구도 승점을 얻지 않습니다.

#B 팀원들이 얻을 수 있는 최대 승점을 return 하도록 solution 함수를 완성해주세요.
# 제한사항
# A와 B의 길이는 같습니다.
# A와 B의 길이는 1 이상 100,000 이하입니다.
# A와 B의 각 원소는 1 이상 1,000,000,000 이하의 자연수입니다.

from collections import deque
def solution(A, B):
    A.sort()
    B.sort()

    answer = 0

    while A:
        x = A[0]
        tmp = []
        for i in B:
            if x < i:
                tmp.append(i)
                break
        if len(tmp) != 0:
            B.remove(min(tmp))
            answer += 1
        A.remove(x)

    return answer

if __name__ == "__main__":
    A = [5,1,3,7]
    B = [2,2,6,8]
    result = 3

    A2 = [2,2,2,2]
    B2 = [1,1,1,1]
    result2 = 0

    res = solution(A,B)
    print(res)
    print("정답입니다" if res == result else "틀렸습니다 모지리 새끼야")

    res2 = solution(A2, B2)
    print(res2)
    print("정답입니다" if res2 == result2 else "틀렸습니다 모지리 새끼야")