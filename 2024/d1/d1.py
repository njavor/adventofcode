y,d,t = 2024, 1, "Historian Hysteria"
part1, part2 = 0,0

# --------------------------------

list1, list2 = [], []

with open(f"{y}/d{d}/input.txt", "r", encoding="utf8") as f:
    for line in f:
       list1.append(int(line.split()[0]))
       list2.append(int(line.split()[1]))


for n1 in list1:
    part2 += n1 * list2.count(n1)

list1.sort()
list2.sort()
while list1:
    part1 += abs(list1[0]-list2[0])
    list1.pop(0)
    list2.pop(0)

# --------------------------------

print(f"\n\nAoC {y} | Day {d}: {t}")
print(f"           Part 1: {part1}")
print(f"           Part 2: {part2}")