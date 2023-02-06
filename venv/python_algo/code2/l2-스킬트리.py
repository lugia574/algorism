# 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때,
# 썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고,
# 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.
#
# 위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다.
# 따라서 스파크 → 힐링 → 라이트닝 볼트 → 썬더와 같은 스킬트리는 가능하지만,
# 썬더 → 스파크나 라이트닝 볼트 → 스파크 → 힐링 → 썬더와 같은 스킬트리는 불가능합니다.
#
# 선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때,
# 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.


def solution(skill, skill_trees):
    skillList = list(skill)
    answer = 0

    for i in skill_trees:
        idx = 0
        boolean = True
        for j in list(i):
            if j in skillList:
                if j == skillList[idx]:
                    idx += 1
                else:
                    boolean = False
                    break
        if boolean:
            answer += 1


    return answer


if __name__ == "__main__":
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    result = 2

    res = solution(skill, skill_trees)
    print("정답입니다." if res == result else "틀렸습니다 모지리 새끼야")