score = input("Enter Score: ")
xf = float(score)
if xf >=1:
    print("please enter correct score!")
elif xf >= 0.9:
    print("A")
elif xf >= 0.8:
    print("B")
elif xf >= 0.7:
    print("C")
elif xf >= 0.6:
    print("D")
elif xf < 0.6:
    print("F")
