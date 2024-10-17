print("Welcome to rollercoaster!")
height = int(input("Enter your Height in cm:\n"))
age = int(input("Enter your age:\n"))

if height >= 120:
    if age > 18:
        print("Please pay $12 for the ride!")
    else:
        print("Please pay $7 for the ride")
else:
    print("Sorry you need to grow some hair.")