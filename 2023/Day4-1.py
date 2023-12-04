lines = []
with open('inputs/input4.txt') as f:
    lines = f.readlines()

total = 0

for line in lines:
    points = 0
    winningNumbers = line.split('|')[0].split(':')[1].strip().split(' ')
    numbers = line.split('|')[1].strip().split(' ')

    # remove empty elements
    while '' in numbers:
        numbers.remove('')
    while '' in winningNumbers:
        winningNumbers.remove('')

    for num in numbers:
        if num in winningNumbers:
            if points == 0:
                points = 1
            else:
                points = points * 2

    total += points

print(total)