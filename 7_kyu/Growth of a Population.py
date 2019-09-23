def nb_year(p0, percent, aug, p, counter = 0):
    if p0 < p:
        counter += 1
        return nb_year(p0 * (1 + percent / 100) + aug, percent, aug, p, counter)
    else:
        return counter