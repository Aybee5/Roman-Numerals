numerals = {
    1000: 'M',
    500: 'D',
    100: 'C',
    50: 'L',
    10: 'X',
    5: 'V',
    1: 'I'
}


def indian_to_roman(number):
    roman = ''
    previous = -1
    for numeral in numerals.keys():
        repeat = int(number / numeral)
        if repeat > 0:
            if previous > 0 and repeat == 4:
                roman += numerals[numeral] + numerals[previous]
            else:
                roman += repeat * numerals[numeral]
        number %= numeral
        previous = numeral
    return roman


def roman():
    num = int(input("Enter an Intiger number between 0-50: "))
    if (num > 0):
        print(indian_to_roman(number))
    else:
        print("Error, number has to be 1 or greater.")
