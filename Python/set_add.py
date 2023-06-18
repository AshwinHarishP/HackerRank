N=int(input())
List = []
for countries in range(N):
    country = input()
    List.append(country)
Set = set(List)
print(len(Set))
