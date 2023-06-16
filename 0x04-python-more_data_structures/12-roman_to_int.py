#!/usr/bin/python3

# I : 1 / V : 5 / X : 10
# L : 50 / C : 100 / D : 500
# M : 1000
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0

    num = 0
    i = 0
    while i < len(roman_string):
        d = roman_string[i]
        after_d = '0'
        if i < len(roman_string) - 1:
            after_d = roman_string[i + 1]

        if d == 'M':
            num += 1000
        elif d == 'D':
            num += 500
        elif d == 'C':
            if after_d == 'D':
                num += 400
                i += 1
            elif after_d == 'M':
                num += 900
                i += 1
            else:
                num += 100
        elif d == 'L':
            num += 50
        elif d == 'X':
            if after_d == 'C':
                num += 90
                i += 1
            elif after_d == 'L':
                num += 40
                i += 1
            else:
                num += 10
        elif d == 'V':
            num += 5
        elif d == 'I':
            if after_d == 'V':
                num += 4
                i += 1
            elif after_d == 'X':
                num += 9
                i += 1
            else:
                num += 1
        else:
            return 0
        i += 1
    return num
