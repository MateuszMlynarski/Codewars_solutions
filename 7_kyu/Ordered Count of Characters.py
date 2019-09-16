def ordered_count(input):
    return [(litera,input.count(litera)) for litera in list(dict.fromkeys([x for x in input]))]