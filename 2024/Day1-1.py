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

for i in range(len(leftNumbers)):
    totalDistance += abs(int(leftNumbers[i]) - int(rightNumbers[i]))

print(totalDistance)