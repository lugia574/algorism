spelling = list(input())


#print(spelling)


def spelling_cheak(sp):
    ans = ''
    ans2 = ''
    dic = {}
    max_cnt = 0
    max_cnt2 = 0

    for i in range(len(sp)):
        sp[i] = sp[i].upper()

    for sp in sp:
        if sp in dic:
            dic[sp] += 1

        else:
            dic[sp] = 1

    for key,val in dic.items():

        if max_cnt < val:
            max_cnt = val
            ans = key

        elif max_cnt == val:
            ans2 = key
            max_cnt2 = val


    if max_cnt == max_cnt2:
        ans = '?'

    return ans

print(spelling_cheak(spelling))