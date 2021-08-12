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

recur_gogodan(2)