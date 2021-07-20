tc= int(input())
for i in range(tc):
    shcool_class = list(map(int,input().split()))
    #print(shcool_class)

    #평균을 구하고 평균을 넘는 애들 cnt 세줘
    # 그걸 cnt/N 해줘
    avg =(sum(shcool_class)-shcool_class[0])/shcool_class[0]
    cnt =0
    for x in range(1,len(shcool_class)):
        if avg < shcool_class[x]:
            cnt+=1

    percent=round(cnt/shcool_class[0]*100,3)
    print('%.3f'%percent+"%")

    #'%.2f' % 2.3
