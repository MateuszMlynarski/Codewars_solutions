def expression_matter(a, b, c):
    if a==1 and c==1:return a+b+c
    elif a==1: return (a+b)*c
    elif c==1: return a*(b+c)
    elif b==1: return (b+min(a,c))*max(a,c)
    else: return a*b*c