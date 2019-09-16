def max_tri_sum(num):
    sum=0
    s=set(num)
    sum+=max(s)
    s=s.difference({max(s)})
    sum+=max(s)
    s=s.difference({max(s)})
    sum+=max(s)
    return sum