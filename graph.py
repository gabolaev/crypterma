from config import *


def percentage(currValue, fromValue):
    return currValue * HEIGHT / fromValue


def compress(dots):
    if len(dots) > WIDTH:
        compressedDots = dict()
        step = 1 + int(len(dots) / WIDTH)

        templist = []
        for i in enumerate(dots.items(), start=1):
            if not i[0] % step:
                nowDate = i[1][0]
                compressedDots[nowDate] = max(templist)
                templist.clear()
            templist.append(i[1][1])
        return compressedDots
    return dots


def plotting(dots):
    compressed = compress(dots)

    maxValue = max(compressed.values())
    minHeight = int(percentage(min(compressed.values()), maxValue))

    axisValue = maxValue
    oldAxisValue = maxValue + 1
    for i in range(HEIGHT, minHeight - 1, -1):
        for key, value in compressed.items():
            printingChar = GRID_LINE
            if percentage(value, maxValue) >= i:
                if value < axisValue:
                    axisValue = value
                printingChar = CHART_LINE
            print(printingChar, end='', flush=True)

        print('{}{}'.format(CHART_LEFT_BORDER, axisValue if axisValue != oldAxisValue else ''))
        oldAxisValue = axisValue

    # I think it's bullshit, but for now let it be
    dateStep = int((len(compressed) - DATE_LENGTH * COUNT_OF_DATES) / COUNT_OF_DATES)
    print(CHART_LOWER_BORDER * len(compressed))

    if dateStep > 0:
        compValues = list(compressed.keys())
        dateIntervals = [i / COUNT_OF_DATES for i in range(0, COUNT_OF_DATES + 1)]
        for i in dateIntervals:
            print(''.join('{}'.format(compValues[int((len(compValues) - 1) * i)])), end=' ' * dateStep)