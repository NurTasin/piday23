"""
calc_pi.py
Calculates the value of pi upto a certain decimal points.
Uses BBP Formula to calculate the value
Uses python's builtin decimal library to make the floating point calculations precise
Implemented by: @nurtasin (Nur Mahmud Ul Alam Tasin) [github.com/nurtasin/]
"""


import decimal
import time

def pi(precision):
    """
    The implementation of the BBP Formula
    the argument `precision` is the number of decimal points you want to calculate
    """
    decimal.getcontext().prec = precision
    decimal.getcontext().prec += 2
    three = decimal.Decimal(3)
    lasts = 0
    t = three
    s = three
    n = 1
    na = 0
    d = 0
    da = 24

    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t

    decimal.getcontext().prec -= 2
    return +s

if __name__=="__main__":
    fp=500000
    start_time=time.time()
    pi_val=pi(fp)
    req_time=time.time()-start_time
    with open(f"./pival-{fp}.txt","w+") as f:
        f.write(f"Calculating PI upto {fp} decimal points\n")
        f.write(f"\n[Calculated in {req_time} seconds]")
        f.write("[[@nurtasin]]")
        f.write(str(pi_val))