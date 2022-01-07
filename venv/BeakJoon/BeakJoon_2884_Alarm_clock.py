#알람시계

H,M = input().split()

H = int(H)
M = int(M)

if(H==0):
    if(M>=45):
        print(H,M-45)
    else:
        print(23, 60 + (M - 45))

else:
    if (M - 45 >= 0):
        print(H, M - 45)
    else:
        print(H - 1, 60 + (M - 45))
