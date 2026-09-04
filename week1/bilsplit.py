print("This program is an Resturant bill splitter. Please enter Numbers")

# prompting the user for input about total of bill
totalBill = float(input("What is the total bill amount: "))
peopleAmount = int(input("How many people is splitting the bill: "))

# doing an diversion opeartion to calculate what people have to pay
resturantSplit = round(totalBill / peopleAmount, 3)

# printing the total, how big the total is and how much everybody has to pay
print(
    "The bill total is: ",
    totalBill,
    "And the amount of people splitting the bill is:",
    peopleAmount,
    "The amount each person has to pay is:",
    float(resturantSplit),
)
