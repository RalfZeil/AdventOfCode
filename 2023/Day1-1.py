def main():
    # Read out the file and put them into the lines array
    lines = ""
    with open('inputs/input1-1.txt') as f:
        lines = f.readlines()

    sumCalibration = 0;

    for line in lines:
        firstNumber = None
        lastNumber = None

        for char in line:
            if char.isnumeric():
                if firstNumber is None:
                    firstNumber = char

                lastNumber = char

        print(firstNumber, lastNumber)
        sumCalibration += int(firstNumber + lastNumber)

    print(sumCalibration)


if __name__ == "__main__":
    main()
