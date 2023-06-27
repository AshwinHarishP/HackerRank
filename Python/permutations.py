from itertools import permutations

S = input().split()
string = list(S[0])
k = int(S[1])

permutation_result = list(permutations(string,k))

for elements in sorted(permutation_result):
    print("".join(elements))
