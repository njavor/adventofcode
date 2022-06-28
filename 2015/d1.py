from colors import color

part = input("Which part are you solving: ")
input = input("Your input: ")

floor = 0

# PART 1
if part == "1":

    for char in input:
        if char == "(": floor += 1
        else: floor -= 1

    print (f"\nThe instructions take Santa to floor {color.GREEN}{floor}")

# PART 2
elif part == "2":

    i = 0
    for char in input:
        if char == "(": floor += 1
        else: floor -= 1
        i += 1
        if floor < 0:
            print (f"\nSanta first enter's the basement on character position {color.GREEN}{i}")
            break

print(color.WHITE)