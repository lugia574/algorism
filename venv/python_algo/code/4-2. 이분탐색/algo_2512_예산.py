# 이건 너무 쉽다 너무 직관적이야 섹스게스게스게스게스겟
import sys

def budgeting(n, budget, total):
    if sum(budget) <= total:
        return budget[-1]
    lt = 1
    rt = budget[-1]
    while lt <= rt:
        mid = (lt + rt) // 2
        sumBudget = 0
        for cost in budget:
            sumBudget += mid if cost > mid else cost
        if sumBudget > total:
            rt = mid - 1
        else:
            lt = mid + 1
    return rt

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    budget = list(map(int, input().rsplit()))
    totalBudget = int(input())
    budget.sort()

    ans = budgeting(n, budget, totalBudget)
    print(ans)

