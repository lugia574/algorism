# j:j+i+1 이렇게 되는 이유가 뭐야
# 그니까 j: j+1 이 당연히 1: 2 이런식으로 싹 돌고 거기에 i 가 붙어서
# 2개씩 3개씩 이렇게 묶음을 늘리는거야
def solution(elements):
    length = len(elements)
    numset = set()
    elements = elements * 2

    for i in range(length):
        for j in range(length):
            numset.add(sum(elements[j:j+i+1]))
    answer = len(numset)
    #print(numset)
    return answer

if __name__ == "__main__":
    elements = [7,9,1,1,4]
    answer = solution(elements)
    res = 18
    print(res == answer)