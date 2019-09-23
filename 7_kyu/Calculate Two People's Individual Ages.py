def get_ages(sum, difference):
    x, y = (sum + difference) / 2, (sum - difference) / 2
    if sum >= 0 and difference >= 0 and x >= 0 and y >= 0:
        return x,y
    return None