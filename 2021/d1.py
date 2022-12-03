def part1(sor, before):
    if before < sor: return 1
    return 0

def part2(sor, before):
    now = [before[1], before[2], sor]
    if sum(before) < sum(now): return 1
    return 0
        
p1_increases, p2_increases, b4, b43 = 0, 0, 999, [999, 999, 999]
with open("input.txt", "r", encoding="utf8") as f:
    for sor in f:
        p1_increases += part1(int(sor), b4)
        p2_increases += part2(int(sor), b43)
        b4 = int(sor)
        b43.pop(0)
        b43.append(int(sor))
        
print(f"part 1: {p1_increases}\npart 2: {p2_increases}")