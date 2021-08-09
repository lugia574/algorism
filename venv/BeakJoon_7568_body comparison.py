# 덩치
def body_rank(n,body_list):

    rank_list = [0]*n

    for x in range(len(body_list)):
        rank = 1
        for y in range(len(body_list)):
            if body_list[x][0] < body_list[y][0] and body_list[x][1] < body_list[y][1]:
                rank += 1
        rank_list[x]= rank


    return rank_list




n = int(input())
body_list = []
for _ in range(n):
    body_list.append(list(map(int,input().split())))



rank_list = body_rank(n,body_list)
for x in rank_list:
    print(x , end=" ")