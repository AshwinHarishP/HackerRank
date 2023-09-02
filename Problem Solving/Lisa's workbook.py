def workbook(n, k, arr):
    special_problems = 0
    page = 1
    
    for num_problems in arr:
        for problem in range(1, num_problems + 1):
            if problem == page:
                special_problems += 1
            
            if problem % k == 0 or problem == num_problems:
                page += 1
                
    return special_problems


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    result = workbook(n, k, arr)
    print(result)
