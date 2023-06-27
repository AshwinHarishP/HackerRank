from collections import defaultdict

n, m = list(map(int, input().split()))

A = defaultdict(list)

for i in range(n):
    A[input()].append(i + 1)

for _ in range(m):
    print(*A.get(input(), [-1]))
