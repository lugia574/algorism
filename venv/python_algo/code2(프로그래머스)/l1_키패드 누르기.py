def solution(numbers, hand):
    answer = ''

    # 키패드 위치
    pad = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
           '4': (1, 0), '5': (1, 1), '6': (1, 2),
           '7': (2, 0), '8': (2, 1), '9': (2, 2),
           '*': (3, 0), '0': (3, 1), '#': (3, 2)
           }

    left = pad['*']  # 처음 왼손의 위치
    right = pad['#']  # 처음 오른손의 위치

    for num in numbers:
        # 왼손이 누를 번호
        if num == 1 or num == 4 or num == 7:
            answer += 'L'  # answer에 'L' 저장
            left = pad[str(num)]  # 해당 번호를 눌렀을 때 왼손의 위치 저장

        # 오른손이 누를 번호
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'  # answer에 'R' 저장
            right = pad[str(num)]  # 해당 번호를 눌렀을 때 오른손의 위치 저장

        # 번호가 2,5,8,0일 때
        else:
            # 번호와 왼손의 거리 계산
            left_dis = abs(left[0] - pad[str(num)][0]) + abs(left[1] - pad[str(num)][1])
            # 번호와 오른손의 거리 계산
            right_dis = abs(right[0] - pad[str(num)][0]) + abs(right[1] - pad[str(num)][1])

            # 왼손이 더 가까울 때
            if left_dis < right_dis:
                answer += 'L'
                left = pad[str(num)]

            # 오른손이 더 가까울 때
            elif left_dis > right_dis:
                answer += 'R'
                right = pad[str(num)]

            # 왼손과 오른손 거리가 같을 때
            else:
                if hand == 'right':
                    answer += 'R'
                    right = pad[str(num)]
                else:
                    answer += 'L'
                    left = pad[str(num)]

    return answer