def countdown(m):
    if m == 0:
        print("카운터 제로")
    else:
        print('카운터',m)
        countdown(m-1)

countdown(10)
