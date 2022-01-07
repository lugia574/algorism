list_num =[]
for i in range(9):
    list_num.append(int(input()))

max_num = max(list_num)
print(max_num, list_num.index(max_num)+1)
