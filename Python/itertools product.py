from itertools import product
A = set(list(map(int,input().split())))
B = set(list(map(int,input().split())))

print(*product(A,B))
