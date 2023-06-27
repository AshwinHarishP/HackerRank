from itertools import combinations

inputs = input().split()
s = sorted(list(inputs[0]))
k = int(inputs[1])

for i in range(1,k+1):
    
    Combinations = list(combinations(s,i))

    for elements in (Combinations):
        print("".join(elements))
