# Anagram(아나그램 : 구글 인터뷰 문제)
# Anagram이란 두 문자열이 알파벳의 나열 순서를 다르지만 그 구성이 일치하면 두 단어는 아
# 나그램이라고 합니다.
# 예를 들면 AbaAeCe 와 baeeACA 는 알파벳을 나열 순서는 다르지만 그 구성을 살펴보면
# A(2), a(1), b(1), C(1), e(2)로 알파벳과 그 개수가 모두 일치합니다. 즉 어느 한 단어를 재
# 배열하면 상대편 단어가 될 수 있는 것을 아나그램이라 합니다.
# 길이가 같은 두 개의 단어가 주어지면 두 단어가 아나그램인지 판별하는 프로그램을 작성하세
# 요. 아나그램 판별시 대소문자가 구분됩니다.
# ▣ 입력설명
# 첫 줄에 첫 번째 단어가 입력되고, 두 번째 줄에 두 번째 단어가 입력됩니다.
# 단어의 길이는 100을 넘지 않습니다.
# ▣ 출력설명
# 두 단어가 아나그램이면 “YES"를 출력하고, 아니면 ”NO"를 출력합니다.
# ▣ 입력예제 1
# AbaAeCe
# baeeACA
# ▣ 출력예제 1
# YES
def anagram(arr1, arr2):
    agArr1 = dict()
    agArr2 = dict()
    cnt = 0
    for i in range(len(arr1)):
        agArr1[arr1[i]] = agArr1.get(arr1[i],0) + 1
        agArr2[arr2[i]] = agArr2.get(arr2[i], 0) + 1

    for key in agArr1.keys():
        if key in agArr2.keys() and agArr1[key] == agArr2[key]:
            cnt += 1
        else:
            break
    if len(agArr1) == cnt:
        return "YES"
    return "NO"

def solution (arr1, arr2):
    strDic = dict()
    res = "YES"

    for x in arr1:
        strDic[x] = strDic.get(x,0) + 1
    for x in arr2:
        strDic[x] = strDic.get(x,0) - 1

    for x in a:
        if strDic[x] > 0:
            res = "NO"
            break

    return res

# 리스트 해쉬로 풀기
# 아스키 넘버를 이용해서 풀꺼임
# A~Z 가 65 ~ 90 번임
# a~z 가 97 ~ 122 번임
# 대문자-아스키는 65 를 빼주면 01234~25 이렇게 올라가는 index로 넣을 수 있음
# 소문자-아스키는 이제 26 부터 시작하니까 71을 빼주면 26/27/28 ~ 이렇게 할 수 잇음
# C++ 이 이렇게 푸는듯
def solution2(arr1, arr2):
    str1 = [0]*52
    str2 = [0]*52
    res = "NO"
    for x in arr1:
        # 대문자 일때
        if x.isupper():
            str1[ord(x)-65] += 1

        # 소문자 일때
        else:
            str1[ord(x)-71] += 1

    for x in arr2:
        # 대문자 일때
        if x.isupper():
            str2[ord(x) - 65] += 1

        # 소문자 일때
        else:
            str2[ord(x) - 71] += 1

    for i in range(52):
        if str1[i] != str2[i]:
            break
    else:
        res = "YES"
    return res

def inputFnc():
    arr1 = input()
    arr2 = input()

    return arr1, arr2

arr1, arr2 = inputFnc()

res =solution2(arr1, arr2)
print(res)