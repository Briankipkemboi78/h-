print("Welcome to rollercoaster!")
height = int(input("Enter your Height in cm:\n"))


if height >= 120:
    print("You can Ride")
    age = int(input("Enter your age:\n"))
    if age < 12:
        print("Please pay $5 for the ride!")
    elif age >= 12 and age < 18:
        print("Please pay $7 for the ride")
    else:
        print("Please pay $12 for the ride")
else:
    print("Sorry you need to grow some hair.")