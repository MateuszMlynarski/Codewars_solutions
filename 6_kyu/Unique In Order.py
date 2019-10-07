def unique_in_order(iterable):
    return [letter for i, letter in enumerate(iterable) if iterable[i-1] != letter or i == 0]