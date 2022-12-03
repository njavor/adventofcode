p1_x, p1_y, p2_x, p2_y, p2_aim= 0, 0, 0, 0, 0
with open("input.txt", "r", encoding="utf8") as f:
    for sor in f:
        dirAndAm = ["", 0]
        dirAndAm = sor.split()
        match dirAndAm[0]:
            case "down": p1_x += int(dirAndAm[1])
            case "up": p1_x -= int(dirAndAm[1])
            case "forward": p1_y += int(dirAndAm[1])
        match dirAndAm[0]:
            case "down": p2_aim += int(dirAndAm[1])
            case "up": p2_aim -= int(dirAndAm[1])
            case "forward":
                p2_y += int(dirAndAm[1])
                p2_x += p2_aim*int(dirAndAm[1])

print(f"part 1: {p1_x*p1_y}\npart 2: {p2_x*p2_y}")