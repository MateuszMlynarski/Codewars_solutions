def row_sum_odd_numbers(n):
    return sum(range(2*sum(range(1,n))+1,2*sum(range(1,n+1))+1,2))