# x= '3:16'
# a, b = x.split(':')
# print(a, b, sep=':')

#y, m, d = input().split('.')
#print(d,m,y, sep='-')
#
# s = input()
# y= s[0:2]
# m= s[2:4]
# d= s[4:6]
# print(y,m,d)
#
# h,m,s = input().split(":")
# print(m)

# x,y = input().split(" ")
# print(x+y)
#
# n1=float(input())
# n2=float(input())
# print(n1+n2)
#
# a = int(input())
# print('%X'% a)
# print('%X'%a)

# a = int(input(),16)
# print('%o'%a)

#print(chr(int(input())))


# print(-(int(input())))
# a = ord(input())
# print(chr(int(a+1)))

# x, y= map(int,input().split())
# print(x-y)

# x, y= map(float,input().split())
# print(x*y)

# x, y = input().split()
# print(x*int(y))

# x = int(input())
# y = input()
# print(x*y)

# x, y = map(float,input().split())
# print(x**y)

# x, y = map(int,input().split())
# print(x//y)

# x, y = map(int,input().split())
# print(x%y)

# a=float(input())
# print( format(a, ".2f") )
#
# x, y = map(float,input().split()) >>6043
# print(round(x/y,3))
# print(format(x/y,".3f")) # >> 이런 반올림이 안됨 round 함수 써야해??? 틀렸네 왜? 이따 명균이한태 물어보자


# x, y = map(int,input().split())
# print(x+y)
# print(x-y)
# print(x*y)
# print(x//y)
# print(x%y)
# print((format(x/y,'.2f')))

# x, y, z = map(int,input().split())
# print(x+y+z,format((x+y+z)/3,'.2f'))

# x = int(input())
# print(x<<1)

# x, y = map(int,input().split())
# print(x<<y)

# x, y = map(int, input().split())
# print(x < y)

# x, y = map(int, input().split())
# print(x == y)

# x, y = map(int, input().split())
# print(x <= y)

# x, y = map(int, input().split())
# print(x != y)

# print(bool(int(input())))

# print(not bool(int(input())))

# x, y = map(int,input().split())
# print(bool(x) and bool(y))

# x, y = map(int,input().split())
# print(bool(x) or bool(y))

# x, y =map(int, input().split())
# print((bool(x) and not bool(y)) or(bool(y) and not bool(x)))

# x, y =map(int, input().split())
# print((bool(x) and bool(y)) or(not bool(y) and not bool(x)))

# x, y =map(int, input().split())
# print(not bool(y) and not bool(x))

# x= int(input())
# print(~x)

# #비트 연산자 and
# x, y = map(int, input().split())
# print(x & y)

## 비트 연산자 or
# x, y =map(int, input().split())
# print(x|y)

## 비트 연산자 xor
# x, y =map(int, input().split())
# print(x^y)

# # 삼항 연산자
# x, y= map(int, input().split())
# z = (x if (x>=y) else y)
# print(z)


## 삼항 연산자 2
# a, b, c =map(int, input().split())
# ans =(a if a<b else b) if ((a if a<b else b)<c) else c
# print(ans)

## 짝수만 출력
#a, b, c = map(int, input().split())
#if a%2 ==0:
#    print(a)
#if b%2 == 0:
#    print(b)
#if c%2 == 0:
#    print(c)
#a, b, c = map(int, input().split())
#if a%2 ==0:
#    print('even')
#else:
#    print('odd')
#if b%2 == 0:
#    print('even')
#else:
#    print('odd')
#if c%2 == 0:
#    print('even')
#else:
#    print('odd')

#x = int(input())
#if x<0:
#    if x%2 ==0:
#        print('A')
#    else:
#        print('B')
#else:
#    if x%2 ==0:
#        print('C')
#    else:
#        print('D')


#x =int(input())
#if 90<=x<101:
#    print('A')
#elif 70<=x<90:
#    print('B')
#elif 40<= x < 70:
#    print('C')
#elif 0<=x < 40:
#    print('D')

#x = int(input())
#if x//3 == 1:
#    print('spring')
#elif x//3 ==2:
#    print('summer')
#elif x//3 ==3:
#    print('fall')
#else:
#    print('winter')

#while True:
#    x = int(input())
#    if x == 0:
#        break
#    else:
#        print(x)

#x = int(input())
#while x !=0:
#    print(x)
#    x -=1

#x = ord(input())
## a = 97
#for i in range(97,x+1):
#    print(chr(i), end=' ')

#c = ord(input())
#t = ord('a')
#while t<=c :
#  print(chr(t), end=' ')
#  t += 1

#x = int(input())
#for i in range(0,x+1):
#    print(i)

#x = int(input())
#sum = 0
#for i in range(x+1):
#    if i %2 == 0:
#        sum+=i
#print(sum)

#while True:
#    x = input()
#    if x =='q':
#        print(x)
#        break
#    else:
#        print(x)

#x = int(input())
#sum =0
#num =1
#while sum<x:
#    sum+= num
#    num+=1
#
#print(num-1)

#x, y = map(int, input().split())
#for i in range(1,x+1):
#    for j in range(1,y+1):
#        print(i,j)

#x = int(input(),16)
#for i in range(1,16):
#    print('%X'%x,'*','%X'%i,'=','%X'%(x*i),sep="")

#x = int(input())
#for i in range(1,x+1):
#    if i%10==3or i%10==6or i%10==9:
#        print('X',sep="")
#    else:
#        print(i,sep=" ")

#x, y, z = map(int, input().split())
#tr = 0
#for i in range(x):
#    for j in range(y):
#        for i2 in range(z):
#            print(i,j,i2)
#            tr+=1
#
#print(tr)

#print(44100*16*2*1/8/1024/1024)
#print(format(44100*16*2*1/8/1024/1024*10,".1f"))
#h, b, c, s = map(int,input().split())
#ans =h*b*c*s/8/1024/1024
#print(format(ans,'.1f'),'MB')

#w, h, b = map(int, input().split())
#ans = w*h*b/8/1024/1024
#print(format(ans,'.2f'),'MB')

#goal = int(input())
#sum = 0
#num = 1
#while sum<goal:
#    sum+=num
#    num+=1
#print(sum)

#lastnum = int(input())
#for i in range(lastnum+1):
#    if i%3 !=0:
#        print(i,end=" ")

#s, p, n = map(int,input().split())
#
#for i in range(n-1):
#    s+=p
#
#print(s)

#s, e, n = map(int,input().split())
#
#for i in range(n-1):
#    s*=e
#print(s)

#s,m,d,n = map(int,input().split())
#
#for i in range(n-1):
#    s*=m
#    s+=d
#print(s)

#a, b, c = map(int,input().split())
#day = 1
#while day%a!=0 or day%b!=0 or day%c!=0:
#    day +=1
#print(day)

#tr= int(input())
#list =input().split()
#chek_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#
#for x in range(1,23+1):
#    for y in list:
#
#        if x == int(y):
#            chek_list[x-1]+=1
#
#
#for i in chek_list:
#    print(i,end=" ")

#tr = int(input())
#list= input().split()
#
#for x in range(len(list)-1,-1,-1):
#    print(int(list[x]),end=" ")

#tr = int(input())
#list = input().split()
#for i in range(len(list)):
#    list[i] = int(list[i])
#
#min = 999999
#
#for x in list:
#    if min > x:
#        min =x
#print(min)

## 바둑돌 1
#d= []
#for i in range(20):
#    d.append([])
#    for j in range(20):
#        d[i].append(0)
#
#tr = int(input())
#
#for x in range(tr):
#    a, b = map(int, input().split())
#    d[a][b] = 1
#
#for x in range(1, len(d)):
#    for y in range(1,len(d)):
#        print(d[x][y], end=" ")
#
#    print()

## 바국 십자 뒤집기
# d =[[] for _ in range(19)]
#
# for i in range(19):
#     d[i]=list(map(int, input().split()))
#
# tr = int(input())
# for i in range(tr):
#     x, y = map(int,input().split())
#     for i in range(19):
#         if d[x-1][i]==0:
#             d[x - 1][i]=1
#         else:
#             d[x - 1][i]=0
#
#         if d[i][y-1]==0:
#             d[i][y - 1]=1
#         else:
#             d[i][y - 1]=0
#
# for x in range(len(d)):
#     for y in range(len(d)):
#         print(d[x][y], end=" ")
#     print()

## 설탕과자 뽑기
#첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
#두 번째 줄에 놓을 수 있는 막대의 개수(n)
#세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
#
# h, w = map(int,input().split())
# field=[]
# for i in range(h):
#     field.append([])
#     for j in range(w):
#         field[i].append(0)
#
# bar = int(input())
# for i in range(bar):
#     l, d, x, y = map(int,input().split())
#
#     if d ==0:
#         for j in range(l):
#             field[x-1][y+j-1] = 1
#
#     else:
#         for j in range(l):
#             field[x+j-1][y-1] = 1
#
#
# for i in range(h):
#     for j in range(w):
#         print(field[i][j], end=' ')
#     print()

## 개미는 뚠뚠 오늘도 뚠뚠 열심히 일을 하네 뚠뚠
#
# field =[[] for _ in range(10)]
#
# for i in range(10):
#     field[i]=list(map(int, input().split()))
#
# x,y =1,1 # 시작점
#
# while True:
#     if field[x][y] == 0:
#         if field[x][y+1] == 0 or field[x][y+1]==2:
#             field[x][y]= 9
#             x, y = x, y+1
#
#         else:
#             field[x][y] = 9
#             x, y = x+1, y
#
#     elif field[x][y] == 2:
#         field[x][y] = 9
#         break
#     else:
#         break
#
# for x in range(10):
#     for y in range(10):
#         print(field[x][y], end=' ')
#
#     print()


#
# 5x5
# len= 5
#
# 5x4
# len 5
# range  터진다
#
# h == len(field)
# w == len(field[i])
