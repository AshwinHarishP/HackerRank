def mutate_string(string, position, character):
    List = list(string)
    List[position] = character
    string = "".join(List)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
