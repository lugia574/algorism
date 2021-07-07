T = int(input())
for t in range (T):
    tr,str =input().split()
    tr = int(tr)
    str_list = list(str)

    def StringRepeat (tr,str_list):
        str = ""
        for i in str_list:
            str += i * tr
        return str

    print(StringRepeat(tr,str_list))


# t = int(input())
# for i in range(t):
#     num, s = input().split()
#     text = ''
#     for i in s:
#         text += int(num) * i
#     print(text)