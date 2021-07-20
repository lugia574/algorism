A= int(input())

if A<10:
    a=0
    b=A

else:
    a=A//10
    b=A%10

ans=0
cnt=0

while True:
    c=(a+b)%10

    ans=(b*10)+c
    a=ans//10
    b=ans%10
    cnt+=1
    if ans==A:
        break

print(cnt)