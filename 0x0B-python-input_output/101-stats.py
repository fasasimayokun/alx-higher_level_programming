#!/usr/bin/python3
"""the printer func """


from sys import stdin


stats_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }

total_count = nm = 0


def display():
    """a func that prints the stats"""
    print(f"File size: {total_count}")
    for ky, val in sorted(stats_codes.items()):
        if val > 0:
            print("{:s}: {:d}".format(ky, val))


try:
    for ln in stdin:
        split_ln = ln.split()
        if len(split_ln) >= 2:
            stat = split_ln[-2]
            total_count += int(split_ln[-1])
            if stat in stats_codes:
                stats_codes[stat] += 1

        nm = nm + 1

        if nm % 10 == 0:
            display()
    display()
except KeyboardInterrupt as err:
    display()
