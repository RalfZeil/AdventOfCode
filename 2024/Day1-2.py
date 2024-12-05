lines: list = []
with open('inputs/input1.txt') as f:
    lines = f.readlines()

leftNumbers: list = []
rightNumbers: list = []
totalDistance: int = 0

for line in lines:
    splitLines = line.split()
    leftNumbers.append(splitLines[0])
    rightNumbers.append(splitLines[1])

leftNumbers.sort()
rightNumbers.sort()

for leftNum in leftNumbers:
    appearances: int = 0

    for rightNum in rightNumbers:
        if int(leftNum) == int(rightNum):
            appearances += 1

    totalDistance += int(leftNum) * appearances


print(totalDistance)