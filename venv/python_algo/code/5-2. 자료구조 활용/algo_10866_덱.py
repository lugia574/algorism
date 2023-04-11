import sys

class HandmadeDeque():
    def __init__(self):
        self.q = []

    def push(self, data):
        self.q.append(data)

    def leftPush(self, data):
        self.q.insert(0, data)

    def leftPop(self):
        pop_object = None
        if not self.isEmpty():
            pop_object = self.q.pop(0)
        return pop_object

    def pop(self):
        pop_object = None
        if not self.isEmpty():
            pop_object = self.q.pop()

        return pop_object

    def front(self):
        front_object = None
        if not self.isEmpty():
            front_object = self.q[0]
        return front_object

    def back(self):
        back_object = None
        if not self.isEmpty():
            back_object = self.q[-1]
        return back_object

    def isEmpty(self):
        is_empty = False
        if len(self.q) == 0:
            is_empty = True
        return is_empty

    def size(self):
        return len(self.q)


if __name__ == "__main__":
    input = sys.stdin.readline
    q = HandmadeDeque()
    T = int(input())

    for _ in range(T):
        command = input().split()
        if command[0] == 'push_front':
            q.leftPush(command[1])
        elif command[0] == 'push_back':
            q.push(command[1])
        elif command[0] == 'pop_front':
            if q.isEmpty():
                print(-1)
            else:
                print(q.leftPop())
        elif command[0] == 'pop_back':
            if q.isEmpty():
                print(-1)
            else:
                print(q.pop())
        elif command[0] == 'size':
            print(q.size())

        elif command[0] == 'empty':
            if q.isEmpty():
                print(1)
            else:
                print(0)
        elif command[0] == 'front':
            if q.isEmpty():
                print(-1)
            else:
                print(q.front())

        elif command[0] == 'back':
            if q.isEmpty():
                print(-1)
            else:
                print(q.back())