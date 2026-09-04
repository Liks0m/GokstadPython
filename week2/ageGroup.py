age = int(input("What is your age: "))

if age <= 13:
    ageGroup = "Child"
elif 13 <= age < 17:
    ageGroup = "Teenager"
elif age >= 18:
    ageGroup = "Adult"
else:
    print("You need to input correct age!")

print(f"You are an {ageGroup}")
