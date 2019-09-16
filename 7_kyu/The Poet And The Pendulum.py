def pendulum(values):
    values.sort()
    return values[2::2][::-1] + values[0:1:] + values[1::2]