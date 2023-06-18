T = int(input())

for test_case in range(T):
    A = int(input())
    elements_A = set(input().split())
    
    B = int(input())
    elements_B = set(input().split())
    
    if elements_A.issubset(elements_B):
        print("True")
    else:
        print("False")
        
