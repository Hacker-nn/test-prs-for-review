def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

content = read_file(input("Enter filename: "))