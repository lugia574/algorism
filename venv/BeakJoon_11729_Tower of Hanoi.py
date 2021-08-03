# 하노이 탑

def hanoi(num, from_p, to_p, other_p):
    if num == 0:
        return

    hanoi(num-1, from_p, other_p, to_p)
    hanoi_lsit.append([from_p, to_p])

    hanoi(num - 1, other_p, to_p, from_p)

num = int(input())
from_p = 1
to_p = 3
other_p = 2
hanoi_lsit = []
cnt = 0

hanoi(num, from_p, to_p, other_p)

print(len(hanoi_lsit))
for i in range(len(hanoi_lsit)):
    for j in range(2):
        print(hanoi_lsit[i][j], end=" ")
    print()
