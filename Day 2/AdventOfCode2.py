with open('puzzleCodes2.txt', 'r') as file:
    sequences = [line.strip() for line in file]
res = 0

def sepNum(separateNum, res, didremove):
    if sorted(separateNum, reverse=True) == separateNum or sorted(separateNum, reverse=False) == separateNum:
        gud = True
        for x in range(len(separateNum)-1):
            diff = abs(separateNum[x] - separateNum[x+1])
            print(diff)
            if not (diff >= 1 and diff <= 3):
                if not didremove:
                    separateNum.remove(separateNum[x+1])
                    didremove = True
                else:
                    gud = False
                    print("False")
                    break
        if gud:
            res += 1
    return res

for i in range(len(sequences)):
    separateNum = list(map(int, sequences[i].split(' ')))
    print(separateNum)
    res = sepNum(separateNum, res, False)

res2 = 0
for i in range(len(sequences)):
    separateNum = list(map(int, sequences[i].split(' ')))
    print(separateNum)
    if sorted(separateNum, reverse=True) == separateNum or sorted(separateNum, reverse=False) == separateNum:
        res2 = sepNum(separateNum, res2, False)
    else:
        counter = 0
        for x in range(len(separateNum)-1):
            if separateNum[x+1] - separateNum[x] > 1:
                separateNum.remove(separateNum[x+1])
                counter += 1
            elif separateNum[x] - separateNum[x+1] > -1:
                separateNum.remove(separateNum[x+1])
                counter += 1
        if counter <= 1:
            res2 = sepNum(separateNum, res2, True)

print(res, res2)

