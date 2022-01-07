# 높이 H
# 길이 W
# 방 갯수 H * W
# 방 번호 (HX // N) (몫) 만큼 옆으로 가서 (HX % N) 나머지 수 만큼 올라감

def hotel(H, W, N):
    room_layer = N%H
    room_num = N//H

    if room_layer == 0:
        ans = (H * 100) + room_num
    else:
        ans = (room_layer*100)+room_num + 1
    return ans

T = int(input())
for _ in range(T):
    H, W, N = map(int,input().split())
    print(hotel(H,W,N))