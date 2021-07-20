def solution(purchase):
    purchase_list = []
    purchase_day = [0] * 366
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    answer = [0] * 5

    for i in purchase:
        purchase_list.append([int(i[5:7]), int(i[8:10]), int(i[11:])])
    for i in range(len(purchase_list)):
        for j in range(30):
            month_2 = 0
            for k in range(purchase_list[i][0]):
                month_2 += month[k]

            purchase_day[month_2 + purchase_list[i][1] + j] += purchase_list[i][2]
    for i in range(1,len(purchase_day)):
        if purchase_day[i] < 10000:
            answer[0] += 1
        elif purchase_day[i] < 20000:
            answer[1] += 1

        elif purchase_day[i] < 50000:
            answer[2] += 1

        elif purchase_day[i] < 100000:
            answer[3] += 1
        else:
            answer[4] += 1

         return answer

    # print("hi")
print(solution(["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"]))
