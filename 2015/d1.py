from colors import color

i = input("Your input: ")
part = input("Which part are you solving: ")

floor = 0

# PART 1
if part == "1":

    for char in i:
        if char == "(": floor += 1
        else: floor -= 1

    print (f"\nThe instructions take Santa to floor {color.GREEN}{floor}")

# PART 2
elif part == "2":

    cp = 0
    for char in i:
        if char == "(": floor += 1
        else: floor -= 1
        cp += 1
        if floor < 0:
            print (f"\nSanta first enter's the basement on character position {color.GREEN}{cp}")
            break

print(color.WHITE)