sums, bagdict = [0,0], {"red":12, "green":13, "blue":14}

with open("input.txt", "r", encoding="utf8") as f:
    for line in f:
        splitline, possible = line.strip().split(':'), True

        gamenum = int(splitline[0].replace(splitline[0][:5], ''))
        minbag = {"red": 0, "green":0, "blue":0}
        for subset in splitline[1].split(';'):
            currentbag = dict(bagdict)
            for cubes in subset.split(','):
                data = cubes.split(' ')

                currentbag[data[2]] = currentbag[data[2]] - int(data[1])
                if currentbag[data[2]] < 0: possible = False
                if minbag[data[2]] < int(data[1]): minbag[data[2]] = int(data[1])
        if possible: sums[0] += gamenum
        sums[1] += minbag["red"]*minbag["green"]*minbag["blue"]

print(f"\n\nAoC 2023 - Day 2: Cube Conundrum\n Part One: {sums[0]}\n Part Two: {sums[1]}\n")