N = int(input())

for i in range(N):
    
    try:
        a,b = map(int,input().split())
        print(int(a)//int(b))
        
    except ZeroDivisionError as e:
        print("Error Code:",e)

    except ValueError as e:
        print("Error Code:",e)
