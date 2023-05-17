# 전형적인 다이나믹 문제라길래
# 못 풀고 답 찾아보는 나 자신이 너무 빡쳐서
# 우선은 넘기고 시간이 지나면 다시 풀어보자 라고 했으나
# 몇일이 지나고 다시 풀어볼려고 했으나 역시나 못풀었다
# 확실히 느낀건 난 ㅄ이라는것
# 어쩔 수 없지 결국 코딩도 머리로 하는건데
# 내가 뭐 학생때 공부를 잘한것도 아닌데 이게 코딩에서도 되겠냐고 ㅋㅋㅋ
# 더군다나 수학을 잘한것도 아니고 ㅋㅋㅋㅋ 글렀다 글렀어 ㅋ
# https://dingdingmin-back-end-developer.tistory.com/entry/%EB%B0%B1%EC%A4%80-5557%EC%9E%90%EB%B0%94-java-1%ED%95%99%EB%85%84
# 우는 소리 그만하고 풀자
# 뭔소린지 이제 이해함
# 처음 8 값을 받았다고 해봐
# 그럼 dp[0][8] 에  +1 해줘 // 그러고 다음 숫자로 3 이 왔다고 쳐봐
# 그럼 dp[1][8-3], dp[1][8+3] 에 dp[0][8] + 1 값을 넣어줘 // 그 담에 2 가 오면 그대로 또 해주고
# 이걸 코드로 해주면

import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().rsplit()))
    dp = [[0] * 21 for _ in range(n)]

    dp[0][nums[0]] = 1
    plus = minus = 0

    for i in range(1, n-1):   # 1 에서 n-1 전까지 하는 이유는 0 은 맨 위에 박았고 n-1 은 마지막 이컬 답이니까
        for j in range(21):  # 굳이 이렇게 for 문으로 해서 20까지 도는 이유는 아래로 내려갈 수록 dp에 값 해줘야하는게 2배씩 늘어나니까임
            if dp[i-1][j] != 0: # i-1 번째 값이 있으면 그 값 기준으로 plus, minus 의 값을 구해서 [i][plus], [i][minus] 에 값을 박아 주는거
                plus = j + nums[i]
                minus = j - nums[i]
                if 0 <= plus < 21: dp[i][plus] += dp[i-1][j]
                if 0 <= minus < 21: dp[i][minus] += dp[i-1][j]
    # for x in dp:
    #     print(x)

    print(dp[n-2][nums[n-1]])