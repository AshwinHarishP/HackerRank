N = input().split()
ID = int(N[1])
subjects = N[1]
mark_list = []


for _ in range(ID):
    marks = input().split()
    mark_list.append([float(mark) for mark in marks] )
subject_total = zip(*mark_list)

for elements in subject_total:
    total = sum(list(elements))
    average = round(total/int(subjects),1)
    print(average)
