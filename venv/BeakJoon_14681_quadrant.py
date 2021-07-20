#사분면 고르기

#1사분면 양수, 양수
#2사분면 음수, 양수
#3사분면 음수, 음수
#4사분면 양수, 음수

location_x = int(input())
location_y = int(input())

if(location_x>0 and location_y>0):
    print(1)
elif(location_x<0 and location_y>0):
    print(2)
elif(location_x<0 and location_y<0):
    print(3)
elif(location_x>0 and location_y<0):
    print(4)
else:
    print(0)