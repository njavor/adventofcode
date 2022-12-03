def part2(input, co2):
    for i in range(len(input[0])):
        templist, z, o = [], 0, 0
        for sor in input:
            if sor[i] == "0": z += 1
            else: o += 1
        if z <= o:
            for sor in input:
                if sor[i] == str(int(co2)): templist.append(sor)
        else:
            for sor in input:
                if sor[i] == str(int(not co2)): templist.append(sor)
        input = templist
        if len(input) == 1: break
    return input[0]

input, p1_gamma, p1_epsilon = [], "", ""
with open("input.txt", "r", encoding="utf8") as f:
    for sor in f: input.append(sor.strip())

for i in range(len(input[0])):
    z, o = 0, 0
    for sor in input:
        if sor[i] == "0": z += 1
        else: o += 1
    if z < o:
        p1_gamma += "1"
        p1_epsilon += "0"
    else:
        p1_gamma += "0"
        p1_epsilon += "1"

p2_oxygen, p2_co2 = part2(input, True), part2(input, False) 
        
print(f"part 1: {int(p1_gamma, 2)*int(p1_epsilon, 2)}\npart 2: {int(p2_oxygen, 2)*int(p2_co2, 2)}")