from collections import deque

N = int(input())
d = deque()

for i in range(N):
    command = input().split()
    
    #append
    if command[0] == "append":
        d.append(int(command[1]))
    
    #append left
    elif command[0] == "appendleft":
        d.appendleft(int(command[1]))
    
    #pop
    elif command[0] == "pop":
        d.pop()
    
    #popleft
    elif command[0] == "popleft":
        d.popleft()
print(*d)
