p1_sum, p2_sum = 0, 0
with open("input.txt", "r", encoding="utf8") as f:
    for sor in f:
        p1_numbers, p2_numbers = [], []
        for i in range(len(sor)):
            try:
                if not int(sor[i]) == None: 
                    p1_numbers.append(sor[i])
                    p2_numbers.append(sor[i])
            except:
                match sor[i]:
                    case "o":
                        if i <= len(sor)-3 and sor[i:i+3] == "one": p2_numbers.append('1')
                    case "t":
                        if i <= len(sor)-3 and sor[i:i+3] == "two": p2_numbers.append('2')
                        if i <= len(sor)-5 and sor[i:i+5] == "three": p2_numbers.append('3')
                    case "f":
                        if i <= len(sor)-4 and sor[i:i+4] == "four": p2_numbers.append('4')
                        if i <= len(sor)-4 and sor[i:i+4] == "five": p2_numbers.append('5')
                    case "s":
                        if i <= len(sor)-3 and sor[i:i+3] == "six": p2_numbers.append('6')
                        if i <= len(sor)-5 and sor[i:i+5] == "seven": p2_numbers.append('7')
                    case 'e':
                        if i <= len(sor)-5 and sor[i:i+5] == "eight": p2_numbers.append('8')
                    case "n":
                        if i <= len(sor)-4 and sor[i:i+4] == "nine": p2_numbers.append('9')
        p1_sum += int(p1_numbers[0]+p1_numbers[len(p1_numbers)-1])
        p2_sum += int(p2_numbers[0]+p2_numbers[len(p2_numbers)-1])

print(f"\n\nAOC2023 Day 1: Trebuchet?!\npart 1: {p1_sum}\npart 2: {p2_sum}")