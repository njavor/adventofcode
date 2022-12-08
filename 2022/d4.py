p1_fullcontain, p2_contain, pair = 0, 0, [0, 0]
with open("input.txt", "r", encoding="utf8") as f:
    for sor in f:
        pair = sor.strip().split(",")
        pair[0], pair[1] = [int(n) for n in pair[0].split("-")], [int(n) for n in pair[1].split("-")]
        if (pair[0][0] <= pair[1][0] <= pair[0][1] and pair[0][0] <= pair[1][1] <= pair[0][1]) or (pair[1][0] <= pair[0][0] <= pair[1][1] and pair[1][0] <= pair[0][1] <= pair[1][1]):
            p1_fullcontain += 1
        if (pair[0][0] <= pair[1][0] <= pair[0][1] or pair[0][0] <= pair[1][1] <= pair[0][1]) or (pair[1][0] <= pair[0][0] <= pair[1][1] or pair[1][0] <= pair[0][1] <= pair[1][1]):
            p2_contain += 1
        pair.clear()

print(f"\n\nAOC2022 Day 4: Camp Cleanup\npart 1: {p1_fullcontain}\npart 2: {p2_contain}")