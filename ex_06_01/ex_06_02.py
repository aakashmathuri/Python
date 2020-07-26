no = int(input("Enter nth number: " ))
p,q = 0,0
x = int(no)
if x % 2 == 1:
    x = x / 2
    p1 = x * 7
    print(p1)
else:
    x = x / 2;
    q = 6 * (x - 1)
    print(q)
