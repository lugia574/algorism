tr = int(input())
for tr in range(tr):
    hour_1 = int(input())
    minute_1 = int(input())
    hour_2 = int(input())
    minute_2 = int(input())

    sum_hour = 0
    sum_minute = 0

    if (minute1 + minute2) > 59:
        sum_hour += 1
        sum_minute = minute1 + minute2 - 60

    else:
        sum_minute = minute1 + minute2

    if (hour1 + hour2 + sum_hour) > 12:
        sum_hour = hour1 + hour2 + sum_hour - 12
    else:
        sum_hour = hour1 + hour2 + sum_hour

    print("#" + tr + " " + sum_hour + " " + sum_minute)