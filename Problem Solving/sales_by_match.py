n = 7                         
ar = [1,2,1,2,1,3,2]

paired_socks = list(set(ar))
pair_count = 0

for elements in paired_socks:
    count_elements = ar.count(elements)
    pairs = count_elements/2
    if pairs <= 0:
        pair_count += count_elements/2

print(int(pair_count))
