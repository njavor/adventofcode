def part1(sor):
    res = 0
    if "A Y" in sor or "B Z" in sor or "C X" in sor: res = 6
    elif "A X" in sor or "B Y" in sor or "C Z" in sor: res = 3
    
    if "X" in sor: res += 1
    elif "Y" in sor: res += 2
    else: res += 3

    return res

def part2(sor):
    res = 0
    if "Y" in sor: res += 3
    elif "Z" in sor: res += 6

    if "B X" in sor or "A Y" in sor or "C Z" in sor: res += 1
    elif "C X" in sor or "B Y" in sor or "A Z" in sor: res += 2
    else: res += 3

    return res

p1_score, p2_score = 0, 0
with open("d2_input.txt", "r", encoding="utf8") as f:
    for sor in f:
        p1_score += part1(sor)
        p2_score += part2(sor)

print(f"part 1: {p1_score}\npart 2: {p2_score}")