

def read_file(path):
    data = []
    with open(path, "r") as file:
        for line in file:
            if line[0] != '#':
                data.append(line)
    return data
