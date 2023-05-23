operations = {
    'read': 'r',
    'write': 'w',
    'execute': 'x',
}

files_count = int(input('File count: '))
files = {}

for i in range(files_count):
    file, *available_operations = input(f'File #{i}: ').lower().strip().split(' ')
    files[file] = available_operations

operations_count = int(input('Operation count: '))
output = ''

for i in range(operations_count):
    operation_type, file_name = input(f'Operation #{i}: ').lower().strip().split(' ')
    if operations[operation_type] in files[file_name]:
        output += 'OK\n'
    else:
        output += 'Access Denied\n'

print(output)