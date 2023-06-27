N = int(input())
dict_values = {}
for i in range(N):
    inputs = input().split()
    price,item_name = (inputs[-1] ,inputs[:-1]) 
    item_name = " ".join(item_name)
    
    if not item_name in dict_values:
        dict_values[item_name] = int(price)
    else:
        dict_values[item_name]+=int(price)

for key,value in dict_values.items():
    print(key,value)
