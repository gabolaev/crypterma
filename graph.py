from termcolor import colored

from src.config import *


def percentage(currValue, fromValue):
    return currValue * HEIGHT / fromValue


def getRandomColor():
    import random
    return random.choice(COLORS)


def compress(dots):
    if len(dots) > WIDTH:
        compressedDots = dict()
        step = 1 + int(len(dots) / WIDTH)

        stepIntervalPrices = []
        for i in enumerate(dots.items(), start=1):
            if not i[0] % step:
                compressedDots[i[1][0]] = max(stepIntervalPrices)
                stepIntervalPrices.clear()
            stepIntervalPrices.append(i[1][1])
        return compressedDots
    return dots


def plotting(dots):
    dots = compress(dots)
    maxValue = max(dots.values())
    minHeight = int(percentage(min(dots.values()), maxValue))

    axisValue = maxValue
    oldAxisValue = maxValue + 1

    rainbow = len(COLORS)
    for i in range(HEIGHT, minHeight - 1, -1):
        gridColor = COLORS[i % rainbow]
        for key, value in dots.items():
            if percentage(value, maxValue) >= i:
                printingChar = CHART_LINE
                if value < axisValue:
                    axisValue = value
            else:
                printingChar = GRID_LINE

            print(colored(printingChar, gridColor if printingChar == GRID_LINE else 'white'), end='')

        print(colored('{}{}'.format(CHART_LEFT_BORDER, axisValue if axisValue != oldAxisValue else ''), gridColor))
        oldAxisValue = axisValue

    # I think it's bullshit, but for now let it be
    dateStep = int((len(dots) - DATE_LENGTH * COUNT_OF_DATES) / COUNT_OF_DATES)
    print(colored(CHART_LOWER_BORDER, 'white') * len(dots))

    if dateStep > 0:
        dates = list(dots.keys())
        dateIntervals = [i / COUNT_OF_DATES for i in range(0, COUNT_OF_DATES + 1)]
        print((' ' * dateStep).join('{}'.format(dates[int((len(dates) - 1) * i)]) for i in dateIntervals))
