# python lab
# Jahkeem pianhki
# 9/10/2026
# Conditional lab
print("lab 1")
num1 = int(input("Enter an integer> "))

if num1 > 0:
    print(f"{num1} is posi1tive.")
elif num1 < 0:
    print(f"{num1} is negative.")
else:
    print(f"{num1} is zero.")
print()
print("lab 2")
num2 = int(input("Enter a number: "))

# even or odd; useful for usaccwodnci
if num2 % 2 == 0:
    print(num2, "is an even number.")
else:
    print(num2, "is an odd number.")

print()


print("lab 3")
age = int(input("enter age>"))

if age >= 18:
    print("You can vote")
else:
    years_left = 18 - age
    print(f"You cannot vote yet. You have {years_left} years left.")

print()


print("lab 4")
score = int(input("Enter your score (0 to 100): "))

if score >= 90:
    print("grade is A")
elif score >= 80:
    print("grade is B")
elif score >= 70:
    print("grade is C")
elif score >= 60:
    print("grade is D")
else:
    print("Grade: F")

print()


print("lab 5")
color = input("Enter a traffic light color (red, yellow, green): ").lower()
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Slow down")
elif color == "green":
    print("Go")
else:
    print("Invalid color, Traffic Lights aren't", color + "!")


print("lab 6")
calc_num1 = float(input("Enter a number> "))
calc_num2 = float(input("Enter another number> "))
operator = input("Enter an operator such as +, -, *, or /> ")


if operator == "+":
    result = calc_num1 + calc_num2
    print(calc_num1, "+", calc_num2, "=", result)
elif operator == "-":
    result = calc_num1 - calc_num2
    print(calc_num1, "-", calc_num2, "=", result)
elif operator == "*":
    result = calc_num1 * calc_num2
    print(calc_num1, "*", calc_num2, "=", result)
elif operator == "/":
    if calc_num2 == 0:
        print('you cant do that bro')
    else:
        result = calc_num1 / calc_num2
        print(calc_num1, "/", calc_num2, "=", result)
else:
    print("Invalid operator!")