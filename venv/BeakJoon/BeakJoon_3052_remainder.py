# 10개의 수를 입력  전부 리스트에 담은 다음에
list=[]
for i in range(10):
    list.append(int(input()))

#print(list)

remainder_list=[]

#리스트에 특정 값이 있는지 체크하기
for i in list:
        if i%42 not in remainder_list:
            remainder_list.append(i%42)

print(len(remainder_list))

