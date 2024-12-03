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

def lefts_and_rights(data):
    return [int(x[0]) for x in data], [int(x[1]) for x in data]

def get_distances(lefts, rights):
    lefts.sort()
    rights.sort()
    zips = list(zip(lefts, rights))
    return [abs(tuple[0] - tuple[1]) for tuple in zips]

def similarity(lefts, rights):
    return sum([rights.count(x) * x for x in lefts])

if __name__ == "__main__":
    data = read_data('data.txt')
    data = tansform_data(data)
    lefts, rights = lefts_and_rights(data)
    distances = get_distances(lefts, rights)
    similarity = similarity(lefts, rights)
    print(f"sum of distances is: {sum(distances)}")
    print(f"sum of similarities is: {similarity}")
