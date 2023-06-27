from collections import Counter
count = Counter(input() for _ in range(int(input())))
print(len(count))
print(*count.values())
