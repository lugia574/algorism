# ▣ 입력설명
# 한 줄에 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다. 괄호 문자의
# 개수는 최대 100,000이다.
# ▣ 출력설명
# 잘려진 조각의 총 개수를 나타내는 정수를 한 줄에 출력한다.
# ▣ 입력예제 1
# ()(((()())(())()))(())
# ▣ 출력예제 1
# 17
# ▣ 입력예제 2
# (((()(()()))(())()))(()())
# ▣ 출력예제 2
# 24


# 스택으로 해야해
# 와 내가 어떻게 풀었는지 적어야할꺼 같애
# 스택 리스트를 하나 만들어 그리고 arr 배열을 하나 하나 받아서 if 문으로 비교해
# 그래서 ( 이거면 스택 리스트에 그대로 박고
# ) 이거면 문이 닫 닫히는거니까  이전 요소랑 비교 해서
# 이전 요소가 ( 이거면  () 이니까 레이저임 스택에서 pop 하고 남은 len(stack) 값 cnt+= 하는거임
# 이전 요소가 ) 이거면 )) 이니까 레이저가 아니라 바가 끝나는 지점이라는 소리니까
# 스택에 pop 하고 바 하나 끝났다는 소리니까 cnt += 1 해주는 거임
# 이럼 끝
def cuttingFnc(arr):
    stack = [arr[0]]
    cnt = 0
    for i in range(1,len(arr)):
        if arr[i] == "(" :
            stack.append(arr[i])
        elif arr[i] == ")":
            if arr[i-1] == "(":
                stack.pop()
                if stack:
                    cnt += len(stack)
            elif arr[i-1] == ")":
                stack.pop()
                cnt += 1
    return  cnt

def inputFnc ():
    arr = list(map(str,input()))
    return arr

laserAndBar = inputFnc()

res = cuttingFnc(laserAndBar)
print(res)