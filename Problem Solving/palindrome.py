def theLoveLetterMystery(s):
    count = 0
    for i in range(len(s)//2):
        count += abs(ord(s[i]) - ord(s[n-1-i]))
    return count

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        print(result)
