def SortAll(x, lines, leftL, rightL):

    for i in range(len(x)-1):
        sortString(x[i], x[i+1], lines, leftL, rightL)


def sortString(xko,druhe, lines, leftL, rightL):
    if [xko, druhe] in lines:
        return [xko, druhe]
    else:
        return [druhe, xko]

with open("puzzleCodes5_1.txt", 'r') as file:
    lines = file.read().splitlines()
    for i in range(len(lines)):
        lines[i] = lines[i].split('|')
    l1 = []
    l2 = []
    for i in range(len(lines)):
        l1.append(lines[i][0])
        l2.append(lines[i][1])
    print(l1)
    print(l2)
with open("puzzleCodes5_2.txt", 'r') as file:
    toCheck = file.read().splitlines()

print(toCheck)
res = 0
res2 = 0
for i in range (len(toCheck)):
    x = toCheck[i].split(',')
    print(x)
    bol = False
    for idx in range(len(x)):

        if x[idx] in l1:
            z = [index for index, value in enumerate(l1) if value == x[idx]]
            for index in z:
                if l2[index] in x:
                    if not idx < x.index(l2[index]):
                        bol = True
                        break

    if not bol:
        res += int(x[len(x)//2])
        print("res + ", x[len(x)//2])
    # part 2 starts here





print(res, res2)




print(lines)