n = int(input())
roll_numbers_n = set(input().split())
b = int(input())
roll_numbers_b = set(input().split())
atleast_one_subscription = roll_numbers_n.union(roll_numbers_b)
print(len(atleast_one_subscription))

