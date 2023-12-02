total = 0

lines = []
with open('inputs/input2.txt') as f:
    lines = f.readlines()

for line in lines:
    gameNumber = line.split(":")[0].split(" ")[1]
    handGrab = line.split(":")[1].split(";")

    minRed = 0
    minGreen = 0
    minBlue = 0

    for cubes in handGrab:
        singularColor = cubes.split(",")
        for single in singularColor:
            if single.strip().split(" ")[1] == "red":
                if int(single.strip().split(" ")[0]) > minRed:
                    minRed = int(single.strip().split(" ")[0])
            if single.strip().split(" ")[1] == "green":
                if int(single.strip().split(" ")[0]) > minGreen:
                    minGreen = int(single.strip().split(" ")[0])
            if single.strip().split(" ")[1] == "blue":
                if int(single.strip().split(" ")[0]) > minBlue:
                    minBlue = int(single.strip().split(" ")[0])

    total += (minRed * minGreen * minBlue)


print(total)
