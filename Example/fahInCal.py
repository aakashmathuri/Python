n = input("Enter Fahrenheit Temperature: ")
try:
    fahr = float(n)
    cel = (fahr - 32) * 5.0 / 9.0
    print(cel)
except:
    print('Enter a number!')
