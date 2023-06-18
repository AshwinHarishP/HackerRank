A = set(input().split())
n = int(input())
flag = 0


for n_lines in range(n):
    n_sets = set(input().split())
    if not A.issuperset(n_sets):
        flag = 1
        
if flag == 1:
    print("False")
else:
    print("True")
    
    
