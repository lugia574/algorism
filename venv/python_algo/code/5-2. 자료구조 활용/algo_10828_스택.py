import sys

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        pop_object = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            pop_object = self.stack.pop()

        return pop_object

    def top(self):
        top_object = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            top_object = self.stack[-1]

        return top_object

    def isEmpty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True
        return is_empty

    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())

    stackArr = Stack()
    for _ in range(n):
        command = input().split()

        if command[0] == 'push':
            stackArr.push(command[1])
        elif command[0] == 'pop':
            if stackArr.isEmpty():
                print(-1)
            else:
                print(stackArr.pop())
        elif command[0] == 'size':
            print(stackArr.size())
        elif command[0] == 'empty':
            if stackArr.size() == 0:
                print(1)
            else:
                print(0)
        elif command[0] == 'top':
            if stackArr.size() == 0:
                print(-1)
            else:
                print(stackArr.top())