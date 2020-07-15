n = input('Enter Celsius: ')
try:
    cel = float(n)
    fahr = (cel * 9/5) + 32
    print(fahr)
except:
    print('Enter a number!')
