def max_gap(numbers):
    return max([abs(sorted(numbers)[number] - sorted(numbers)[number+1])for number in range(0,len(numbers)-1)])