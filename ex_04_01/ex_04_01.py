def computepay(h,r):
    try:
        h1 = float(h)
        r1 = float(r)
    except:
        print("Error, please enter numeric input")
        quit()
    if h1 > 40:
        reg = r1 * h1
        otp = (h1 - 40.0) * (r1 * 0.5)
        xp = reg + otp
    else:
        xp = h1 * r1
    return xp

xh = input("Enter Hours:")
xr = input("Enter Rate:")
p = computepay(xh,xr)
print("Pay",p)
