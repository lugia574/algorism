class stack:
    def __init__(self):
        self.stack_list = []
        self.stak_size = 0

    def push(self, item):
        self.stack_list.append(item)
        self.stak_size += 1

    def pop(self):
        length = self.stak_size
        ans = -1

        if length == 0:
            return ans
        else:
            ans = self.stack_list[length-1]
            self.stack_list.remove(self.stack_list[length-1])
            self.stak_size -= 1
            return ans

    def empty(self):
        length = self.stak_size
        ans = 1
        if length == 0:
            return ans
        else:
            ans = 0
            return 0

    def top(self):
        length = self.stak_size
        ans = -1
        if length == 0:
            return ans
        else:
            ans = self.stack_list[length-1]
        return  ans

    def size(self):
        size = self.stak_size
        return size

    def show(self):
        ans = self.stack_list
        return  ans



stack = stack()

n =int(input())

for _ in range(n):
    command = input().split(" ")
    if command[0] == 'push':
        stack.push(int(command[1]))

    elif command[0] == 'pop':
        print(stack.pop())

    elif command[0] == 'top':
        print(stack.top())

    elif command[0] == 'empty':
        print(stack.empty())

    elif command[0] == 'size':
        print(stack.size())

print(stack.show())



# 14
# push 1
# push 2
# top
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# top


# 7
# pop
# top
# push 123
# top
# pop
# top
# pop