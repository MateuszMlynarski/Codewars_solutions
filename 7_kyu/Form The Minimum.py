def min_value(digits):
    l=sorted(list(dict.fromkeys(digits)))
    sl=''.join(str(v) for v in l)
    return int(sl)