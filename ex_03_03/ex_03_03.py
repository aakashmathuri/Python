sc = input('Enter score: ')
try :
    xsc = float(sc)
except :
    print('Error, please enter numeric input')
    quit()
if xsc >= 1.0 :
    print('error, please score between 0.9 to 0.0')
elif xsc >= 0.9 :
    print('A')
elif xsc >= 0.8 :
    print('B')
elif xsc >= 0.7 :
    print('C')
elif xsc >= 0.6 :
    print('D')
else :
    print('F')
