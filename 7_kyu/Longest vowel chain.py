import re

vowels = ('a', 'e', 'i' ,'o' ,'u')

def solve(s):
    return max(
        [
            len(ones) for ones in re.findall(
            '1*', ''.join(['1' if letter in vowels else '0' for letter in s])
        )
        ]
    )
