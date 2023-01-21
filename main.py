les = [[1, 3, 1, 5], [-1, -1, 1, 1], [2, 4, -1, 2]]

if les[0][0] == 0:
    les[1], les[0] = les[0], les[1]

def RemoveVariable(base, changing, index):
    coefficient = -1 * changing[index] / base[index]
    changing[:] = [changing[i] + x * coefficient for i, x in enumerate(base)]
    return changing

for i in range(1, len(les)):
    for j in range(i, len(les)):
        les[j] = RemoveVariable(les[i-1], les[j], i-1)

for i in range(1, len(les)):
    for j in range(i + 1, len(les) + 1):
        les[-j] = RemoveVariable(les[-i], les[-j], -i-1)

solutions = [x[-1]/x[i] for i, x in enumerate(les)]

print(solutions)