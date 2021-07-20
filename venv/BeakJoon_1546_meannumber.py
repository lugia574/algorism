# 먼저 싹 받아
# 그리고 최대값을 구하고
# N/최대값*100 값을 다 해주고 리스트를 새로 만들던가 갱신
# 그거 평균값 출력

tr= int(input())
score_list=list(map(int,input().split(" ")))

#print(score_list)

max_num=max(score_list)

for i in range(tr):
    score_list[i]=score_list[i]/max_num*100

ans=round(sum(score_list)/len(score_list),6)
print(ans)


