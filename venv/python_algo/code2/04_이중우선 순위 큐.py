# 이중우선순위 큐
# 이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.
# I 숫자	큐에 주어진 숫자를 삽입합니다.
# D 1	큐에서 최댓값을 삭제합니다.
# D -1	큐에서 최솟값을 삭제합니다.

# 이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때,
# 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면
# [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

# 제한사항
# operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.
# operations의 원소는 큐가 수행할 연산을 나타냅니다.
# 원소는 “명령어 데이터” 형식으로 주어집니다.-
# 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
# 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.
import heapq as hq


def solution(operations):
    answer = []
    maxNum = -21467000
    minNum = 21467000
    cnt = 0
    for i in operations:
        command, num= i.split()
        num = int(num)
        if command == "I":
            answer.append(num)
            cnt += 1
            if maxNum < num:
                maxNum = num

            if minNum > num:
                minNum = num

        elif command == "D":
            if cnt == 0:
                continue
            cnt -= 1
            if num == -1:
                answer.remove(minNum)
            else:
                answer.remove(maxNum)
            if cnt > 0:
                maxNum = max(answer)
                minNum = min(answer)
            else:
                maxNum = -21467000
                minNum = 21467000
    if cnt == 0:
        return [0, 0]
    else:
        return [maxNum, minNum]
def solHeap(operations):
    maxHeap = []
    minHeap = []
    cnt = 0
    for i in operations:
        command, num = i.split()
        num = int(num)
        if command == "I":
            cnt += 1
            hq.heappush(minHeap, num)
            hq.heappush(maxHeap, -num)
        elif command == "D":
            if cnt == 0:
                continue
            cnt -= 1
            if num == -1:
                tmp = hq.heappop(minHeap) * -1
                maxHeap.remove(tmp)
            else:
                tmp = hq.heappop(maxHeap) * -1
                minHeap.remove(tmp)

    if cnt > 0:
        maxNum = hq.heappop(maxHeap) * -1
        minNum = hq.heappop(minHeap)
    else:
        maxNum = 0
        minNum = 0
    return [maxNum,minNum]

if __name__ == "__main__":
    operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    answer = [0,0]

    # operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    # answer = [333, -45]

    ans = solHeap(operations)
    print(ans)
    print("정답입니다." if ans == answer else "틀렸습니다. 이새끼야")