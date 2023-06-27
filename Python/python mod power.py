def calculate_power(a,b,m):
    power = a**b
    modular_exponention = pow(a,b,m)
    print(power)
    print(modular_exponention)

a = int(input())
b = int(input())
m = int(input())
calculate_power(a,b,m)
