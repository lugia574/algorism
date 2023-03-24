# 후위식 연산
# 후위연산식이 주어지면 연산한 결과를 출력하는 프로그램을 작성하세요.
# 만약 3*(5+2)-9 을 후위연산식으로 표현하면 352+*9- 로 표현되며 그 결과는 21입니다.
# ▣ 입력설명
# 첫 줄에 후위연산식이 주어집니다. 연산식의 길이는 50을 넘지 않습니다.
# 식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.
# ▣ 출력설명
# 연산한 결과를 출력합니다.
# ▣ 입력예제 1
# 352+*9-
# ▣ 출력예제 1
# 12
# +-/*

def postfixCalFnc(arr):
    stack = []
    for i in arr:
        if 41<ord(i)<44 or ord(i) == 45 or ord(i) == 47:
            num2 = int(stack.pop())
            num1 = int(stack.pop())

            if i == "+":
                stack.append(num1+num2)
            elif i == "-":
                stack.append(num1-num2)
            elif i == "/":
                stack.append(num1/num2)
            elif i == "*":
                stack.append(num1*num2)
        else:
            stack.append(i)


    return stack[0]

def inputFnc():
    arr = list(map(str,input()))

    return  arr

arr = inputFnc()
res = postfixCalFnc(arr)
print(res)