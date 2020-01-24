birthYear = int(input("What year were you born in? "))
currentYear = int(input("What is the current year? "))

print("Your age is ", currentYear - birthYear)

age = currentYear - birthYear

if age >= 18:
    print("You can drink alcohol")
else:
    print("Too young mate")