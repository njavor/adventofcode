from colors import color

part = input("Which part are you solving: ")
i = []
print("Your input:")
while True:
    line = input()
    if line: i.append(line)
    else: break

# PART 1
if part == "1":
    wpaper = 0

    for line in i:
        n = line.split("x")
        dim = [int(n[0]) * int(n[1]), int(n[0]) * int(n[2]), int(n[1]) * int(n[2])]
        wpaper += (2*(dim[0] + dim[1] + dim[2])) + min(dim)

    print(f"The elves should order {color.GREEN}{wpaper}{color.WHITE} square feet of wrapping paper")

# PART 2
elif part == "2":
    ribbon = 0

    for line in i:
        n = line.split("x")
        n = [int(j) for j in n]
        ribbon += (n[0] * n[1] * n[2]) + (2 * (min(n) + sorted(n)[1]))

    print(f"The elves should order {color.GREEN}{ribbon}{color.WHITE} feet of ribbon")