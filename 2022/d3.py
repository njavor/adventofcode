common = ""
def part1(sor):
    compartments = ["", "", ""]
    compartments[0], compartments[1] = sor[:len(sor)//2], sor[len(sor)//2:]
    common = list(set(compartments[0])&set(compartments[1]))

    if common[0].isupper(): return ord(common[0]) -38
    else: return ord(common[0]) -96

compartments = []
def part2(sor):
    compartments.append(sor.strip())
    if len(compartments) == 3:
        common = list(set(compartments[0])&set(compartments[1])&set(compartments[2]))
        compartments.clear()
        
        if common[0].isupper(): return ord(common[0]) -38
        else: return ord(common[0]) -96
    return 0

p1_sum, p2_sum = 0, 0
with open("d3_input.txt", "r", encoding="utf8") as f:
    for sor in f:
        p1_sum += part1(sor)
        p2_sum += part2(sor)
        
print(f"part 1: {p1_sum}\npart 2: {p2_sum}")