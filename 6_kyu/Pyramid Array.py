def pyramid(n):
    if n == 0:
        return list()
    else:
        elements = pyramid(n-1)
        elements.append([1 for i in range(n)])
        return elements

# Best practice
# def pyramid(n):
#     return [ [1] * i for i in range(1, n+1) ]