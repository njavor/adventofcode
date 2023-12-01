sums, numdict = [0,0], {"one":['1',3], "two":['2',3] , "three":['3',5], "four":['4',4], "five":['5',4], "six":['6',3], "seven":['7',5], "eight":['8',5], "nine":['9',4]}

with open("input.txt", "r", encoding="utf8") as f:
    for line in f:
        numlists = [[],[]]
        for i in range(len(line)):
            try:
                if not int(line[i]) == None:
                    for numlist in numlists:
                        numlist.append(line[i])
            except:
                for num in numdict:
                    if i <= len(line)-numdict[num][1] and line[i:i+numdict[num][1]] == num: 
                        numlists[1].append(numdict[num][0])
        for i in range(len(sums)):
            sums[i] += int(numlists[i][0] + numlists[i][len(numlists[i])-1])

print(f"\n\nAoC 2023 - Day 1: Trebuchet?!\n Part One: {sums[0]}\n Part Two: {sums[1]}\n")