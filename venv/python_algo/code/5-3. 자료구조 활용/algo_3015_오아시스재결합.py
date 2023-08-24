# 어?? 이거 푼거 같은데??
# 아닌가??
# 옥상정원 꾸미기랑도 비슷하고 비슷 공연 문제가 딱 이거였는데 설명조차 똑같았던거 같기도 하고?
# 이 문제 전에 풀려고 한적이 있었네 그래서 푼거 같다는 느낌을 받았음
# https://velog.io/@thguss/백준-3015.-오아시스-재결합-with.-Python
# 결국 안풀리더라 키가 같은 경우를 생각해야나벼
# 아 근데 귀찮다 이거 내일이나 아님 이따가 폼 좀 오르면 그때 ㄱㄱ
import sys
if __name__ == "__main__":
    input = sys.stdin.readline
    oasis = [int(input()) for _ in range(int(input()))]

    stack = []  # (키, cnt)로 append
    result = 0

    for o in oasis:

        # 스택 끝 값보다 키 크면 pop
        while stack and stack[-1][0] < o:
            result += stack.pop()[1]

        # 스택이 비어있으면 해당 키 append하고 continue
        if not stack:
            stack.append((o, 1))
            continue

        # 스택 끝 값의 키와 같을 때
        if stack[-1][0] == o:
            cnt = stack.pop()[1]
            result += cnt

            if stack: result += 1
            stack.append((o, cnt + 1))

        # 스택 끝 값의 키보다 작을 때
        else:
            stack.append((o, 1))
            result += 1

    # 결과값 출력
    print(result)