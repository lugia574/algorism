# 먼소린지 모르겠음
# 먼가 어려워
# https://dev-note-97.tistory.com/165
# 끝까지 남을 수 있는 풍선의 조건은 자신을 기준으로 양쪽의 최솟값 중 하나라도 자신보다 크면 된다는 것 이라는데?
# 양쪽의 최솟값이 둘 다 자신보다 작다면, 그 풍선은 어떻게든 터질 수 밖에 없다

# ㅇㅇㅇ 먼소린지 이해갔음
# 결국 양측 최솟값을 비교하는 이유는 가령 10 9 5 3 4 1 에서 9 가 가능한지 따져 보면
# 10 : 9 는 당연히 10 이 더크니까 더질꺼고
# 9 : 5 3 4 1 에서 다 9보다 작음 그렇지만 결국 동일값은 없음 (a의 모든 수는 서로 다릅니다.)
# 그렇기에 결국 5 3 에서 5 잡히고 3 4 에서 4 잡히고 3 1 에서 3 잡히니까 결국은 최솟값 1 만 남음
# 그럼 9 : 1 인데 딱 한번 그냥 조지기 가능하니까 결국 9번은 살아 나음

# 이런 원리로 양극단에 있는 숫자는 무조건 될 수 밖에 없음
# 왜냐면 양측에서 비교하는게 아닌 한쪽면만 비교하면 되니까
# 결국은 최솟값만 남게 될것이고 그게 해당 넘버보다 크든 작든 어차피 넘겨 버릴 수 있으니까

# 그럼 이제 어떻게 구현 하냐를 따지면
# 당연히 for 으로 하나하나 lt, rt 최솟값(min)을 구해서 그걸 비교해서 할텐데
# 이러면 시간이 너무 걸림 사실상 o^2 수준일듯? 그래서 효율성 검사에서 조짐

# 어떻게 하냐? dp 를 조져야함
# 두개의 dp 를 만들고 양측에서 시작해서 하나하나 값을 비교해서 최솟값을 구해 박아
# 그러면 어느 한곳 기준으로 양 최솟값을 바로 양옆을 보고 체크가 가능함

def solution(a):
    if len(a) == 1:
        return 1

    answer = 2  # 기본적으로 양쪽 끝은 끝까지 살아남을 수 있음

    # 최솟값 쌓기 ----------------
    l_min = [a[0]]
    r_min = [a[-1]]
    for i in range(1, len(a)):
        if a[i] < l_min[-1]:
            l_min.append(a[i])
        else:
            l_min.append(l_min[-1])
        if a[len(a) - 1 - i] < r_min[-1]:
            r_min.append(a[len(a) - 1 - i])
        else:
            r_min.append(r_min[-1])
    r_min.reverse()
    # -----------------

    # 찾은 최솟값으로 비교 계산 -------------
    for i in range(1, len(a) - 1):
        if l_min[i - 1] > a[i] or r_min[i + 1] > a[i]:
            answer += 1
    # --------------------------------

    return answer

if __name__ == "__main__":
    a = [9,-1,-5]
    res = 3
    ans = solution(a)
    print(ans == res, ans)

    a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
    res = 6
    ans = solution(a)
    print(ans == res, ans)




