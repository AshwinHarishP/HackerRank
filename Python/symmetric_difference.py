M = input()
set_a = input().split()
N = input()
set_b = input().split()

List_a =[]
List_b =[]

for characters_a in set_a :
    digits_a = int(characters_a)
    List_a.append(digits_a)
List_a=set(List_a)

for characters_b in set_b :
    digits_b = int(characters_b)
    List_b.append(digits_b)
List_b=set(List_b)

List_c = sorted(list(List_a.symmetric_difference(List_b)))
 


for k in List_c:
    print(k)


