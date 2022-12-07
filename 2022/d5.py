from copy import deepcopy

p1_sol, orders = [], []
with open("input.txt", "r", encoding="utf8") as f:
    for sor in f:
        if "[" in sor:
            line = sor.replace("[","").replace("]", "").replace("\n","").replace("    ", "0 ").split(" ")
            if p1_sol == []:
                for element in range(len(line)): p1_sol.append([])
            for column in range(len(line)): p1_sol[column].append(line[column].replace("0", ""))
        if sor == "\n":
            for crate in p1_sol:
                for a in range(len(crate)):
                    if crate[0] == "": crate.pop(0)
            p2_sol = deepcopy(p1_sol)
        if "move" in sor:
            orders = sor.replace("move","").replace("from","").replace("to","").split()
            for i in range(int(orders[0])):
                p1_sol[int(orders[2])-1].insert(0, p1_sol[int(orders[1])-1].pop(0))
                p2_sol[int(orders[2])-1].insert(i, p2_sol[int(orders[1])-1].pop(0))

print("part 1: ", end="")
for crate in p1_sol: print(crate[0], end="")
print("\npart 2: ", end="")
for crate in p2_sol: print(crate[0], end="")