# 30의 배수가 되는 조건
# - 일의 자리수가 0이여야 함.
# - 각 자리의 숫자들을 더했을때 3으로 나누어 떨어져야함.
# 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.
# 나 약간 이해가 안가는게
# 만약에 음 015 면 510 인데 만약에 510가 안되면 150 가야하는거 아님가? 무조건 되나?
# 그런듯??? 무조건 각 숫자들으 합을 3으로 나눌수 있음 무조건 되나벼
# https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-10610%EB%B2%88-30-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython
import sys

def multiple(arr):
    sumNum = 0
    if '0' not in arr:
        return -1
    for x in arr:
        sumNum += int(x)
    if sumNum % 3 != 0:
        return -1
    return "".join(arr)

if __name__ == "__main__":
    input = sys.stdin.readline
    st = list(input().rstrip())
    st.sort(reverse=True)
    res = multiple(st)
    print(res)