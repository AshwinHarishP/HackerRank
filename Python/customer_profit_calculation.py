from collections import Counter
X = int(input())
all_shoe = input().split()
N_of_customers = int(input())
Sum=0

for _ in range(N_of_customers):
    customer_shoes = input().split()
    shoe_size = customer_shoes[0]
    price = int(customer_shoes[1])
    
    if shoe_size in all_shoe:
        all_shoe.remove(shoe_size)
        Sum+=price
print(Sum)
