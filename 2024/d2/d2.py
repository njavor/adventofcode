y,d,t = 2024, 2, "Red-Nosed Reports"
part1, part2 = 0,0

# --------------------------------


# list1, list2 = [], []
with open(f"{y}/d{d}/input.txt", "r", encoding="utf8") as f:
    for line in f:
        splitline = [int(x) for x in line.split()]
        
        safe = True
        n, order = splitline[0], -1
        splitline.pop(0)

        for m in splitline:
            if abs(n-m) > 3 or n-m == 0:
                safe = False
            else:
                match order:
                    case "inc":
                        if n-m > 0: safe = False
                    case "dec":
                        if n-m < 0: safe = False
                    case -1:
                        if n-m < 0: order = "inc"
                        else: order = "dec"
            n = m
        if safe: part1 += 1

# --------------------------------

print(f"\n\nAoC {y} | Day {d}: {t}")
print(f"           Part 1: {part1}")
print(f"           Part 2: {part2}")