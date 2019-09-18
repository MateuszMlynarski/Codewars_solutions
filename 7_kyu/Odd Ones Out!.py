def odd_ones_out(numbers):
    my_dict = { key : numbers.count(key) for key in dict.fromkeys(numbers) }
    return [number for number in numbers if my_dict[number] % 2 == 0 ]

# best practice
# def odd_ones_out(numbers):
#     return [i for i in numbers if numbers.count(i) % 2 == 0]