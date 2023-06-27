from collections import Counter
X = int(input())
all_shoe = input().split()
N_of_customers = int(input())
Sum=0

for _ in range(N_of_customers):
    customer_shoes = input().split()
    keys,value = tuple(Counter(customer_shoes))
    
    if keys in all_shoe:
        Sum+=int(value)
        all_shoe.remove(keys)
print(Sum)
