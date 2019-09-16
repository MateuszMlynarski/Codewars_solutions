def next_happy_year(year):
    year += 1
    while len(list(set([i for i in map(int,list(str(year)))]))) != len([i for i in map(int,list(str(year)))]):
        year += 1
    return year