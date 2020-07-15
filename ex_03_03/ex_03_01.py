hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
xh = float(hours)
xr = float(rate)
if xh > 40:
    reg = xh * xr
    op = (xh - 40.0) * (xr * 0.5)
    xp = reg + op
else:
    xp = xh * xr
print(xp)
