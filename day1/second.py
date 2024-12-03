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

def get_lefts(data):
    return [x[0] for x in data]

def get_rights(data):
    return [x[1] for x in data]

def to_int(data):
    return [int(x) for x in data]

def similarity(lefts, rights):
    return sum([rights.count(x) * x for x in lefts])

if __name__ == "__main__":
    data = read_data('data.txt')
    data = tansform_data(data)
    lefts = get_lefts(data)
    lefts_as_ints = to_int(lefts)
    rights = get_rights(data)
    rights_as_ints = to_int(rights)
    similarity = similarity(lefts_as_ints, rights_as_ints)
    print(similarity)
