y,d,t = 2020, 1, "Report Repair"
part1, part2 = 0,0

# --------------------------------

numbers = []

with open(f"{y}/d{d}/input.txt", "r", encoding="utf8") as f:
    for line in f:
       numbers.append(int(line))

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] + numbers[j] == 2020:
            part1 = numbers[i]*numbers[j]
        if part2 == 0:
            for k in range(len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    part2 = numbers[i]*numbers[j]*numbers[k]

# --------------------------------

print(f"\n\nAoC {y} | Day {d}: {t}")
print(f"           Part 1: {part1}")
print(f"           Part 2: {part2}")