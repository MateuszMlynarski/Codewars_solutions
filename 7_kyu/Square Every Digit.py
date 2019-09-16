def square_digits(num):
    return int(''.join(list(map(str,map(lambda x: x**2,map(int,list(str(num))))))))