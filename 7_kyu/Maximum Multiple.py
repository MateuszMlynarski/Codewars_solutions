def max_multiple(divisor, bound):
    N = divisor
    while 0 < N <= bound:
        N += divisor
    return N - divisor

# Best practices
# def max_multiple(divisor, bound):
#     return bound - (bound % divisor)
#
# def max_multiple(divisor, bound):
#     return bound // divisor * divisor
#
# max_multiple = lambda divisor, bound: bound - (bound % divisor)