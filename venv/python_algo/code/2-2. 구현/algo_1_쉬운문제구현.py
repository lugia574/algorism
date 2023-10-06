import sys

#### algo_11718
def algo_11718():
    input = sys.stdin.readline
    while True:
        st = input().strip()
        if st == '':
            break
        print(st)

#### algo_2743_단어 길이재기
def algo_2743():
    input = sys.stdin.readline
    st = input().strip()
    print(len(st))

#### algo_5597_과제 안내신분
def algo_559():
    input = sys.stdin.readline
    student = [False] * 31
    for _ in range(28):
        num = int(input())
        student[num] = True

    for i in range(1, 31):
        if not student[i]:
            print(i)

if __name__ == '__main__':
    algo_559()

