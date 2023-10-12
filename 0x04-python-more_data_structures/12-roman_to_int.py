#!/usr/bin/python3

def rom_sub(ls_num):
    rm_sb = 0
    max_nm = max(ls_num)

    for i in ls_num:
        if max_nm > i:
            rm_sb = rm_sb + i

    return (max_nm - rm_sb)


def roman_to_int(roman_string):
    """a func that converts a Roman numeral to an integer."""
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_nm = {"I": 1, "V": 5, "X": 10,
                "L": 50, "C": 100, "D": 500, "M": 1000}
    get_rom_keys = list(roman_nm.keys())

    nm = 0
    last_roman = 0
    ls_num = [0]

    for c in roman_string:
        for rom_key in get_rom_keys:
            if rom_key == c:
                if roman_nm[c] <= last_roman:
                    nm += rom_sub(ls_num)
                    ls_num = [roman_nm[c]]
                else:
                    ls_num.append(roman_nm[c])

                last_roman = roman_nm[c]
    nm = nm + rom_sub(ls_num)
    return (nm)
