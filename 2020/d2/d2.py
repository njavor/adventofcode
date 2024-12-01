y,d,t = 2020, 2, "Password Philosophy"
part1, part2 = 0,0

# --------------------------------

with open(f"{y}/d{d}/input.txt", "r", encoding="utf8") as f:
    for line in f:
        splitl = line.split()
        num1,num2 = int(splitl[0].split('-')[0]),int(splitl[0].split('-')[1])
        character,password = splitl[1][0], splitl[2]
        
        if num1 <= password.count(character) and password.count(character) <= num2:
            part1 += 1
        
        if (password[num1-1] == character) ^ (password[num2-1] == character):
            part2 += 1

# --------------------------------

print(f"\n\nAoC {y} | Day {d}: {t}")
print(f"           Part 1: {part1}")
print(f"           Part 2: {part2}")