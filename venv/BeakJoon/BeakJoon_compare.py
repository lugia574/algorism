#두수 비교하기
number1, number2 = input().split()

number1= int(number1)
number2= int(number2)

if (number1<number2):
    print('<')
elif (number1>number2):
    print('>')
else:
    print('==')