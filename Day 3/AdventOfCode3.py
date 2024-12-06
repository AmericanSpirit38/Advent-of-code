import re

with open('PuzzleCodes3.txt', 'r', encoding='utf-8') as file:
    data = file.read()
#part 1
pat = r"mul\((\d{1,3}),(\d{1,3})\)"
toMul = re.findall(pat, data)
print(toMul)
res = 0
for i in range(len(toMul)):
    res += int(toMul[i][0]) * int(toMul[i][1])

print(res)
#part 2
pt2 = "do()"
pt3 = "don't()"
start = 0
for i in range(data.count(pt2)):
    strt = data.find(pt3, start)
    end = data.find(pt2, strt)
    data = data[:strt] + data[end:]
toMul2 = re.findall(pat, data)
res2 = 0
for i in range(len(toMul2)):
    res2 += int(toMul2[i][0]) * int(toMul2[i][1])

print(res2)