# 큐 fifo (first in first out)

class queue:
    def __init__(self):
        self.q_list = [None for _ in range(n)]
        self.q_size = 0

    def push (self, item):
        self.q_list[self.q_size] = item
        self.q_size += 1

    def pop(self):
        ans = -1

        if self.q_size != 0:
            ans = self.q_list[0]
            self.q_list[0] = None

            # 한칸씩 당겨야 하는거 아니냐
            for i in range(self.q_size):
                self.q_list[i] = self.q_list[i+1]
            self.q_size -= 1

        return ans

    def size (self):
        size = self.q_size
        return size

    def empty(self):
        ans = 1
        if self.q_size == 0:
            return ans
        else:
            ans = 0
            return 0

    def front(self):
        ans = -1
        if self.q_size !=0:
            ans = self.q_list[0]
        return ans

    def back(self):
        ans = -1
        if self.q_size != 0:
            ans = self.q_list[self.q_size-1]
        return ans

    def show(self):
        return self.q_list

n = int(input())
queue = queue()


for _ in range(n):
    command = input().split(" ")
    if command[0] == 'push':
        queue.push(int(command[1]))

    elif command[0] == 'pop':
        print(queue.pop())

    elif command[0] == 'front':
        print(queue.front())

    elif command[0] == 'back':
        print(queue.back())

    elif command[0] == 'empty':
        print(queue.empty())

    elif command[0] == 'size':
        print(queue.size())

    elif command[0] == 'show':
        print(queue.show())


# 15
# push 1
# push 2
# front
# back
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
# front