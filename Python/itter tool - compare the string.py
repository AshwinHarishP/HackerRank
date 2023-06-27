from itertools import groupby
s = input()
group = groupby(s)
List = []
for keys,values in group:
    print(f'({len(list(values))}, {keys})',end=' ' )
