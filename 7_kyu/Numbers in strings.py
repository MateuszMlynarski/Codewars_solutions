def solve(s):
    return max([int(number) for number in ''.join([letter if letter.isnumeric() else ' ' for letter in s]).split(' ') if number.isnumeric()])