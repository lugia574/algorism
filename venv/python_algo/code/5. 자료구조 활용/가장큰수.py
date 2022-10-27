# 가장 큰 수
# 선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하
# 여 가장 큰 수를 만들라고 했습니다. 여러분이 현수를 도와주세요.(단 숫자의 순서는
# 유지해야 합니다)
# 만약 5276823 이 주어지고 3개의 자릿수를 제거한다면
# 7823이 가장 큰 숫자가 됩니다.
# ▣ 입력설명
# 첫째 줄에 숫자(길이는 1000을 넘지 않습니다)와 제가해야할 자릿수의 개수가 주어집니다.
# ▣ 출력설명
# 가장 큰 수를 출력합니다.
# ▣ 입력예제 1
# 5276823 3
# ▣ 출력예제 1
# 7823
# ▣ 입력예제 2
# 9977252641 5
# ▣ 출력예제 2
# 99776

# 스택으로 하자

# 값 받기 fnc
def inputFnc ():
    num, n = map(int, input().split())
    return num, n

# 숙자 쪼개서 array로 만들기 fnc
def numArr(num):
    arr = list(map(int,str(num)))
    return arr


# array 된 숫자 붙히기 fnc
def numAttach(arr):
    res = ""
    for i in arr:
        res += str(i)
    #  res = "".join(map(str,arr))
    res = int(res)

    return  res

# 큰수 만들기 fnc
def lagestNum(stackArr, n):
    cnt = n
    res = [stackArr[0]]
    for i in range(1,len(stackArr)):
        while res and cnt != 0 and res[len(res)-1] < stackArr[i]:
            res.pop()
            cnt -= 1
        res.append(stackArr[i])

    if cnt != 0:
        res = res[:-cnt]

    return res



num, n = inputFnc()

stackArr = numArr(num)
res = lagestNum(stackArr, n)
res = numAttach(res)

print(res)