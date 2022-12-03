elfs, calories = [], 0
with open("input.txt", "r", encoding="utf8") as f:
    for sor in f:
        if sor == "\n":
            elfs.append(calories)
            calories = 0
        else: calories += int(sor)

elfs.sort(reverse=True)
print(f"part 1: {elfs[0]}\npart 2: {elfs[0]+elfs[1]+elfs[2]}")