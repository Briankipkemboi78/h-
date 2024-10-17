print("Welcome to rollercoaster!")
height = int(input("Enter your Height in cm:\n"))
bill = 0


if height >= 120:
    print("You can Ride")
    age = int(input("Enter your age:\n"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5!")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want a photo? Type y for Yes and n for No.\n ")
    if wants_photo == 'y':
        bill += 3
        
    print(f"Your total bill is ${bill}")

else:
    print("Sorry you need to grow some hair.")