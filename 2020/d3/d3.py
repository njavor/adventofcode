y,d,t = 2020, 3, "Toboggan Trajectory"
part1, part2 = 0,0

# --------------------------------

with open(f"{y}/d{d}/input.txt", "r", encoding="utf8") as f:
    for line in f:

# --------------------------------

print(f"\n\nAoC {y} | Day {d}: {t}")
print(f"           Part 1: {part1}")
print(f"           Part 2: {part2}")