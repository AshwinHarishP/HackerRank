english_tot = int(input())
english_roll = set(input().split())
french_tot = int(input())
french_roll = set(input().split())
only_english = english_roll.difference(french_roll)
Total_students = len(only_english)
print(Total_students)
