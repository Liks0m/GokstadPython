age = int(input("What is your age: "))
hasID = input("do you have your ID: ").lower() == "yes"
is_vip = input("are you an vip: ").lower() == "yes"
raining = input("Is it raining today: ").lower() == "yes"
temperature = int(input("What is the the temperature: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are under 18")

if raining:
    print("It is raining today!")
else:
    print("It is not raining today")

if temperature >= 25:
    print("It is warm.")
elif temperature >= 15:
    print("It is mild")
else:
    print("It is cold")

if (age >= 18 and hasID) or is_vip:
    print("Entry allowed.")
elif age >= 18:
    print("You must have an valid ID.")
else:
    print("You must be 18 or older.")
