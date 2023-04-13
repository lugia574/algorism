# https://seongonion.tistory.com/53
# 이게 단순히 배열 하나로 넣고 빼고 커서를 어쩌고, insert 하고 ㅈㄹ하는 걸로는 해당 문제를 풀수 없음
# 시간 초과가 떠버림
# 왜냐면 insert 같이 해당 index를 요구하게 되면 길이가 길어지는 만큼 존나 뺑뺑 돌아
# 그래서 배열 두개를 준비해서 커서 뒤에 있는 애들은 st2 로 옮겨버리면서 하는 거임
# 그러면 단순히 pop() 만으로도 쌉 가능
import sys

def editor():
    for _ in range(int(input())):
        command = list(input().split())
        if command[0] == 'L':
            if st1:
                st2.append(st1.pop())

        elif command[0] == 'D':
            if st2:
                st1.append(st2.pop())

        elif command[0] == 'B':
            if st1:
                st1.pop()

        else:
            st1.append(command[1])

if __name__ == "__main__":
    input = sys.stdin.readline
    st1 = list(input().rstrip())
    st2 = []
    editor()
    st1.extend(reversed(st2))
    print(''.join(st1))
