hrs = input('Enter Hours: ')
rt = input('Enter Rate: ')
try:
    xhrs = float(hrs)
    xrt = float(rt)
except:
    print('Error, please enter numeric input')
    quit()
if xhrs > 40:
    req = xhrs * xrt
    op = (xhrs - 40.0) * (xrt * 0.5)
    xp = req + op
else:
    xp = xhrs * xrt
print('Pay',xp)
