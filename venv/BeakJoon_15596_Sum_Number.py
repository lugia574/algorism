# 정수  N 개가 주어 졌을때 정수들의 함들 구하시오

num_list = list(map(int,input().split()))


def sum_num (num_list):
    sum = 0
    try:
        for i in num_list:
            sum += i

        return sum

    except:
        print()

print(sum_num(num_list))