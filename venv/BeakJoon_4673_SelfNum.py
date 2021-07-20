# 셀프 넘버 >> 생성자가 없는 숫자
# 우선 던져봐

def self_number():
    number_list = []
    for i in range(1,10000):
        number_list.append(i)

    for i in range(1, 10000):
        sum = i
        if i < 10: sum += i%10
        elif i < 100: sum += i%10 + (i//10)
        elif i < 1000: sum += i% 10 + ((i//10)%10) + (i//100)
        elif i < 10000: sum += i% 10 + ((i//10)%10) + ((i//100)%10) + (i//1000)

        #print('원래 값',i,'//','나온값',sum)
        if sum in number_list:
            #print('빠져야할값', sum)
            number_list.remove(sum)


    for i in number_list:
        print(i)

self_number()