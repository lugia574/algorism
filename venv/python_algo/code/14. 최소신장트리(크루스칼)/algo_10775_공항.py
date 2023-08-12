# 이게 뭔소리야??
# 아아 대충 뭔소린지 알겠음
# i번 비행기가 들어오면 gate 1 번부터 i 번째까지 중에 하나 골라서 들어갈 수 있다고
# 만약에 비행기가 못들어가게 되면 이후는 그냥 끝임
# 이걸 생각해야하는게
# 단순히 arr에 박아 넣으면 안됨
# 1 ~ i 까지 있을때 얼마나 애들이 있냐를 따져야해
# 딱 생각나는건 매번 sum 으로 비교하는건데
# 이러면 누가봐도 시초 날꺼란 말이지
# 그럼 sum 으로 비교할때 생각나는건 세그먼트트린데 좀 적용이 안된다?
# 그래서 검색해보니까 다들 유니온 파인드로 문제를 풀어버리네
# https://velog.io/@veonico/백준-10775.-공항-파이썬python
# 세그먼트는 약간 닭잡는데 소칼 쓰는 감이 있긴해
# 그래도 기양 한꺼 세그먼트로 풀고 싶은데 잘 안되네 씹


import sys

def find_root(airplane):
    stack = [airplane]

    while True:
        parking_gate = alters[airplane]

        if parking_gate == airplane:
            break
        else:
            stack.append(parking_gate)
            airplane = alters[parking_gate]

    while stack:
        temp = stack.pop()
        alters[temp] = parking_gate

    return parking_gate

def union(a,b):
    # b is bigger
    a_root = find_root(a)
    b_root = find_root(b)

    alters[a_root] = b_root


if __name__ == "__main__":
    input = sys.stdin.readline

    # 입력 받기
    num_gates = int(input())
    num_airplanes = int(input())
    airplanes = [int(input()) for _ in range(num_airplanes)]

    # 변수 초기화
    alters = list(range(num_gates+1)) # 대안 게이트

    # 게이트 찾기
    cnt = 0

    for i in range(num_airplanes):
        airplane = airplanes[i]
        root = find_root(airplane)

        if root == 0:
            break

        union(root, root-1)
        #print(alters)
        cnt += 1

    print(cnt)