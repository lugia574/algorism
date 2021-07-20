sel = 'a s d f w e q '

st = list(sel)

for i in st:
    if i == ' ':
        st.remove(' ')

print(st)

test = 'heollo python haha'

test_1= test.split()
print(test_1)


# 슬라이싱 문제
# 문제. 해당 배열을 받을시 2개 이상의 문자를 가진것을 기준으로 슬라이싱을 한 배열을 반환하는것
# ex) pizza >> ['pi','aa'] daadsewwwe >> ['d','dse','e'] aaddxxx >> ['','','']

def solution (s):
    str_list = list(s)
    answer = []
    # 1. 먼저 리스트에 중복되는 문자가 있는가?
    std = 0
    cnt = 0
    # 1-1. 판별
    if std == 0:




        for i in range(1,len(str_list)):
            if str_list[i] != str_list[i-1]:
                cnt += 1

            else:
                answer.append(str_list[start:start+cnt])
                start = i
                cnt = 0



# 인덱싱 문제 ㅇㅋㅋ


    # 1-2. 중복되는 문자가 없으면 그대로 뱉어




    return answer





