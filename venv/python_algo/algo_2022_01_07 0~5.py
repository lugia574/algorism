# 반복문을 이용한 문제 풀이
# 1. 1부터 N 까지 홀수 출력
# 2. 1부터 N 까지  합 구하기
# 3. N의 약수 구하기

n= int(input())

n_list= []
sum_num= 0

print('1번 답:', end=" ")
for i in range(1,n+1):
    if i%2==1:
        print(i,end=" ")

    if n%i==0:
        n_list.append(i)

    sum_num+= i

print()
print('2번 답:',sum_num)
print('3번 답', list(n_list))
