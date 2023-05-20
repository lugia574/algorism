def solution(user_id, banned_id):
    answer = []
    res = [[]]

    for ban in banned_id:
        lis = []
        for user in user_id:
            if len(ban) != len(user):
                continue
            else:
                boolean = True
                for i in range(len(ban)):
                    if (ban[i] == "*" or ban[i] == user[i]):
                        continue
                    else:
                        boolean = False
                        break

                if boolean:
                    for c in res:
                        if user not in c:
                            lis.append(c + [user])
        res = lis
    #print(res)
    for s in res:
        if set(s) not in answer:
            answer.append(set(s))

    return len(answer)

if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id  = ["fr*d*", "abc1**"]
    res = 2
    ans = solution(user_id, banned_id)
    print(res == ans)


    user_id2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id2 = ["*rodo", "*rodo", "******"]
    res2 = 2
    ans2 = solution(user_id2, banned_id2)
    print(res2 == ans2)

    user_id2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id2 = ["fr*d*", "*rodo", "******", "******"]
    res2 = 3
    ans2 = solution(user_id2, banned_id2)
    print(res2 == ans2)
