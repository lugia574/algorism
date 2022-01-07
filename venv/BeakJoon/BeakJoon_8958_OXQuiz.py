tr = int(input())
for i in range(tr):
    quiz_list=list(input())
    #print(quiz_list)

    cnt = 1
    score = 0
    for x in quiz_list:
        if x =='O':
            score+=cnt
            cnt+=1
        else:
            cnt=1
    print(score)