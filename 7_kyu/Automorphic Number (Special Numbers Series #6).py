def automorphic(n):
    if n%10**(len(str(n))) == ((n%10**(len(str(n))))**2)%10**(len(str(n))): return "Automorphic"
    else: return "Not!!"