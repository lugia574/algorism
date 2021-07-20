#윤년
#조건 4의배수이면서 100의 배수는 아닐것 or 400의 배수일때

year=int(input())


if(year%4==0 and year%100!=0):
    print(1)

elif(year%400==0):
    print(1)

else:
    print(0)
