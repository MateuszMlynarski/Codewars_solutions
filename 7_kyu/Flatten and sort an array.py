def flatten_and_sort(array):
    return sorted([int(i) for i in ' '.join([' '.join(map(str, list)) for list in array]).split()])