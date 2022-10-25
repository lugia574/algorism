class InputClass ():
    def __init__(self):
        self.N = 0
        self.arr = []

    @classmethod
    def inputFnc(self):
        self.N=int(input())
        self.arr= list(map(int,input().split()))

        return self.N, self.arr