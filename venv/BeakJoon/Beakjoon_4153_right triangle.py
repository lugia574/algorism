def r_triangle(side):
    ans = 'right'
    max_side = max(side)
    side.remove(max_side)

    if side[0]**2 + side[1]**2 != max_side**2:
        ans = 'wrong'

    return ans

while True:
    side = list(map(int,input().split()))
    if sum(side) == 0:
        break

    ans = r_triangle(side)
    print(ans)