with open('PuzzleCodes4.txt', 'r') as file:
    lines = file.read().splitlines()
print(lines)
Leers = [list(line) for line in lines]
print(Leers)

indicesX = []
indicesM = []
indicesA = []
indicesS = []
for i in range(len(Leers)):
    for j, ltr in enumerate(Leers[i]):
        if ltr == "X":
            idx = [i, j]
            indicesX.append(idx)
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

for i in range(len(indicesX)):
    pos = indicesX[i]
    l1 = [[pos[0]-1, pos[1]], [pos[0]+1, pos[1]], [pos[0], pos[1]-1], [pos[0], pos[1]+1], [pos[0]-1, pos[1]-1], [pos[0]-1, pos[1]+1], [pos[0]+1, pos[1]-1],[pos[0]+1, pos[1]+1]]
    print(l1)
    commell = [item for item in l1 if item in indicesM]
    print("comell:", commell)
    if commell:
        for l in commell:
            pos2 = [l[0] + (l[0] - pos[0]), l[1] + (l[1] - pos[1])]
            print("pos2:", pos2)
            if pos2 in indicesA:
                pos3 = [pos2[0] + (l[0] - pos[0]), pos2[1] + (l[1] - pos[1])]
                if pos3 in indicesS:
                    res += 1



print("All indices of 'X':", indicesX)
print("All indices of 'M':", indicesM)
print(indicesA)
print(res)
