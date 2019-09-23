def func_or(a,b):
    return bool(a) or bool(b)

def func_xor(a,b):
    return func_or(a,b) and not (bool(a) and bool(b))

# Alternative solution
# def func_or(a, b):
#     return not (bool(a) == bool(b) == False)
#
# def func_xor(a, b):
#     return not (bool(a) == bool(b))