if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runner_up = list(set(arr))
    runner_up = sorted(runner_up,reverse=True)
    print(runner_up[1])
