def countdown(m):
    if m == 0:
        print("카운터 제로")
    else:
        print('카운터',m)
        countdown(m-1)

# countdown(10)

def recur_gogodan(m, index = 1):
    if index == 9:
        print(m,'*',index,'=',m*index)
    else:
        print(m,'*', index, '=', m * index)
        recur_gogodan(m,index+1)

# recur_gogodan(2)

def cnt(m):
    if m > 0:
        print(m)
        cnt(m - 1)


# cnt(5)

def fac(m):
    if m == 1:
        return 1
    else:
        return m * fac(m-1)

# print(fac(7))

def pow(a, n):
    if n == 1:
        return a
    else:
        return a * pow(a, n-1)

a = 2
n = 6

# print(pow(2, 6))

def make_castle(m):
    if m == 0:
        return
    else:
        for _ in range(m):
            print("*", end="")
        print()

        make_castle(m-1)

        for _ in range(m):
            print("*", end="")
        print()

make_castle(5)