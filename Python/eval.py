x,k = input().split()
P = input()

result = eval(P.replace("x",x))

if str(result) == str(k):
    print(True)
else:
    print(False)
