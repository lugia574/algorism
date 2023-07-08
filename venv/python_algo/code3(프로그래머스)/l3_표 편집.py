# 그냥 q 구조 문제 아닌가? 쓰레기통은 스택구조로 하고?
# idx 변수 선언해서 idx = k 로 초기화 해주고
# 문제는 단순히 지우고 넣고가 땡이 아니라
# 해당 요소들이 제대로 있는지 OX 로 표시해서 출력해야하자너
# 그리고 단순히 remove, pop 이런거 하면 제법 마니 계산이 돌꺼 같은데
# 배열을 두개 써야할듯?
# 이게 구현하기 전에도 어쩌지 생각은 했었는데
# z 로 다시 돌릴때 완전 원래 있던 자리로 돌리는거라
# 이걸 어떻게 원래 자리르 찾아가냐 이걸 못하겠더라
# 이걸 먼저 생각하고 구현에 들어가야하는데
# 우선 어떻게든 해보자 하고 짜면서 생각하니까 ㅋ

# https://kimjingo.tistory.com/161
# 대충 링크드리스트 구현해주는걸로 해당 문제를 해결함
# 클래스로 각각 노드들의 앞뒤를 정보를 가진 구조체로 구현해놓고
# cmd 에 따라 cur(현재위치) 를 조정하고
# 'C' 삭제일땐 False 처리만 하고
# 앞뒤 노드의 연결을 수정해줘
# 그리고 'Z' 일땐 휴지통에서 pop 해줘서 해당 노드 정보에 앞뒤가 누군지 다 나와있으니까
# 재연결 해주면 되는거임
from collections import deque

class Node:
    def __init__(self):
        self.prev = -1 # 이전 노드 인덱스
        self.next = -1 # 다음 노드 인덱스
        self.is_delete = False # 삭제 여부

def solution(n, k, cmd):
    # 1. 링크드리스트 초기화
    node_list = [Node() for _ in range(n)]  # 노드 리스트 생성
    for i in range(n - 1):
        node_list[i].next = i + 1  # i 번째 노드의 next는 i+1
        node_list[i + 1].prev = i  # i+1 번째 노드의 prev는 i

    # 2. 삭제된 노드를 저장할 스택
    del_stack = deque()

    # 3. 명령어 처리
    cur = k  # 현재 가리키고 있는 노드의 인덱스
    for c in cmd:

        if len(c) > 1:
            c, move_size = c.split(' ')
            move_size = int(move_size)

        if c == "U":
            for i in range(move_size):
                cur = node_list[cur].prev  # cur을 cur 노드의 prev로 교체
        elif c == "D":
            for i in range(move_size):
                cur = node_list[cur].next  # cur을 cur 노드의 next로 교체
        elif c == "C":
            node_list[cur].is_delete = True  # 현재 노드에 삭제 표시
            del_stack.append(cur)  # 스택에 삭제된 노드 번호 추가

            prev_node = node_list[cur].prev  # 이전 노드 번호
            next_node = node_list[cur].next  # 다음 노드 번호

            if prev_node != -1:  # 이전 노드가 있는 경우
                node_list[prev_node].next = next_node  # 이전 노드의 next를 삭제된 노드가 가리키던 next로 교체
            if next_node != -1:  # 다음 노드가 있는 경우
                node_list[next_node].prev = prev_node  # 다음 노드의 prev를 삭제된 노드가 가리키던 prev로 교체
                cur = next_node  # 가리키고 있는 노드를 next_node로 갱신
            else:  # 만약 다음 노드가 없는 경우
                cur = prev_node  # 가리키고 있는 노드를 prev_node로 갱신

        elif c == "Z":
            del_node = del_stack.pop()  # stack의 가장 상위 요소를 가져옴
            node_list[del_node].is_delete = False  # 해당 노드의 is_delete = False로 변경

            prev_node = node_list[del_node].prev  # 삭제된 노드의 이전 노드
            next_node = node_list[del_node].next  # 삭제된 노드의 다음 노드

            if prev_node != -1:  # 이전 노드가 존재하는 경우
                node_list[prev_node].next = del_node  # 이전 노드의 next를 현재 노드로 지정
            if next_node != -1:
                node_list[next_node].prev = del_node  # 다음 노드의 prev를 현재 노드로 지정

    # 4. 삭제된 노드 판별
    answer = []
    for i in range(n):
        if node_list[i].is_delete:
            answer.append("X")
        else:
            answer.append("O")
    return "".join(answer)


if __name__ == "__main__":
    # n, k = 8, 2
    # cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
    # result = "OOOOXOOO"
    #
    # answer = solution(n, k, cmd)
    # print(result == answer, answer)

    n, k = 8, 2
    cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
    result = "OOXOXOOO"

    answer = solution(n, k, cmd)
    print(result == answer, answer)