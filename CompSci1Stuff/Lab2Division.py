# all about you
# Jahkeem pianhki
# 8/26/2026

name = input("What is your name? ")
age = int(input("How old are you? "))
year = int(input("What year was your last birthday? "))

print("---")

print("Your name is", name.capitalize(), "and you are", age, "years old.")

born = year - age
print("You were born in", born)

future_age = age + 10
print("In 10 years, you will be", future_age)

days = age * 365
print("You have lived for about", days, "days!")

# challenge
age_2050 = age + (2050 - year)
print("In the year 2050, you will be", age_2050)
# number lab
# Jahkeem pianhki
# 8/26/2026


x = int(input("enter int for x: "))
y = int(input("enter int for y: "))
z = float(input("enter float for z: "))

print("---")

print("Product of x and y is", x * y)

print("Product of x, y, and z is", round(x * y * z, 2))

print(x, "mod 2 is", x % 2)
print(y, "mod 2 is", y % 2)
print(z, "mod 2 is", round(z % 2, 2))
