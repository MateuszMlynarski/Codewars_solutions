def letter_count(s):
    return {key : s.count(key) for key in sorted(list(dict.fromkeys(s)))}

# Best practice
# from collections import Counter
# def letter_count(s):
#     return Counter(s)