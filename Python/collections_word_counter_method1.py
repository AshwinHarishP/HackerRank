from collections import Counter
N = int(input())
words = ""

for _ in range(N):
    inputs = input()
    words += inputs+" "

words = words.split()
count = Counter(words)

print(len(count))
print(*count.values())
