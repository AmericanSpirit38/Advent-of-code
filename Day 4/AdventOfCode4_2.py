with open('PuzzleCodes4.txt', 'r') as file:
    lines = file.read().splitlines()
print(lines)
Leers = [list(line) for line in lines]
print(Leers)


indicesM = []
indicesA = []
indicesS = []
for i in range(len(Leers)):
    for j, ltr in enumerate(Leers[i]):

        if ltr == "M":
            idx = [i, j]
            indicesM.append(idx)

        if ltr == "A":
            idx = [i, j]
            indicesA.append(idx)

        if ltr == "S":
            idx = [i, j]
            indicesS.append(idx)

res = 0

for i in range(len(indicesA)):
    pos = indicesA[i]
    l1 = [[pos[0]-1, pos[1]-1], [pos[0]+1, pos[1]+1]]
    l2 = [[pos[0]-1, pos[1]+1], [pos[0]+1, pos[1]-1]]
    l3 = [item for item in l1 if item in indicesM]
    l4 = [item for item in l2 if item in indicesM]
    if len(l3) == 1 and len(l4) == 1:
        l5 = [item for item in l1 if item in indicesS]
        l6 = [item for item in l2 if item in indicesS]
        if len(l5) == 1 and len(l6) == 1:
            res += 1




print(indicesA)
print(res)