from termcolor import colored

from src.config import *


def percentage(currValue, fromValue, height):
    return currValue * height / fromValue


def calculateHeight(minValue, maxValue):
    return START_HEIGHT + int(minValue / maxValue * START_HEIGHT)


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
        print(colored('{}{}'.format(CHART_LEFT_BORDER, axisValue if axisValue != oldAxisValue else ''), gridColor))
        oldAxisValue = axisValue

    print(colored(CHART_LOWER_BORDER, 'white') * len(dots))

    dates = list(dots.keys())
    countOfDates = int(len(dots) / (DATE_STRING_LENGTH + DATES_SPACE_LENGTH))

    if countOfDates:
        dateIntervals = [i / countOfDates for i in range(0, countOfDates + 1)]
        print((' ' * DATES_SPACE_LENGTH).join('{}'.format(dates[int(i * (len(dates) - 1))]) for i in dateIntervals))
