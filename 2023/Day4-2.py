lines = []
with open('inputs/input4.txt') as f:
    lines = f.readlines()

# Key = card number INT
# Value = card amount INT
cards = {1: 0}

for line in lines:
    print(cards)
    currentCard = line.split('|')[0].split(':')[0].split(' ')[-1]
    # Apply default card
    if int(currentCard) not in cards.keys():
        cards[int(currentCard)] = 1
    else:
        cards[int(currentCard)] += 1

    winningNumbers = line.split('|')[0].split(':')[1].strip().split(' ')
    numbers = line.split('|')[1].strip().split(' ')

    # remove empty elements
    while '' in numbers:
        numbers.remove('')
    while '' in winningNumbers:
        winningNumbers.remove('')

    for i in range(cards.get(int(currentCard))):
        points = 0
        for num in numbers:
            if num in winningNumbers:
                points += 1

        for i in range(points):
            indexCard = int(i + int(currentCard) + 1)
            if indexCard > 198:
                break
            if indexCard in cards.keys():
                cards[indexCard] += 1
            else:
                cards[indexCard] = 1


print(sum(cards.values()))
