number1= int(input())
number2= input()
multi_num=list(number2)
multi_num=list(map(int, multi_num))

print(number1*multi_num[2])
print(number1*multi_num[1])
print(number1*multi_num[0])
multiplication=(number1*multi_num[2])+(number1*multi_num[1]*10)+(number1*multi_num[0]*100)
print(multiplication)