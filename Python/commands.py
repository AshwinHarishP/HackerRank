def process_operations(operations):
    input_list = []
    for operation in operations:
        operation_parts = operation.split()

        if operation_parts[0] == 'insert':
            input_list.insert(int(operation_parts[1]), int(operation_parts[2]))

        elif operation_parts[0] == 'print':
            print(input_list)

        elif operation_parts[0] == 'remove':
            input_list.remove(int(operation_parts[1]))

        elif operation_parts[0] == 'append':
            input_list.append(int(operation_parts[1]))

        elif operation_parts[0] == 'sort':
            input_list.sort()

        elif operation_parts[0] == 'pop':
            input_list.pop()

        elif operation_parts[0] == 'reverse':
            input_list.reverse()

operations = []
N=int(input())
for i in range(N):
    operation = input()
    operations.append(operation)
    
process_operations(operations)
