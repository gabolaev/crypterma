from termcolor import colored
from .configs.config import *


def percentage(curr_value, from_value, height):
    return curr_value * height / from_value


def calculate_height(min_value, max_value):
    return START_HEIGHT + int(min_value / max_value * START_HEIGHT)


def compress(dots):
    if len(dots) > WIDTH:
        compressed_dots = {}
        step = 1 + int(len(dots) / WIDTH)

        step_interval_prices = []
        for i in enumerate(dots.items(), start=1):
            if not i[0] % step:
                compressed_dots[i[1][0]] = max(step_interval_prices)
                step_interval_prices.clear()
            step_interval_prices.append(i[1][1])
        return compressed_dots
    return dots


def plotting(dots):
    dots = compress(dots)

    max_value, min_value = max(dots.values()), min(dots.values())
    height = calculate_height(min_value, max_value)
    min_height = int(percentage(min_value, max_value, height))

    axis_value = max_value
    old_axis_value = max_value + 1

    rainbow = len(COLORS)
    for i in range(height, min_height - 1, -1):
        grid_color = COLORS[i % rainbow]
        for key, value in dots.items():
            if percentage(value, max_value, height) >= i:
                printing_char = CHART_LINE
                axis_value = min(value, axis_value)
            else:
                printing_char = GRID_LINE
            print(colored(printing_char, grid_color if printing_char == GRID_LINE else 'white'), end='', flush=True)
        print(colored(f'{CHART_LEFT_BORDER}{axis_value if axis_value != old_axis_value else ""}', grid_color))
        old_axis_value = axis_value

    print(colored(CHART_LOWER_BORDER, 'white') * len(dots))

    dates = list(dots.keys())
    count_of_dates = int(len(dots) / (DATE_STRING_LENGTH + DATES_SPACE_LENGTH))

    if count_of_dates:
        date_intervals = [i / count_of_dates for i in range(0, count_of_dates + 1)]
        print((' ' * DATES_SPACE_LENGTH).join(f'{dates[int(i * (len(dates) - 1))]}' for i in date_intervals))
