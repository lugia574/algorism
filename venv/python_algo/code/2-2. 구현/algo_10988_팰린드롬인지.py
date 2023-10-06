import sys

def palindrome(arr):
    size = len(arr)
    for i in range(size//2):
        if arr[i] != arr[size-1-i]:
            return False
    return True

if __name__ == "__main__":
    input = sys.stdin.readline
    st = input().strip()
    ok = palindrome(st)
    print(1 if ok else 0)