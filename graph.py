from termcolor import colored

from src.config import *


def percentage(currValue, fromValue, height):
    return currValue * height / fromValue


def calculateHeight(minValue, maxValue):
    # <math>
    return 30 + int(minValue / maxValue * 30)
    # </math> :)


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
    maxValue, minValue = max(dots.values()), min(dots.values())
    height = calculateHeight(minValue, maxValue)
    minHeight = int(percentage(minValue, maxValue, height))

    axisValue = maxValue
    oldAxisValue = maxValue + 1

    rainbow = len(COLORS)
    for i in range(height, minHeight - 1, -1):
        gridColor = COLORS[i % rainbow]
        for key, value in dots.items():
            if percentage(value, maxValue, height) >= i:
                printingChar = CHART_LINE
                if value < axisValue:
                    axisValue = value
            else:
                printingChar = GRID_LINE

            print(colored(printingChar, gridColor if printingChar == GRID_LINE else 'white'), end='', flush=True)

        print(colored('{}{}'.format(CHART_LEFT_BORDER, axisValue if axisValue != oldAxisValue else ''), gridColor), flush=True)
        oldAxisValue = axisValue

    # I think it's bullshit, but for now let it be
    # TODO
    dateStep = int((len(dots) - DATE_LENGTH * COUNT_OF_DATES) / COUNT_OF_DATES)
    print(colored(CHART_LOWER_BORDER, 'white') * len(dots))

    if dateStep > 0:
        dates = list(dots.keys())
        dateIntervals = [i / COUNT_OF_DATES for i in range(0, COUNT_OF_DATES + 1)]
        print((' ' * dateStep).join('{}'.format(dates[int((len(dates) - 1) * i)]) for i in dateIntervals))
