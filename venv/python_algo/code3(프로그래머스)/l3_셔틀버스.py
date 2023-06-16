# https://mjmjmj98.tistory.com/121

def solution(n, t, m, timetable):
    answer = 0
    crew = [int(time[:2])*60 + int(time[3:]) for time in timetable]
    crew.sort()
    bus = [9*60 + t*i for i in range(n)]

    idx = 0
    for tm in bus:
        cnt = 0
        while cnt < m and idx < len(crew) and crew[idx] <= tm:
            cnt += 1
            idx += 1

        if cnt < m:
            answer = tm
        else:
            answer = crew[idx-1] - 1


    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)

if __name__ == "__main__":
    n, t, m = 1, 1, 5
    timetable = ["08:00", "08:01", "08:02", "08:03"]
    res = "09:00"
    ans = solution(n, t, m, timetable)
    print(ans, res == ans)

    n, t, m = 2, 10, 2
    timetable = ["09:10", "09:09", "08:00"]
    res = "09:09"
    ans = solution(n, t, m, timetable)
    print(ans, res == ans)

    n, t, m = 2, 1, 2
    timetable = ["09:00", "09:00", "09:00", "09:00"]
    res = "08:59"
    ans = solution(n, t, m, timetable)
    print(ans, res == ans)

    n, t, m = 1, 1, 5
    timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
    res = "00:00"
    ans = solution(n, t, m, timetable)
    print(ans, res == ans)

    n, t, m = 1, 1, 1
    timetable = ["23:59"]
    res = "09:00"
    ans = solution(n, t, m, timetable)
    print(ans, res == ans)

    n, t, m = 10, 60, 45
    timetable = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
    res = "18:00"
    ans = solution(n, t, m, timetable)
    print(ans, res == ans)


