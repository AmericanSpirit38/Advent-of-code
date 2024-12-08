with open("PuzzleCodes7.txt", 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()
res = 0
for item in lines:
    item = item.split(": ")
    trgt = int(item[0])
    toSumOrMul = list(map(int, item[1].split(" ")))
    print(trgt, toSumOrMul)
    answers = {toSumOrMul[0]}
    for i in range(1, len(toSumOrMul)):
        new_answers = set()
        for ans in answers:
            new_answers.add(ans + toSumOrMul[i])
            new_answers.add(ans * toSumOrMul[i])
        answers= new_answers
    if trgt in answers:
        res += trgt
    print(answers)
print(res)


