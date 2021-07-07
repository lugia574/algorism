class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):

        length = stk.size()

        if length == 0:
            print(-1)
        else:
            print(self.items[length-1])
            self.items.remove(self.items[length-1])

    def isEmpty(self):
        length = stk.size()
        if length == 0:
            return 1
        else:
            return 0

    def top(self):
        length = stk.size() - 1
        return  self.items[length]

    def size(self):
        length = 0
        for _ in self.items:
            length+= 1

        return length





stk = stack()

n =int(input())

for _ in range(n):
    command = input().split(" ")
    if command[0] == 'push':
        stk.push(int(command[1]))

    elif command[0] == 'pop':
        stk.pop()

    elif command[0] == 'top':
        print(stk.top())

    elif command[0] == 'empty':
        print(stk.isEmpty())

    elif command[0] == 'size':
        print(stk.size())

