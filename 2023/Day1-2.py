from typing import List
from word2number import w2n

numbersInText: List[str] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

lines = []
with open('inputs/input1-1.txt') as f:
    lines = f.readlines()

sumCalibration: int = 0

for line in lines:
    firstNumber: int = None
    lastNumber: int = None
    textNumbers: List[str] = []

    # Extract written numbers from line
    for num in numbersInText:
        if num in line:
            textNumbers.append(num)

    # Extract numbers from line
    for char in line:
        if char.isdigit():
            if firstNumber is None:
                firstNumber = char

            lastNumber = char

    # Compare position of written and literal numbers in line
    for textNum in textNumbers:
        if line.find(textNum) < line.find(firstNumber):
            firstNumber = textNum

        if line.rfind(textNum) > line.rfind(lastNumber):
            lastNumber = textNum

    sumCalibration += int(str(w2n.word_to_num(firstNumber)) + str(w2n.word_to_num(lastNumber)))

print(sumCalibration)
