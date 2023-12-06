from typing import TypeAlias

lines = []
with open('inputs/input3.txt') as f:
    lines = f.read()

schematic = [list(row.split()) for row in lines.strip().split('\n')]
print(schematic)


def GetSpecialCharacterIndexes(string) -> list[int]:
    indexes = []
    symbols = set('!@#$%^&*+_-=')
    for i in range(len(string)):
        if string[i] in symbols:
            indexes.append(i)
    return indexes


for line in schematic:
    specialChars = GetSpecialCharacterIndexes(line)
    print(specialChars)