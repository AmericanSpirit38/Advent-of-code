with open('puzzleCodes.txt', 'r') as file:
    data = [tuple(map(int, line.split())) for line in file]
l = []
r = []
for i in range(len(data)):
    l.append(int(data[i][0]))
    r.append(int(data[i][1]))

res1 = 0
for i in range(len(l)):
    cnt = r.count(l[i])
    res1 += l[i] * cnt
res = 0
for i in range(len(l)):
    z = min(l)
    x = min(r)
    y = abs(x-z)
    res += y
    l.remove(z)
    r.remove(x)

print(res, res1)
