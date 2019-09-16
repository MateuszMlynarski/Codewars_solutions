def small_enough(a, limit):
    if limit >= sorted(a, reverse = True)[0]:
        return True
    return False