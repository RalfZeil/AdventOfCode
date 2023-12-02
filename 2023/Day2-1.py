maxRed = 12
maxGreen = 13
maxBlue = 14

total = 0

lines = []
with open('inputs/input2.txt') as f:
    lines = f.readlines()

for line in lines:
    isValid = True
    gameNumber = line.split(":")[0].split(" ")[1]
    handGrab = line.split(":")[1].split(";")

    for cubes in handGrab:
        singularColor = cubes.split(",")
        for single in singularColor:
            if single.strip().split(" ")[1] == "red":
                if int(single.strip().split(" ")[0]) > maxRed:
                    isValid = False
            if single.strip().split(" ")[1] == "green":
                if int(single.strip().split(" ")[0]) > maxGreen:
                    isValid = False
            if single.strip().split(" ")[1] == "blue":
                if int(single.strip().split(" ")[0]) > maxBlue:
                    isValid = False

    if isValid:
        print("Added: ", gameNumber, " to ", total)
        total += int(gameNumber)


print(total)
