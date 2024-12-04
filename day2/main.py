def read_data(filename):
    f = open(filename, 'r')
    data = f.read()
    return data

def tansform_data(data):
    data = data.split("\n\n")
    remove_newlines = [elem.rstrip() for elem in data]
    grouped_data = [elem.split("\n") for elem in remove_newlines][0]
    remove_whitespace = [elem.split() for elem in grouped_data]
    return remove_whitespace


if __name__ == "__main__":
    data = read_data('data.txt')
    data = tansform_data(data)
    print(data)
