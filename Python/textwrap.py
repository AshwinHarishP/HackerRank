import textwrap

def wrap(string, max_width):
    length = (len(string) //max_width)+1
    start_index = 0
    end_index = max_width
    for characters in range(length):
        result = string[start_index:end_index]
        start_index+= max_width
        end_index+= max_width
        print(result)
    return ""

        
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
