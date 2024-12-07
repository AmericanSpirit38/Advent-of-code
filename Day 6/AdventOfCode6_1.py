with open("PuzzleCodes6.txt", 'r', encoding='utf-8') as file:
    lines = list(map(list, file.read().splitlines()))
l = False
r = False
t = False
b = False
pos = [0, 0]
for item in lines:
    if "^" in item:
        t = True
        pos = [item.index("^"), lines.index(item)]
        break
    if "v" in item:
        b = True
        pos = [item.index("v"), lines.index(item)]
        break
    if "<" in item:
        l = True
        pos = [item.index("<"), lines.index(item)]
        break
    if ">" in item:
        r = True
        pos = [item.index(">"), lines.index(item)]
        break

lines[pos[1]][pos[0]] = "X"
print(pos, r, l, t, b)
while 0 <= pos[0] < len(lines[0]) and 0 <= pos[1] < len(lines):
    if l:
        if pos[0] - 1 >= 0:
            if lines[pos[1]][pos[0] - 1] == "#":
                t = True
                l = False
            else:
                pos[0] -= 1
                lines[pos[1]][pos[0]] = "X"
        else:
            break
    if r:
        if pos[0] + 1 < len(lines[0]):
            if lines[pos[1]][pos[0]+1] == "#":
                b = True
                r = False
            else:
                pos[0] += 1
                lines[pos[1]][pos[0]] = "X"
        else:
            break
    if t:
        if pos[1] - 1 >= 0:
            if lines[pos[1] - 1][pos[0]] == "#":
                r = True
                t = False
            else:
                pos[1] -= 1
                lines[pos[1]][pos[0]] = "X"
        else:
            break

    if b:
        if pos[1] + 1 < len(lines):
            if lines[pos[1] + 1][pos[0]] == "#":
                l = True
                b = False
            else:
                pos[1] += 1
                lines[pos[1]][pos[0]] = "X"
        else:
            break
res = 0
for item in lines:
    res += item.count("X")
    print(item)
print(res)

