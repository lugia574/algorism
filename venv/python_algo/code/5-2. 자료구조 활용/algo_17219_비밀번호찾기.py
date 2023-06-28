# 그냥 딕셔너리 쓰면 됨 자바는 해쉬
import sy

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    homepage = {}
    for _ in range(n):
        http, pw = map(str, input().split())
        homepage[http] = pw

    for _ in range(m):
        http = input().strip()
        print(homepage[http])