# 분수
# 1/1  (1) >> 1
# 1/2, 2/1 (2) >> 2 3
# 3/1, 2/2, 1/3 (3) >> 4 5 6
# 1/4, 2/3, 3/2, 4/1 (4) >> 7 8 9 10
# 5/1, 4/2, 3/3, ~~
# 갯수 1 3 6 10 15 21 28 36

# 갯수 증가는 등차수열
# 증가 값이 홀수면 분자가 큰거부터
# 짝수는 분모가 큰거부터


def fraction (num):
    ans = ''
    num_range = 1
    pre_range = 0
    plus = 2
    #print('num :', num, 'num_range : ', num_range)

    if num == 1:
        return '1/1'
    else:
        while True:
            if num <= num_range:
                # 딱 이 범위니까 거기서 맞춰서 분수 찾고 출력
                if (num_range-pre_range)%2 == 0:
                    # 짝수 증가
                    ans = str(num-pre_range)+'/'+str(num_range+1-num)
                else:
                    # 홀수 증가
                    ans = str(num_range+1-num)+'/'+str(num-pre_range)



                return  ans

            else:
                pre_range = num_range
                num_range += plus
                plus += 1









cnt = int(input())
print(fraction(cnt))