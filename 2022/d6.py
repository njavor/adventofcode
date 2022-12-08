def part1(input):
    res, dic = 3, []
    for i in range(3):
        dic.append(input[0])
        input = input[1:]
    for c in input: 
        res += 1
        if c in dic or 1 < dic.count(dic[0]) or 1 < dic.count(dic[1]) or 1 < dic.count(dic[2]):
            dic.append(c)
            dic.pop(0)
        else: return res

def part2(input):
    res, dic = 13, []
    for i in range(13):
        dic.append(input[0])
        input = input[1:]
    for c in input: 
        res += 1
        if c in dic or 1 < dic.count(dic[0]) or 1 < dic.count(dic[1]) or 1 < dic.count(dic[2]) or 1 < dic.count(dic[3]) or 1 < dic.count(dic[4]) or \
        1 < dic.count(dic[5]) or 1 < dic.count(dic[6]) or 1 < dic.count(dic[7]) or 1 < dic.count(dic[8]) or 1 < dic.count(dic[9]) or 1 < dic.count(dic[10]) or 1 < dic.count(dic[11]):
            dic.append(c)
            dic.pop(0)
        else: return res

input = ""
with open("input.txt", "r", encoding="utf8") as f: input = f.readline()
p1_marker = part1(input)
p2_marker = part2(input)

print(f"\n\nAOC2022 Day 6: Tuning Trouble\npart 1: {p1_marker}\npart 2: {p2_marker}")