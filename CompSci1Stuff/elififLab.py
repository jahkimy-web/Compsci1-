# python lab
# Jahkeem pianhki
# 9/9/2026
# Step 1: Collect input from the user
go = False
while not go:
    try:
        age = int(input("Enter your age< "))
        height = int(input("Enter your height in inches< "))
        weight = int(input("Enter your weight in pounds<"))

# conversion
        feet = height // 12
        inches = height % 12

        print("You are " + str(height) + " inches tall. That is " + str(feet) + " feet and " + str(inches) + " inches tall.")
        go = True
    except(ValueError):
        print("This isn't a number")

# Step 3: see what they can ride
if height >= 48:
    print("You qualify for the Roller Coaster")
elif age >= 10:
    print("You can use the Haunted House")
elif weight < 250:
    print("You qualify for the Ferris Wheel")
else:
    print("Sorry, you are not allowed")

# Step 4: see if they can ride bumper cars
if age >= 8:
    print("you are old enough for Bumper Cars")
else:
    print("You are too young for Bumper Cars")
