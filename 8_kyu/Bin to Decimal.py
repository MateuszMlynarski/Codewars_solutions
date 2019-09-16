def bin_to_decimal(bin):
    dec=0
    for i in range(1,len(bin)+1):
        dec=dec+int(bin[-i])*2**(i-1)
    return dec