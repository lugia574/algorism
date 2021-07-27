def factorial_recursion(num):
    if num <= 1 :
        return 1
    else:
        return num * factorial_recursion(num-1)

num = int(input())

print(factorial_recursion(num))