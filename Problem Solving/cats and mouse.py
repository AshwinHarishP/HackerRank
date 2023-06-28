def catAndMouse(x, y, z):
    
    cat_A = abs(z - x)
    cat_B = abs(z - y)
    
    if cat_A < cat_B:
        return("Cat A")
    elif cat_B < cat_A:
        return("Cat B")
    else:
        return("Mouse C")

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)
        print(result)

