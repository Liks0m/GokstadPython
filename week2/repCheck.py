# efficent non for loops invloved solution
print("Cinema seats to the right numbers")
cinemaRow = range(0, 21, 2)
print(list(cinemaRow))

# Unefficent way with for loops and if statement
print("Cinema seats to the right numbers")
for i in range(21):
    if i % 2 == 0:
        print(i)


# Gym Rep teller
print("Easy gym rep counter")
for i in range(21):
    print(i)
