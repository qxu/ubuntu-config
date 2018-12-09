#!/usr/bin/env python3

import argparse
import subprocess
import bisect
import math


brightness_values = set([0, 1])
brightness_num_steps = 12
brightness_values.update([(i / brightness_num_steps) ** 4 for i in range(brightness_num_steps + 1)])
brightness_values = {value for value in brightness_values if value >= 0.11737089201877934 / 100}
brightness_values = sorted(brightness_values)


def get_brightness():
    light_g = subprocess.run(['light', '-G'], stdout=subprocess.PIPE)
    output = light_g.stdout.decode('utf-8')
    first_part = output.split()[0]
    return float(first_part.strip()) / 100


def set_brightness(value):
    if value < 0:
        value = 0
    elif value > 1:
        value = 1

    subprocess.run(['light', '-S', str(value * 100)], stdout=subprocess.DEVNULL)


def inc_brightness(normalize=True):
    prev_brightness = get_brightness()
    brightness = prev_brightness
    index = bisect.bisect_right(brightness_values, brightness)
    if normalize and index >= len(brightness_values):
        index = len(brightness_values) - 1
        if index >= 0:
            set_brightness(brightness_values[index])
        return index
    elif index < len(brightness_values):
        while True:
            set_brightness(brightness_values[index])
            brightness = get_brightness()
            if brightness != prev_brightness or index >= len(brightness_values) - 1:
                break
            index += 1
        return index
    else:
        return index


def dec_brightness(normalize=True):
    prev_brightness = get_brightness()
    brightness = prev_brightness
    index = bisect.bisect_left(brightness_values, brightness) - 1
    if normalize and index < 0:
        index = 0
        if index < len(brightness_values):
            set_brightness(brightness_values[index])
        return index
    elif index >= 0:
        while True:
            set_brightness(brightness_values[index])
            brightness = get_brightness()
            if brightness != prev_brightness or index <= 0:
                break
            index -= 1
        return index
    else:
        return index


def print_brightness(value=None):
    if value is None:
        value = get_brightness()
    print('{0:.4f}'.format(value))


def main():
    arg_parser = argparse.ArgumentParser(description='Change brightness')
    command_group = arg_parser.add_mutually_exclusive_group()
    command_group.add_argument('-g', '--get', action='store_true',
        help='Get the brightness')
    command_group.add_argument('-s', '--set', type=float,
        help='Set the brightness [0.0, 1.0]')
    command_group.add_argument('-i', '--inc', action='store_true',
        help='Increment the brightness')
    command_group.add_argument('-d', '--dec', action='store_true',
        help='Decrement the brightness')
    command_group.add_argument('-l', '--list', action='store_true',
        help='List the brightness increment/decrement values')

    args = arg_parser.parse_args()

    if args.get:
        print_brightness()
    if args.list:
        print('\n'.join(map(str, brightness_values)))

    if args.set is not None:
        set_brightness(args.set)
        print_brightness()
    elif args.inc:
        print(inc_brightness() + 1)
    elif args.dec:
        print(dec_brightness() + 1)


if __name__ == '__main__':
    main()

