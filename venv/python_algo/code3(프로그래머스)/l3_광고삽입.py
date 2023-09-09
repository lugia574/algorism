# 딱봐도 예전에 풀었던
# 철판인가 뭐 무슨 판들이 있는 데에서 어디를 잘라야 판이 마니 나오냐, 고속도로 카메라 설치를 어디를 해야
# 이런 류들 문제구만 뭘
# 근데 이 문제는 좀 빡세 보이긴해
# 애초에 카메라 문제도 내가 제대로 못풀었는데

def solution(play_time, adv_time, logs):
    answer = ''
    
    return answer

if __name__ == "__main__":
    play_time = "02:03:55"
    abv_time = "00:14:15"
    logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
    res = "01:30:59"

    answer = solution(play_time, abv_time, logs)
    print(res == answer, answer)


    play_time = "99:59:59"
    abv_time = "25:00:00"
    logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
    res = "01:00:00"

    answer = solution(play_time, abv_time, logs)
    print(res == answer, answer)



    play_time = "50:00:00"
    abv_time = "50:00:00"
    logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
    res = "00:00:00"

    answer = solution(play_time, abv_time, logs)
    print(res == answer, answer)
